# Intro
- Hầu hết các ứng dụng web hiện đại đều sử dụng cấu trúc cơ sở dữ liệu tại back-end. Cơ sở dữ liệu như vậy được sử dụng để lưu trữ và truy xuất dữ liệu liên quan đến ứng dụng web, từ nội dung web thực tế đến thông tin và nội dung người dùng, v.v. Để làm cho các ứng dụng web trở nên năng động, ứng dụng web phải tương tác với cơ sở dữ liệu theo thời gian thực. Khi các yêu cầu HTTP(S) đến từ người dùng, phần phụ trợ của ứng dụng web sẽ đưa ra các truy vấn tới cơ sở dữ liệu để xây dựng phản hồi. Các truy vấn này có thể bao gồm thông tin từ yêu cầu HTTP(S) hoặc thông tin liên quan khác.

![image](https://github.com/user-attachments/assets/4dadba74-8cd0-4685-bc2b-7316ba52798b)

- Khi thông tin do người dùng cung cấp được sử dụng để xây dựng truy vấn tới cơ sở dữ liệu, người dùng có ý định không tốt có thể lừa truy vấn được sử dụng cho mục đích khác với mục đích của lập trình viên ban đầu, cung cấp cho người dùng quyền truy cập để truy vấn cơ sở dữ liệu bằng cách sử dụng một cuộc tấn công được gọi là **SQL injection** ( SQLi).

- **SQL injection** đề cập đến các cuộc tấn công chống lại cơ sở dữ liệu quan hệ như MySQL (việc injections vào cơ sở dữ liệu không quan hệ, chẳng hạn như MongoDB, là việc NoSQL injections).

## SQL Injection (SQLi)
- Injection vulnerabilities xảy ra khi dữ liệu đầu vào do người dùng kiểm soát không được xử lý đúng cách và trực tiếp được đưa vào mã nguồn hoặc truy vấn, dẫn đến việc thực thi mã không mong muốn hoặc truy cập dữ liệu trái phép.
- Có rất nhiều loại injection vulnerabilities như là:
    - HTTP injection.
    - Code injection
    - Command injection.
    - SQL injection.

### 1. HTTP Injection
- HTTP Injection xảy ra khi đầu vào không an toàn được nhúng vào tiêu đề hoặc nội dung HTTP. Lỗ hổng này cho phép ta sửa đổi cấu trúc HTTP để thực hiện các hành vi độc hại, như:

    - Biến đổi URL: Chèn thêm tham số vào URL để khai thác hoặc dò tìm thông tin.
    - Sửa đổi tiêu đề HTTP (HTTP Headers): Tấn công có thể chèn các trường không mong muốn trong tiêu đề, như Host, Referer, hoặc User-Agent.
- Ví dụ: Một ứng dụng sử dụng trực tiếp giá trị Host từ tiêu đề để xây dựng URL:

```python
url = f"http://{request.headers['Host']}/login"
```
- Ta có thể chèn mã độc vào tiêu đề Host để chuyển hướng người dùng tới một trang web lừa đảo.

### 2. Code Injection
- Code Injection xảy ra khi dữ liệu đầu vào không được xác thực được đưa trực tiếp vào mã thực thi (như Python, PHP, hoặc JavaScript), dẫn đến thực thi mã không mong muốn.

- Ta có thể thực thi mã trên máy chủ hoặc ứng dụng.

- Ví dụ: Trong PHP, đoạn mã sau dễ bị tấn công:

```php
eval("return " . $_GET['input'] . ";");
```

### 3. Command Injection
- Command Injection xảy ra khi dữ liệu không được kiểm soát được đưa vào các lệnh hệ điều hành (OS commands). Lỗ hổng này cho phép ta thực thi lệnh tùy ý trên hệ thống đích.

- Ta có thể chiếm quyền điều khiển máy chủ hoặc thực hiện các hành động độc hại như xóa dữ liệu, đánh cắp thông tin.

- Ví dụ
```python
os.system(f"ping {user_input}")
```
- Nếu user_input là 127.0.0.1 && rm -rf /, lệnh rm -rf / sẽ được thực thi, gây mất toàn bộ dữ liệu.

### 4. SQL Injection
- SQL Injection (SQLi) xảy ra khi đầu vào không an toàn được đưa trực tiếp vào truy vấn SQL. Điều này cho phép ta:

    - Lấy thông tin nhạy cảm từ cơ sở dữ liệu.
    - Chèn, sửa đổi, hoặc xóa dữ liệu.
    - Thậm chí có thể chiếm quyền điều khiển máy chủ.
- Ví dụ: Truy vấn SQL dễ bị tấn công:

```sql
SELECT * FROM users WHERE username = '$username' AND password = '$password';
```
- Nếu username là admin' --, truy vấn sẽ trở thành:
```sql
SELECT * FROM users WHERE username = 'admin' -- ' AND password = '';
```
- Để thực hiện SQL Injection (SQLi), ta cần chèn mã SQL độc hại vào đầu vào của người dùng, sau đó phá vỡ logic truy vấn ban đầu của ứng dụng web hoặc thêm một truy vấn hoàn toàn mới. Điều này đòi hỏi việc vượt qua giới hạn đầu vào dự kiến để mã SQL độc hại được thực thi thay vì chỉ xử lý như dữ liệu thông thường.

- Cách thức thực hiện:

    - Đầu tiên ta sẽ thoát khỏi giới hạn đầu vào:

        - Ta thường bắt đầu bằng cách chèn ký tự đặc biệt như dấu ngoặc đơn (') hoặc dấu ngoặc kép (") vào đầu vào để thoát khỏi chuỗi đầu vào ban đầu và đưa mã độc vào truy vấn SQL.
        - Ví dụ: Nếu ứng dụng mong đợi một tên người dùng, việc nhập ' OR '1'='1 có thể thay đổi logic của truy vấn SQL.
    - Thêm mã độc:

        - Sau khi thoát khỏi chuỗi đầu vào, ta có thể thêm một đoạn mã SQL để thực hiện hành vi mong muốn, chẳng hạn như:
        - Chồng truy vấn (stacked queries): Thực hiện nhiều truy vấn trong một lệnh, ví dụ: '; DROP TABLE users; --.
        - Truy vấn Union: Kết hợp kết quả từ truy vấn của ứng dụng với kết quả từ truy vấn do ta đưa vào.
    - Truy xuất kết quả:

        - Để khai thác thành công, ta thường cần thấy đầu ra từ truy vấn, chẳng hạn như dữ liệu hiển thị trên giao diện web.
        - Nếu không có cách hiển thị trực tiếp, họ có thể cố gắng ghi kết quả ra file hoặc sử dụng các cách khác để kiểm tra.
- Ví dụ minh họa:
    - Giả sử một ứng dụng web thực hiện truy vấn SQL để kiểm tra tài khoản người dùng:

```sql
SELECT * FROM users WHERE username = '$username' AND password = '$password';
```
- Ta nhập vào:
```text
username: admin' --
password: (tùy ý).
```
- Truy vấn sẽ trở thành:

```sql
SELECT * FROM users WHERE username = 'admin' -- ' AND password = '';
```
- Dấu `--` làm mọi thứ sau nó bị bỏ qua, dẫn đến việc truy vấn chỉ kiểm tra tên người dùng admin, và bỏ qua kiểm tra mật khẩu.

## Databases
### Database Management Systems
- **Hệ thống quản lý cơ sở dữ liệu** hay **Database Management Systems** **(DBMS)** giúp tạo, xác định, lưu trữ và quản lý cơ sở dữ liệu. Nhiều loại **DBMS** khác nhau được thiết kế theo thời gian, chẳng hạn như DBMS dựa trên tệp, DBMS quan hệ (RDBMS), NoSQL, dựa trên đồ thị và lưu trữ Khóa/Giá trị.

- Có nhiều cách để tương tác với DBMS, chẳng hạn như các công cụ dòng lệnh, giao diện đồ họa hoặc thậm chí APIs (Application Programming Interfaces). DBMS được sử dụng trong các lĩnh vực ngân hàng, tài chính và giáo dục khác nhau để ghi lại lượng lớn dữ liệu. Một số tính năng cần thiết của DBMS bao gồm:

| Tính năng                  | Mô tả                                                                                                     |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| **Concurrency** (Tính đồng thời)            | Ứng dụng thực tế thường có nhiều người dùng tương tác cùng lúc. DBMS đảm bảo các tương tác này thành công mà không làm hỏng hoặc mất dữ liệu. |
| **Consistency** (Tính nhất quán)            | Với nhiều tương tác đồng thời, DBMS cần đảm bảo rằng dữ liệu vẫn nhất quán và hợp lệ trong toàn bộ cơ sở dữ liệu. |
| **Security**                   | DBMS cung cấp các cơ chế kiểm soát bảo mật chi tiết thông qua xác thực người dùng và phân quyền, ngăn chặn truy cập trái phép vào dữ liệu nhạy cảm. |
| **Reliability**                | Hệ thống cho phép sao lưu cơ sở dữ liệu dễ dàng và khôi phục lại trạng thái trước đó trong trường hợp mất dữ liệu hoặc bị xâm phạm. |
| **Structured Query Language** | SQL đơn giản hóa việc tương tác với cơ sở dữ liệu nhờ cú pháp trực quan, hỗ trợ nhiều thao tác khác nhau.                             |

![image](https://github.com/user-attachments/assets/ac74fee0-bc79-4ddd-8f64-038bf114e215)

- Trong hệ thống, **Tier I** thường là các ứng dụng phía người dùng như trang web hoặc các chương trình giao diện đồ họa (GUI). Đây là nơi diễn ra các thao tác trực tiếp với người dùng, chẳng hạn như đăng nhập hoặc bình luận. Dữ liệu từ các thao tác này được gửi đến **Tier II** thông qua các API hoặc các yêu cầu khác.

- **Tier II** là tầng trung gian (**middleware**), có nhiệm vụ xử lý các sự kiện nhận được và định dạng chúng sao cho phù hợp với hệ thống quản lý cơ sở dữ liệu (DBMS). Lớp ứng dụng trong tầng này sử dụng các thư viện và trình điều khiển (drivers) phù hợp với loại DBMS để thực hiện việc tương tác.

- Hệ thống quản lý cơ sở dữ liệu (DBMS) nhận các truy vấn từ tầng trung gian, thực hiện các tác vụ được yêu cầu như chèn, truy xuất, xóa hoặc cập nhật dữ liệu. Sau khi xử lý xong, DBMS trả về dữ liệu được yêu cầu hoặc mã lỗi nếu truy vấn không hợp lệ.

- Có thể đặt máy chủ ứng dụng (**application server**) và hệ thống DBMS trên cùng một máy. Tuy nhiên, đối với các cơ sở dữ liệu lớn hoặc có nhiều người dùng truy cập, việc tách chúng ra trên các máy chủ riêng biệt thường được ưu tiên để cải thiện hiệu suất và khả năng mở rộng.

## Types of Databases
### Relational Databases
- Cơ sở dữ liệu quan hệ (**Relational Database**) là một trong những loại cơ sở dữ liệu phổ biến nhất, sử dụng một **schema** (cấu trúc định sẵn) để xác định cách dữ liệu được tổ chức và lưu trữ.
- Với cơ sở dữ liệu này, các dữ liệu được tổ chức thành bảng (tables) giống như bảng trong Excel. Mỗi bảng lưu trữ một loại thông tin, và các bảng này liên kết với nhau thông qua khóa (keys).

### Non-relational Databases
- Cơ sở dữ liệu phi quan hệ (**Non-relational Databases**), hay còn gọi là NoSQL, không sử dụng các bảng, dòng, cột, hay các mối quan hệ chặt chẽ như cơ sở dữ liệu quan hệ. Thay vào đó, NoSQL lưu trữ dữ liệu theo nhiều mô hình linh hoạt, tùy thuộc vào loại dữ liệu. Điều này khiến NoSQL rất linh hoạt và dễ mở rộng, đặc biệt khi làm việc với dữ liệu không có cấu trúc rõ ràng.
- Do các đặc điểm trên nên ta sẽ dùng **NoSQL** khi:
    - Dữ liệu không có cấu trúc hoặc thay đổi thường xuyên (ví dụ: dữ liệu mạng xã hội, logs).
    - Cần mở rộng dễ dàng để hỗ trợ lượng dữ liệu lớn.
    - Không cần sự liên kết chặt chẽ giữa các phần dữ liệu.

- Một số mô hình lưu trữ phổ biến của NoSQL
    - **Key-Value:**

        - Lưu trữ dữ liệu dưới dạng cặp key-value (giống từ điển trong Python).
        -  Ví dụ:
        ```json
        {
          "100001": {
            "date": "01-01-2021",
            "content": "Welcome to this web application."
          },
          "100002": {
            "date": "02-01-2021",
            "content": "This is the first post on this web app."
          }
        }
        ```
        - **Key:** Mã định danh duy nhất (như "100001").
        - **Value:** Nội dung dữ liệu (có thể là chuỗi, từ điển, hoặc đối tượng phức tạp).
    - **Document-Based:**

        - Dữ liệu được lưu dưới dạng tài liệu (document), thường là JSON hoặc XML.
        - Mỗi document chứa tất cả thông tin liên quan trong một đối tượng.
    - **Wide-Column:**

        - Lưu dữ liệu dưới dạng bảng với các cột tùy biến.
        - Thích hợp cho các ứng dụng cần truy vấn nhanh với cấu trúc dữ liệu phức tạp.
    - **Graph:**

        - Lưu trữ dữ liệu dạng đồ thị, với các nút (nodes) và cạnh (edges).
        - Thích hợp cho dữ liệu có mối quan hệ phức tạp, như mạng xã hội hoặc bản đồ.
    
| Đặc điểm                | Cơ sở dữ liệu Quan hệ (Relational)                           | Cơ sở dữ liệu Phi Quan hệ (Non-relational)          |
|-------------------------|-------------------------------------------------------------|-----------------------------------------------------|
| **Cấu trúc dữ liệu**    | Dữ liệu được tổ chức trong bảng (tables) với hàng và cột.   | Dữ liệu không theo cấu trúc bảng, lưu dạng key-value, document, graph, hoặc wide-column. |
| **Schema**              | Có schema cố định, yêu cầu định nghĩa trước khi thêm dữ liệu. | Không yêu cầu schema cố định, linh hoạt hơn trong việc thay đổi cấu trúc dữ liệu. |
| **Quan hệ dữ liệu**      | Có mối quan hệ chặt chẽ giữa các bảng thông qua khóa (keys). | Không có hoặc rất ít quan hệ chặt chẽ giữa các phần dữ liệu. |
| **Ngôn ngữ truy vấn**    | Sử dụng SQL (Structured Query Language).                    | Không cần SQL, thường sử dụng API hoặc JSON/XML để truy vấn. |
| **Khả năng mở rộng**     | Mở rộng theo chiều dọc (nâng cấp máy chủ).                  | Mở rộng theo chiều ngang (thêm máy chủ mới).        |
| **Tốc độ xử lý**         | Thường chậm hơn khi xử lý dữ liệu lớn hoặc phi cấu trúc.    | Xử lý nhanh hơn, đặc biệt với dữ liệu lớn và phi cấu trúc. |
| **Dữ liệu phù hợp**      | Phù hợp với dữ liệu có cấu trúc và quan hệ rõ ràng.         | Thích hợp với dữ liệu phi cấu trúc hoặc thay đổi thường xuyên. |
| **Ứng dụng phổ biến**    | Hệ thống quản lý tài chính, ERP, CRM.                      | Big data, mạng xã hội, phân tích log, dữ liệu IoT.  |
| **Ví dụ**               | MySQL, PostgreSQL, Oracle, SQL Server.                     | MongoDB, Redis, Cassandra, Neo4j.                  |

## MySQL
- Structured Query Language (SQL) hay ngôn ngữ truy vấn có cấu trúc là một ngôn ngữ tiêu chuẩn được sử dụng để giao tiếp và quản lý dữ liệu trong hệ quản trị cơ sở dữ liệu quan hệ (**Relational Database Management System - RDBMS**). Nó cho phép người dùng thực hiện các thao tác trên cơ sở dữ liệu như truy vấn, thêm, sửa, xóa dữ liệu và quản lý cấu trúc cơ sở dữ liệu.
- Tuy nhiên tùy thuộc vào loại **RDBMS** mà **SQL syntax** có thể khác nhau giữa các **RDNMS**. Mặc dù khác nhau nhưng tất cả chúng đều phải tuân theo tiêu chuẩn **ISO** của SQL. Syntax MySQL/MariaDB cho các ví dụ được hiển thị. SQL có thể được sử dụng để thực hiện các hành động sau:
    - **Retrieve data**
    - **Update data**
    - **Delete data**
    - **Create new tables and databases**
    - **Add / remove users**
    - **Assign permissions to these users**
