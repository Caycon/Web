# CHƯƠNG 1: TỔNG QUAN

## 1.1. LÝ DO CHỌN ĐỀ TÀI
- Hiện nay, với sự phát triển của giáo dục đại học và sự gia tăng nhanh chóng về số lượng sinh viên, việc quản lý thông tin sinh viên trở thành một thách thức lớn đối với các trường đại học. Các phương pháp quản lý truyền thống như sử dụng giấy tờ hoặc bảng tính Excel không còn phù hợp, vì:
	- Dễ xảy ra sai sót khi nhập liệu, thống kê hoặc tra cứu dữ liệu.
	- Khó khăn trong việc quản lý số lượng lớn sinh viên, lớp học và môn học.
	- Hạn chế khả năng tích hợp và mở rộng hệ thống.

- Một hệ thống quản lý sinh viên hiện đại có thể:
	- Đơn giản hóa quy trình quản lý thông tin.
	- Hỗ trợ tra cứu nhanh chóng, giảm thiểu sai sót.
	- Tăng cường khả năng phân tích và thống kê dữ liệu về tình hình học tập của sinh viên.
    - Tích hợp công nghệ thông tin vào quản lý giáo dục, góp phần hiện đại hóa nền giáo dục.

- Với những lý do trên, việc xây dựng một hệ thống quản lý sinh viên hiệu quả và dễ sử dụng là một nhu cầu cấp thiết và cũng là mục tiêu chính của đề tài này.

---

## 1.2. XÁC ĐỊNH ĐỀ TÀI

### 1.2.1. Tên đề tài
**Hệ thống quản lý sinh viên cấp đại học.**

### 1.2.2. Mục tiêu của đề tài
- Đề tài hướng đến các mục tiêu cụ thể sau:
	- Xây dựng một hệ thống quản lý toàn diện về thông tin sinh viên, lớp học, môn học và điểm số.
	- Hỗ trợ các chức năng thêm, sửa, xóa, tìm kiếm thông tin dễ dàng và chính xác.
	- Cung cấp báo cáo, thống kê về kết quả học tập và phân loại sinh viên.
	- Đảm bảo tính linh hoạt, dễ mở rộng và bảo mật thông tin.

### 1.2.3. Phạm vi hệ thống
- Hệ thống tập trung vào các chức năng chính:
1. **Quản lý sinh viên:** 
   - Lưu trữ thông tin cá nhân như mã sinh viên, họ tên, ngày sinh, giới tính, địa chỉ, số điện thoại.
2. **Quản lý lớp học:** 
   - Theo dõi thông tin lớp học, danh sách sinh viên thuộc từng lớp.
3. **Quản lý môn học:**
   - Quản lý danh sách các môn học, số tín chỉ, thông tin giảng viên phụ trách.
4. **Quản lý điểm số:**
   - Lưu trữ điểm số từng môn học, tính toán điểm trung bình, xếp loại học lực.

### 1.2.4. Phạm vi nghiên cứu
- Đề tài tập trung nghiên cứu và triển khai các nội dung sau:
	- Phân tích nghiệp vụ và thiết kế hệ thống quản lý sinh viên cấp đại học.
	- Ứng dụng phương pháp phân tích thiết kế hướng đối tượng (OOAD) với công cụ UML.
	- Sử dụng cơ sở dữ liệu MySQL để lưu trữ và quản lý thông tin.
	- Xây dựng giao diện thân thiện và dễ sử dụng cho người dùng.

---

## 1.3. CẤU TRÚC BÁO CÁO
- Báo cáo được chia thành các chương sau:
1. **Chương 1: Tổng quan**
   - Trình bày lý do chọn đề tài, mục tiêu, phạm vi nghiên cứu, và cấu trúc báo cáo.
2. **Chương 2: Kiến thức cơ sở**
   - Trình bày các lý thuyết liên quan đến cơ sở dữ liệu, phân tích thiết kế hệ thống và ngôn ngữ mô hình hóa UML.
3. **Chương 3: Nội dung thực hiện**
   - Mô tả chi tiết quá trình khảo sát, phân tích nghiệp vụ, thiết kế hệ thống và xây dựng phần mềm.
4. **Chương 4: Kết quả nghiên cứu, hướng phát triển và kết luận**
   - Tổng kết kết quả đạt được, đánh giá ưu nhược điểm và đề xuất cải tiến hệ thống trong tương lai.

---

## 1.4. PHƯƠNG PHÁP NGHIÊN CỨU
- Để thực hiện đề tài, các phương pháp nghiên cứu sau được áp dụng:

### 1.4.1. Phương pháp khảo sát thực tế
- Tìm hiểu thực trạng và các vấn đề trong quản lý sinh viên tại các trường đại học.
- Phân tích nhu cầu của người dùng như nhân viên quản lý, giảng viên và sinh viên.

