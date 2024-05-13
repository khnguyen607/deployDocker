# Sử dụng một image Python làm nền tảng
FROM python:3.9

# Thiết lập thư mục làm việc mặc định trong container
WORKDIR /app

# Sao chép file requirements.txt vào thư mục làm việc trong container
COPY module.txt .

# Cài đặt các dependencies từ file module.txt
RUN pip install --no-cache-dir -r module.txt

# Cài đặt Chrome
RUN apt-get update && apt-get install -y wget gnupg \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Cài đặt ChromeDriver
RUN CHROME_DRIVER_VERSION=`curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE` \
    && wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin \
    && rm /tmp/chromedriver.zip
    
# Sao chép tất cả các file từ thư mục hiện tại trên máy host vào thư mục làm việc trong container
COPY . .

# Command mặc định khi container được chạy
CMD ["python", "fast.py"]
