# -----------------------------------------------
# Dockerfile for Flask App (To-Do List Manager)
# -----------------------------------------------

# 1. Chọn image Python chính thức
FROM python:3.11-slim

# 2. Đặt thư mục làm việc trong container
WORKDIR /app

# 3. Sao chép toàn bộ project vào container
COPY . /app

# 4. Cài đặt các thư viện cần thiết
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. Khai báo port Flask sẽ chạy (5000)
EXPOSE 5000

# 6. Lệnh mặc định để chạy ứng dụng Flask
CMD ["python", "app.py"]