### 1.4.2. Phương pháp phân tích hệ thống
- Ứng dụng phương pháp phân tích hướng đối tượng để xây dựng sơ đồ Use Case, Class Diagram, Sequence Diagram, và Activity Diagram.
- Phân tích quy trình quản lý sinh viên hiện tại và đề xuất các cải tiến.

### 1.4.3. Phương pháp thực nghiệm
- Lập trình và triển khai hệ thống trên nền tảng công nghệ phù hợp.
- Chạy thử nghiệm hệ thống với các tình huống thực tế để đánh giá hiệu quả.

### 1.4.4. Phương pháp tài liệu
- Nghiên cứu các tài liệu về cơ sở dữ liệu, ngôn ngữ lập trình và mô hình UML.
- Tìm hiểu các hệ thống quản lý sinh viên hiện có để rút ra bài học kinh nghiệm và ý tưởng cải tiến.

---
# CHƯƠNG 2: KIẾN THỨC CƠ SỞ

## 2.1. LÝ THUYẾT CƠ SỞ DỮ LIỆU

### 2.1.1. Định nghĩa
- Cơ sở dữ liệu (Database) là tập hợp có tổ chức các dữ liệu, được lưu trữ và quản lý để dễ dàng truy xuất, sửa đổi, phân tích và chia sẻ. Trong hệ thống quản lý, cơ sở dữ liệu là một thành phần cốt lõi giúp lưu trữ các thông tin liên quan một cách khoa học và logic.

### 2.1.2. Các thành phần chính
1. **Thực thể (Entity):**  
   Là đối tượng cụ thể hoặc trừu tượng mà ta cần lưu trữ thông tin. Ví dụ, trong hệ thống quản lý sinh viên, các thực thể bao gồm Sinh viên, Lớp học, Môn học, Điểm.
   
2. **Thuộc tính (Attribute):**  
   Là các đặc điểm hoặc thông tin cụ thể của thực thể. Ví dụ, thuộc tính của thực thể Sinh viên có thể là họ tên, mã sinh viên, ngày sinh, và giới tính.
   
3. **Mối quan hệ (Relationship):**  
   Là sự liên kết giữa các thực thể. Ví dụ, mỗi sinh viên sẽ thuộc một lớp học và học nhiều môn học.

### 2.1.3. Ưu điểm của cơ sở dữ liệu
- **Giảm trùng lặp thông tin:** Dữ liệu được tổ chức logic, tránh dư thừa.
- **Đảm bảo toàn vẹn dữ liệu:** Các quy tắc ràng buộc giúp dữ liệu luôn chính xác và hợp lệ.
- **Dễ dàng truy xuất:** Cơ sở dữ liệu cung cấp công cụ tìm kiếm, truy vấn nhanh chóng.
- **Tính bảo mật:** Có thể phân quyền người dùng và bảo vệ dữ liệu khỏi truy cập trái phép.

### 2.1.4. Nhược điểm của cơ sở dữ liệu
- **Phức tạp trong thiết kế:** Đòi hỏi kỹ năng chuyên sâu khi xây dựng mô hình cơ sở dữ liệu.
- **Chi phí đầu tư:** Cần các hệ quản trị cơ sở dữ liệu và phần cứng phù hợp.
- **Khả năng lỗi hệ thống:** Rủi ro mất mát dữ liệu khi gặp sự cố nếu không có sao lưu.

### 2.1.5. Phân loại cơ sở dữ liệu
1. **Cơ sở dữ liệu quan hệ (Relational Database):**  
   Lưu trữ dữ liệu dưới dạng bảng, mỗi bảng tương ứng với một thực thể. Ví dụ: MySQL, PostgreSQL.
2. **Cơ sở dữ liệu phi quan hệ (NoSQL):**  
   Dữ liệu được tổ chức theo dạng key-value, document, hoặc graph. Ví dụ: MongoDB, Firebase.
3. **Cơ sở dữ liệu phân tán:**  
   Dữ liệu được lưu trữ và xử lý trên nhiều máy chủ. Ví dụ: Apache Cassandra.
4. **Cơ sở dữ liệu nhúng:**  
   Được tích hợp trực tiếp vào ứng dụng. Ví dụ: SQLite.

---

## 2.2. HỆ QUẢN TRỊ CƠ SỞ DỮ LIỆU MYSQL

### 2.2.1. Giới thiệu
- MySQL là một hệ quản trị cơ sở dữ liệu mã nguồn mở, sử dụng mô hình quan hệ (RDBMS). Nó cho phép lưu trữ, truy vấn và quản lý dữ liệu một cách hiệu quả. MySQL là một trong những công cụ được sử dụng phổ biến nhất, đặc biệt trong các hệ thống web.

