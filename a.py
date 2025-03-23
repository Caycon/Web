#!/usr/bin/env sage -python
from pwn import remote
import json
from sage.all import *

# ======= Parameters from the challenge =======
p = 2**192 - 237
a = -3
b = 1379137549983732744405137513333094987949371790433997718123
order_full = 6277101735386680763835789423072729104060819681027498877478

# ======= Re-implementation of the ladder =======
def dbl(P):
    X, Z = P
    XX = (X**2) % p
    ZZ = (Z**2) % p
    A = 2 * (((X + Z)**2 - XX - ZZ)) % p
    aZZ = (a * ZZ) % p
    X3 = ((XX - aZZ)**2 - 2 * b * A * ZZ) % p
    Z3 = (A * (XX + aZZ) + 4 * b * (ZZ**2)) % p
    return (X3, Z3)

def diffadd(P, Q, x0):
    X1, Z1 = P
    X2, Z2 = Q
    X1Z2 = (X1 * Z2) % p
    X2Z1 = (X2 * Z1) % p
    Z1Z2 = (Z1 * Z2) % p
    T = ( (X1Z2 + X2Z1) * (X1 * X2 + a * Z1Z2) ) % p
    Z3 = ((X1Z2 - X2Z1)**2) % p
    X3 = (2 * T + 4 * b * (Z1Z2**2) - x0 * Z3) % p
    return (X3, Z3)

def ladder(s, x0):
    R0 = (x0, 1)
    R1 = dbl(R0)
    n = s.nbits()
    pbit = 0
    bit = 0  # Initialize bit to 0 to avoid UnboundLocalError
    for i in range(n - 2, -1, -1):
        bit = (s >> i) & 1
        pbit ^= bit
        if pbit:
            R0, R1 = R1, R0
        R1 = diffadd(R0, R1, x0)
        R0 = dbl(R0)
        pbit = bit
    # Final correction using the last bit
    if bit:
        R0 = R1
    if R0[1] == 0:
        return "Infinity"
    return R0[0] * inverse_mod(R0[1], p) % p


# ======= Function to compute the order of (x0,1) under the ladder =========
def get_order(x0, max_iter=1000000):
    # We compute k*P (with P = (x0,1)) until we get "Infinity"
    for k in range(1, max_iter):
        Q = ladder(Integer(k), x0)
        if Q == "Infinity":
            return k
    return None

# ======= Search for a candidate base point with smooth (small) order =======
def find_base_point(lower=2, upper=300):
    candidates = []
    for cand in range(lower, upper):
        r = get_order(cand)
        if r is None:
            continue
        fac = factor(r)
        # We want r to be smooth; here we require that all prime factors are small.
        if max([prime for prime,exp in fac]) < 1000:
            candidates.append( (cand, r, fac) )
    return candidates

print("[*] Searching for candidate base points with smooth orders...")
cand_list = find_base_point()
if len(cand_list) < 2:
    print("Not enough candidates found; try a wider search.")
    exit()
# For the attack we need two base points with coprime orders and such that r1*r2 > order_full.
# (Since the secret key is chosen as the minimum of priv and order-full minus priv, it is at most order_full/2.)
for i in range(len(cand_list)):
    for j in range(i+1, len(cand_list)):
        bp1, r1, fac1 = cand_list[i]
        bp2, r2, fac2 = cand_list[j]
        if gcd(r1, r2) == 1 and r1 * r2 > order_full:
            print(f"[*] Using base points: x0 = {bp1} (order {r1}) and x0 = {bp2} (order {r2})")
            goto = True
            break
    else:
        continue
    break
else:
    print("No two suitable base points found!")
    exit()

# ======= Function to compute discrete log by brute force in the small subgroup =======
def dlog(x0, order_val, target):
    # Since order_val is small, we precompute the table:
    table = {}
    for k in range(order_val):
        val = ladder(Integer(k), x0)
        table[val] = k
    if target not in table:
        print("Discrete log not found!")
        exit()
    return table[target]

# ======= Connect to remote challenge =======
print("[*] Connecting to challenge server...")
r = remote("socket.cryptohack.org", 13416)

def send_req(data):
    r.sendline(json.dumps(data).encode())
    return json.loads(r.recvline().strip().decode())

# Get public key for first base point bp1:
req1 = {"option": "get_pubkey", "x0": str(bp1)}
resp1 = send_req(req1)
pub1 = int(resp1["pubkey"])
print(f"[*] For base point x0={bp1}, server returned pubkey = {pub1}")

# Get public key for second base point bp2:
req2 = {"option": "get_pubkey", "x0": str(bp2)}
resp2 = send_req(req2)
pub2 = int(resp2["pubkey"])
print(f"[*] For base point x0={bp2}, server returned pubkey = {pub2}")

# ======= Solve discrete logs in each subgroup =======
print("[*] Solving discrete logs in the two subgroups...")
d1 = dlog(bp1, r1, pub1)
print(f"[*] Found d1 = {d1} mod {r1}")
d2 = dlog(bp2, r2, pub2)
print(f"[*] Found d2 = {d2} mod {r2}")

# ======= Recover full private key via CRT =======
privkey = crt([d1, d2], [r1, r2])
print(f"[*] Recovered private key: {privkey}")

# ======= Submit private key to get the flag =======
req3 = {"option": "get_flag", "privkey": str(privkey)}
r.sendline(json.dumps(req3).encode())
print("[*] Server reply:")
print(r.recvline().decode())
r.close()
