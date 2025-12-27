# 📚 Library Management System

### Nguyễn Thị Vân Anh, Cao Khánh Ly, Võ Ngọc Thảo Nguyên, Võ Thị Anh Thư , Nguyễn Khánh Sơn
#### Nhom12@gmail.com

---

## Abstract
Quản lý thư viện là một nhu cầu quan trọng trong các trường học, cơ quan nhà nước và tổ chức giáo dục.  
Hệ thống Quản lý Thư viện được xây dựng bằng **Django** và **Bootstrap**, nhằm số hóa toàn bộ quy trình quản lý sách, độc giả và hoạt động mượn/trả.  
Hệ thống cung cấp giao diện trực quan, dễ sử dụng, hỗ trợ lọc dữ liệu, thống kê trực quan và báo cáo chi tiết.  
Mục tiêu chính là nâng cao hiệu quả quản lý tri thức, giảm thiểu sai sót thủ công, tăng cường khả năng truy xuất thông tin nhanh chóng, và tạo ra một nền tảng có thể mở rộng cho nhiều loại thư viện khác nhau.

---

## Keywords
Library · Django · Bootstrap · Book Management · Borrow/Return · Statistics · Education · Digital Transformation

---

## Motivation
Trong bối cảnh chuyển đổi số, việc quản lý thư viện truyền thống gặp nhiều khó khăn:  
- Dữ liệu phân tán, khó tra cứu.  
- Quản lý thủ công dễ sai sót.  
- Thiếu công cụ thống kê và báo cáo.  

Hệ thống Quản lý Thư viện ra đời nhằm giải quyết các vấn đề trên, mang lại một giải pháp hiện đại, hiệu quả và dễ triển khai.

---

## Technologies Used
- **Python 3.13** – Ngôn ngữ lập trình chính.  
- **Django 4.2** – Framework backend mạnh mẽ, hỗ trợ ORM và quản lý dữ liệu.  
- **Bootstrap 5** – Thiết kế giao diện hiện đại, responsive.  
- **SQLite** – Cơ sở dữ liệu mặc định, dễ triển khai và quản lý.  
- **HTML, CSS, JavaScript** – Xây dựng giao diện và tương tác người dùng.  

---

## Framework
Hệ thống được thiết kế theo mô hình MVC (Model-View-Controller) của Django:  
- **Model**: Quản lý dữ liệu sách, độc giả, lượt mượn, tác giả, thể loại.  
- **View**: Xử lý logic hiển thị, lọc dữ liệu, thống kê.  
- **Template**: Giao diện người dùng với Bootstrap.  
![alt text](img/framework.png)
---

## Features
- 📘 **Quản lý Sách**: thêm, sửa, phân loại, tìm kiếm và quản lý kho sách.  
- 🧑‍🎓 **Quản lý Độc giả**: theo dõi thông tin độc giả, lịch sử mượn trả và trạng thái tài khoản.  
- 🔄 **Mượn / Trả**: quản lý quy trình mượn trả sách nhanh chóng, chính xác, có cảnh báo quá hạn.  
- ⚙️ **Quản lý dữ liệu phụ**: quản lý nhà xuất bản, thể loại, tác giả và các dữ liệu liên quan.  
- 📊 **Thống kê & Báo cáo**: trực quan hóa dữ liệu hoạt động thư viện, xuất báo cáo định kỳ.  
- 🌗 **Dark Mode**: hỗ trợ chế độ nền tối để tăng trải nghiệm người dùng.  

---

## Algorithm
Các thuật toán chính trong hệ thống:  
- **Tìm kiếm**: áp dụng `icontains` để tìm kiếm gần đúng.  
- **Thống kê**: tổng hợp dữ liệu từ các bảng, hiển thị bằng biểu đồ.  

---

## Overall Time Complexity
- **Lọc sách**: O(n) với n là số lượng sách.  
- **Tìm kiếm theo tác giả/thể loại**: O(log n) khi dùng indexing.  
- **Thống kê**: O(n) duyệt toàn bộ dữ liệu.  
- **Quản lý mượn/trả**: O(1) cho mỗi giao dịch, O(m) với m là số lượt mượn.  

## Installation 
1. Clone repo: ```bash git clone https://github.com/yourusername/library-management.git cd library-management
2. python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver
6. Truy cập tại: http://127.0.0.1:8000

## Usage
Vào trang chủ để xem giới thiệu hệ thống.

Truy cập Danh sách Sách để tìm kiếm và lọc sách theo tiêu chí.

Vào Quản lý Độc giả để theo dõi thông tin người dùng.

Vào Mượn/Trả để quản lý giao dịch mượn sách.

Sử dụng Thống kê để xem báo cáo trực quan.

## Result
Ảnh minh họa giao diện hệ thống:

![Trang chủ](img/home.png)
![Danh sách Sách](img/book_list.png)
![Quản lý Độc giả](img/borrower_list.png)
![Mượn/Trả](img/loan_list.png)
![Thống kê](img/tk.png)