![image](https://hackmd.io/_uploads/H1PVjWoG1l.png)


### 2.2.2. Tính năng chính của MySQL
- **Hỗ trợ ngôn ngữ SQL:** Ngôn ngữ tiêu chuẩn để thao tác dữ liệu.
- **Tương thích đa nền tảng:** Hoạt động tốt trên Windows, Linux, macOS.
- **Bảo mật cao:** Hỗ trợ phân quyền người dùng, mã hóa dữ liệu.
- **Hiệu năng tốt:** Xử lý khối lượng dữ liệu lớn với tốc độ cao.

### 2.2.3. Ưu điểm của MySQL
- **Dễ sử dụng:** Giao diện thân thiện, cú pháp SQL đơn giản.
- **Hiệu suất cao:** Tối ưu hóa cho các ứng dụng web và dữ liệu lớn.
- **Miễn phí:** Phiên bản cộng đồng cung cấp đầy đủ tính năng cơ bản.

### 2.2.4. Nhược điểm của MySQL
- **Hạn chế tính năng cao cấp:** Không mạnh mẽ bằng Oracle hoặc SQL Server trong các tác vụ phức tạp.
- **Phụ thuộc vào cấu hình:** Bảo mật và hiệu năng phụ thuộc vào khả năng cấu hình của người dùng.

---

## 2.3. PHÂN TÍCH THIẾT KẾ HƯỚNG ĐỐI TƯỢNG – UML

### 2.3.1. Khái niệm OOAD
- Phân tích và thiết kế hướng đối tượng (Object-Oriented Analysis and Design - OOAD) là phương pháp tiếp cận sử dụng các đối tượng để phân tích và thiết kế hệ thống. OOAD giúp biểu diễn các thành phần hệ thống theo cách gần gũi với thế giới thực, dễ dàng quản lý và mở rộng.

### 2.3.2. Ngôn ngữ UML
- **UML (Unified Modeling Language)** là một ngôn ngữ mô hình hóa tiêu chuẩn, được sử dụng để trực quan hóa và tài liệu hóa các hệ thống phần mềm. UML cung cấp các sơ đồ giúp phân tích và thiết kế hệ thống dễ dàng hơn.

### 2.3.3. Các sơ đồ UML chính
1. **Use Case Diagram:**  
   - Biểu diễn các chức năng chính của hệ thống và mối quan hệ với người dùng.
   - Ví dụ: Chức năng "Quản lý sinh viên" bao gồm thêm, sửa, xóa sinh viên.
 
![image](https://hackmd.io/_uploads/ry3_sbofJe.png)


2. **Class Diagram:**  
   - Biểu diễn các lớp, thuộc tính, phương thức và mối quan hệ giữa các lớp.
   - Ví dụ: Lớp Sinh viên có các thuộc tính (họ tên, mã số) và phương thức (đăng ký môn học).

![image](https://hackmd.io/_uploads/SJ25i-jzkx.png)


3. **Sequence Diagram:**  
   - Minh họa trình tự các tương tác giữa các đối tượng trong một chức năng cụ thể.
   - Ví dụ: Quá trình đăng ký môn học của sinh viên.

![image](https://hackmd.io/_uploads/By42sWsfyg.png)


4. **Activity Diagram:**  
   - Biểu diễn các luồng hoạt động hoặc quy trình nghiệp vụ.
   - Ví dụ: Quy trình quản lý điểm thi.

![image](https://hackmd.io/_uploads/ByS0objzJx.png)


---

## 2.4. MỤC ĐÍCH VÀ YÊU CẦU PHÂN TÍCH HỆ THỐNG

### 2.4.1. Mục đích
- **Tăng hiệu quả quản lý:** Hệ thống giúp tối ưu hóa việc lưu trữ và xử lý dữ liệu sinh viên.
- **Đảm bảo tính logic và chính xác:** Dữ liệu được tổ chức chặt chẽ, tránh sai sót.
- **Hỗ trợ mở rộng và bảo trì:** Thiết kế hệ thống linh hoạt, dễ dàng nâng cấp trong tương lai.

### 2.4.2. Yêu cầu
1. **Tính chính xác:**  
   - Đảm bảo dữ liệu không trùng lặp, sai lệch.  
   - Xử lý chính xác các nghiệp vụ như thêm, sửa, xóa sinh viên.

2. **Tính thân thiện:**  
   - Giao diện trực quan, dễ sử dụng cho người quản trị và sinh viên.

3. **Tính bảo mật:**  
   - Phân quyền truy cập, đảm bảo dữ liệu an toàn khỏi truy cập trái phép.

4. **Tính hiệu quả:**  
   - Hệ thống có khả năng xử lý nhanh chóng với lượng lớn dữ liệu.

---
