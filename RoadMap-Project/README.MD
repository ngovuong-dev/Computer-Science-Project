**Roadmap Manager** là ứng dụng Desktop giúp quản lý chương trình đào tạo và lộ trình môn học cho sinh viên. Ứng dụng thuật toán **Tarjan** để tự động phát hiện các lỗi logic (phụ thuộc vòng) trong cấu trúc môn học tiên quyết.

## 🚀 Tính năng nổi bật

* **Quản lý Môn học:** Thêm, sửa danh sách môn học dễ dàng.
* **Thiết lập Tiên quyết:** Định nghĩa mối quan hệ "Học A xong mới được học B".
* **Trực quan hóa Đồ thị:** Vẽ sơ đồ lộ trình học tập tự động bằng `Matplotlib` & `NetworkX`.
* **Kiểm tra Logic (Core Feature):** Sử dụng **Thuật toán Tarjan** để tìm các thành phần liên thông mạnh (SCC).
    * ✅ Nếu SCC = 1 node: Lộ trình hợp lệ.
    * ❌ Nếu SCC > 1 node: Báo lỗi "Vòng lặp môn học" (Ví dụ: A cần B, B cần A).
* **Lưu trữ Bền vững:** Dữ liệu được lưu tự động dưới dạng JSON, không cần cài đặt SQL Server.
* **Giao diện Hiện đại:** Dark Mode phong cách, thân thiện người dùng.

## 🛠️ Công nghệ sử dụng

Dự án được xây dựng theo mô hình kiến trúc **MVC (Model-View-Controller)**:

* **Ngôn ngữ:** Python 3.11
* **Giao diện (View):** PyQt6 (Desktop GUI)
* **Đồ thị (View/Model):** NetworkX, Matplotlib
* **Thuật toán (Controller):** Tarjan's Algorithm (Tìm SCC)
* **Lưu trữ (Model):** JSON File System

## 📂 Cấu trúc dự án
roadmap-manager/
├── app/
│   ├── algorithms/       # Chứa thuật toán Tarjan thuần túy
│   ├── controllers/      # Điều phối logic giữa UI và Data
│   ├── storage/          # Quản lý Đọc/Ghi file JSON
│   └── ui/               # Giao diện người dùng (PyQt6)
├── data/                 # Thư mục chứa file roadmap.json
├── main.py               # File khởi chạy ứng dụng
└── requirements.txt      # Danh sách thư viện



RoadMap-Project/
├── data/
│   └── roadmap.json
├── src/
│   ├── algorithms/
│   │   ├── __init__.py
│   │   └── tarjan_algorithm.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── roadmap_controller.py
│   ├── storage/
│   │   ├── __init__.py
│   │   └── file_manager.py
│   └── ui/
│       ├── widgets/
│       │   ├── __init__.py
│       │   └── graph_canvas.py
│       ├── __init__.py
│       └── main_window.py
├── README.MD
├── main.py
└── requirements.txt