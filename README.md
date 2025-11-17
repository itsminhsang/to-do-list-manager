📝 To-Do List Manager

Thông tin đồ án

Môn học:*Lập trình Python Nâng cao

Sinh viên thực hiện:
- Lại Trần Minh Sang
- Phạm Phú Sơn

Chủ đề: Ứng dụng quản lý công việc (To-Do List) sử dụng Python Flask

---

🎯 Mô tả dự án

To-Do List Manager là ứng dụng web giúp người dùng quản lý công việc hàng ngày một cách hiệu quả. Ứng dụng được xây dựng bằng Python Flask với giao diện đẹp mắt, dễ sử dụng và đầy đủ tính năng.

✨ Tính năng chính

1. Quản lý công việc
- ✅ Thêm công việc mới với tiêu đề, mô tả chi tiết
- ✏️ Chỉnh sửa thông tin công việc
- 🗑️ Xóa công việc
- ☑️ Đánh dấu hoàn thành/chưa hoàn thành
- 🔍 Tìm kiếm công việc theo từ khóa

2. Phân loại và ưu tiên
- 📁 Tạo và quản lý danh mục công việc
- 🎨 Tùy chỉnh màu sắc cho từng danh mục
- 🔴🟡🟢 Phân loại độ ưu tiên (Cao, Trung bình, Thấp)
- ⏰ Thiết lập hạn hoàn thành

3. Lọc và thống kê
- 📊 Thống kê tổng quan (tổng số, đang làm, hoàn thành, tiến độ)
- 🔽 Lọc theo trạng thái (tất cả, đang thực hiện, đã hoàn thành)
- 📂 Lọc theo danh mục
- 📈 Thanh tiến độ trực quan

4. Giao diện người dùng
- 🎨 Thiết kế hiện đại với gradient màu đẹp mắt
- 📱 Responsive, tương thích đa thiết bị
- ⚡ Hiệu ứng chuyển động mượt mà
- 🔔 Thông báo flash messages thân thiện
- 🌈 Color picker cho danh mục

🛠️ Công nghệ sử dụng

Backend
- Python 3.8+: Ngôn ngữ lập trình chính
- Flask 3.0.0: Web framework
- Flask-SQLAlchemy: ORM để quản lý database
- SQLite: Database nhẹ, dễ triển khai

Frontend
- HTML5: Cấu trúc trang web
- CSS3: Styling với gradient, animation, flexbox, grid
- JavaScript: Tương tác người dùng
- Font: Times New Roman, size 13px

Widgets đã sử dụng
- Label: Hiển thị text, tiêu đề
- Frame/Container: Bố cục trang web
- Button: Các nút thao tác
- Textbox/Input: Nhập liệu text
- Textarea: Nhập mô tả dài
- Combobox/Select: Chọn danh mục, độ ưu tiên
- Checkbox: Đánh dấu hoàn thành
- Date picker: Chọn hạn hoàn thành
- Color picker: Chọn màu danh mục
- Progress bar: Thanh tiến độ
- Message boxes: Flash messages
- Search box: Tìm kiếm

📁 Cấu trúc thư mục

```
todo-list-manager/
│
├── app.py                 # File chính chạy ứng dụng
├── requirements.txt       # Danh sách thư viện cần cài đặt
├── README.md             # File hướng dẫn này
│
├── templates/            # Thư mục chứa HTML templates
│   ├── base.html        # Template gốc
│   ├── index.html       # Trang chủ
│   ├── edit.html        # Trang chỉnh sửa
│   └── categories.html  # Trang quản lý danh mục
│
├── static/              # Thư mục chứa file tĩnh (tạo thêm nếu cần)
│   └── favicon.ico     # Icon trang web
│
└── instance/            # Database (tự động tạo)
    └── todo.db         # SQLite database
```

🚀 Hướng dẫn cài đặt và chạy

1. Yêu cầu hệ thống
- Python 3.8 trở lên
- pip (Python package manager)

2. Cài đặt

Bước 1: Clone hoặc tải project về máy

Bước 2: Mở terminal/cmd tại thư mục project

Bước 3: Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```

3. Chạy ứng dụng

```bash
python app.py
```

4. Truy cập ứng dụng

Mở trình duyệt và truy cập: http://localhost:5000

📖 Hướng dẫn sử dụng

Thêm công việc mới
1. Nhập tiêu đề công việc (bắt buộc)
2. Nhập mô tả chi tiết (tùy chọn)
3. Chọn độ ưu tiên
4. Chọn danh mục
5. Chọn hạn hoàn thành
6. Click "Thêm công việc"

Quản lý công việc
- Hoàn thành: Click vào checkbox bên trái tiêu đề
- Chỉnh sửa: Click nút "✏️ Sửa"
- Xóa: Click nút "🗑️ Xóa" và xác nhận

Lọc và tìm kiếm
- Sử dụng các nút lọc: Tất cả, Đang thực hiện, Đã hoàn thành
- Lọc theo danh mục bằng cách click vào tên danh mục
- Tìm kiếm bằng ô search ở góc trên

Quản lý danh mục
1. Click vào "📁 Danh mục" trên thanh menu
2. Nhập tên danh mục và chọn màu sắc
3. Click "Thêm" để tạo danh mục mới
4. Click "🗑️ Xóa" để xóa danh mục (lưu ý: sẽ xóa cả công việc trong danh mục)

💾 Database Schema

Bảng Category (Danh mục)
- `id`: Integer, Primary Key
- `name`: String(50), Tên danh mục
- `color`: String(7), Mã màu HEX
- `todos`: Relationship với bảng Todo

Bảng Todo (Công việc)
- `id`: Integer, Primary Key
- `title`: String(200), Tiêu đề công việc
- `description`: Text, Mô tả chi tiết
- `completed`: Boolean, Trạng thái hoàn thành
- `priority`: String(20), Độ ưu tiên (low/medium/high)
- `due_date`: DateTime, Hạn hoàn thành
- `created_at`: DateTime, Thời gian tạo
- `category_id`: Foreign Key → Category.id

🎨 Màu sắc và Layout

Bảng màu chính
- Primary Gradient: #667eea → #764ba2
- Background: White (#ffffff)
- Secondary: #f8f9fa
- Border: #e9ecef
- Text: #333333
- Success: #28a745
- Error: #dc3545

Font
- Font family: Times New Roman
- Font size: 13px (theo yêu cầu đồ án)

🔒 Bảo mật

- Secret key cho Flask session
- CSRF protection (có thể mở rộng)
- Input validation
- SQL injection protection (SQLAlchemy ORM)

🚧 Tính năng có thể mở rộng

- [ ] Đăng nhập/đăng ký người dùng
- [ ] Chia sẻ công việc giữa nhiều người
- [ ] Thông báo qua email
- [ ] Export công việc ra file PDF/Excel
- [ ] Theme tối/sáng
- [ ] Drag & drop để sắp xếp
- [ ] Sub-tasks (công việc con)
- [ ] Lịch calendar view
- [ ] Mobile app

📝 Ghi chú

- Database SQLite được lưu tại `instance/todo.db`
- Ứng dụng chạy ở chế độ debug (development)
- Port mặc định: 5000

👥 Tác giả

- Lại Trần Minh Sang
- Phạm Phú Sơn

---

📞 Liên hệ

Nếu có bất kỳ thắc mắc nào về dự án, vui lòng liên hệ qua email hoặc tạo issue trên repository.

---

© 2025 - To-Do List Manager | Đồ án môn Lập trình Python Nâng cao**
