# Data Visualization Project

Dự án Python để trực quan hóa dữ liệu từ nhiều nguồn khác nhau: dữ liệu tự sinh, CSV, JSON và API.

## Yêu cầu hệ thống

- Python 3.6 trở lên
- Các thư viện Python cần thiết (xem phần Cài đặt)

## Cài đặt

### 1. Clone hoặc tải dự án về máy

```bash
cd Project_Py
```

### 2. Cài đặt các thư viện cần thiết

Cài đặt các thư viện Python cần thiết bằng pip:

```bash
pip install matplotlib requests
```

Hoặc nếu bạn muốn tạo file `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Cấu trúc dự án

```
Project_Py/
├── main.py              # File chính để chạy chương trình
├── data_generate.py     # Tạo và trực quan hóa dữ liệu Random Walk
├── data_csv.py          # Đọc và trực quan hóa dữ liệu từ file CSV
├── data_json.py         # Đọc và trực quan hóa dữ liệu từ file JSON
├── data_api.py          # Gọi API và trực quan hóa dữ liệu từ GitHub
├── data/                # Thư mục chứa dữ liệu
│   ├── weather.csv      # Dữ liệu thời tiết
│   └── earthquake.json  # Dữ liệu động đất
└── README.md            # File hướng dẫn này
```

## Cách chạy dự án

### Chạy chương trình chính

Mở terminal/command prompt và chạy lệnh:

```bash
python main.py
```

### Sử dụng chương trình

Sau khi chạy, bạn sẽ thấy menu với các tùy chọn:

```
=== DATA VISUALIZATION PROJECT ===
1. Generate Data (Random Walk)
2. Load CSV (Weather)
3. Load JSON (Earthquake)
4. Call API (GitHub Repos)
0. Exit
```

**Các tùy chọn:**

- **1**: Tạo dữ liệu Random Walk và hiển thị biểu đồ
- **2**: Đọc dữ liệu thời tiết từ file CSV và hiển thị biểu đồ
- **3**: Đọc dữ liệu động đất từ file JSON và hiển thị biểu đồ
- **4**: Gọi API GitHub để lấy thông tin repository và hiển thị biểu đồ
- **0**: Thoát chương trình

### Kết quả

Sau khi chọn một tùy chọn, chương trình sẽ:
- Xử lý dữ liệu
- Tạo biểu đồ trực quan hóa
- Lưu biểu đồ vào file PNG trong thư mục gốc:
  - `output_random_walk.png` - Biểu đồ Random Walk
  - `output_weather.png` - Biểu đồ thời tiết
  - `output_earthquake.png` - Biểu đồ động đất
  - `output_github_repos.png` - Biểu đồ GitHub repositories

## Chạy từng module riêng lẻ

Nếu bạn muốn chạy từng chức năng riêng lẻ:

```bash
# Tạo Random Walk
python -c "from data_generate import visualize_random_walk; visualize_random_walk()"

# Trực quan hóa dữ liệu CSV
python -c "from data_csv import visualize_csv_weather; visualize_csv_weather()"

# Trực quan hóa dữ liệu JSON
python -c "from data_json import visualize_earthquake; visualize_earthquake()"

# Trực quan hóa dữ liệu từ API
python -c "from data_api import visualize_github_repos; visualize_github_repos()"
```

## Lưu ý

- Đảm bảo file `data/weather.csv` và `data/earthquake.json` tồn tại trong thư mục dự án
- Khi chọn tùy chọn 4 (GitHub API), cần có kết nối internet
- Các file biểu đồ sẽ được lưu trong thư mục gốc của dự án

## Xử lý lỗi

Nếu gặp lỗi khi chạy:

1. **Lỗi import module**: Kiểm tra xem đã cài đặt đầy đủ các thư viện chưa
   ```bash
   pip install matplotlib requests
   ```

2. **Lỗi không tìm thấy file**: Đảm bảo các file trong thư mục `data/` tồn tại

3. **Lỗi kết nối API**: Kiểm tra kết nối internet khi sử dụng tính năng GitHub API

## Tác giả

Dự án Data Visualization với Python

## License

MIT License

