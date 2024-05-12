# Sử dụng một image Python làm nền tảng
FROM python:3.9

# Thiết lập thư mục làm việc mặc định trong container
WORKDIR /app

# Sao chép file requirements.txt vào thư mục làm việc trong container
COPY module.txt .

# Cài đặt các dependencies từ file module.txt
RUN pip install --no-cache-dir -r module.txt

# Sao chép tất cả các file từ thư mục hiện tại trên máy host vào thư mục làm việc trong container
COPY . .

# Command mặc định khi container được chạy
CMD ["python", "fast.py"]
