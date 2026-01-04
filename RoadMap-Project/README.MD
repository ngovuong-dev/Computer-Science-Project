# 🗺️ Roadmap Manager - Tarjan Algorithm

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![GUI](https://img.shields.io/badge/GUI-PyQt6-green)
![Graph](https://img.shields.io/badge/Analysis-NetworkX-orange)
![Structure](https://img.shields.io/badge/Architecture-MVC-red)

> **Roadmap Manager** là ứng dụng quản lý lộ trình học tập/dự án dựa trên đồ thị, sử dụng thuật toán Tarjan để phân tích sự phụ thuộc và phát hiện các vòng lặp trong lộ trình.

## 📖 Giới thiệu

Dự án này được xây dựng để giải quyết bài toán quản lý các môn học hoặc tác vụ có tính phụ thuộc lẫn nhau. Ứng dụng cho phép người dùng trực quan hóa lộ trình dưới dạng đồ thị có hướng và sử dụng thuật toán Tarjan để tìm ra các Thành phần Liên thông Mạnh.

Nếu một SCC có nhiều hơn 1 đỉnh, điều đó báo hiệu một "vòng lặp chết" trong lộ trình học tập (Ví dụ: Môn A cần Môn B, nhưng Môn B lại cần Môn A).

## 🏗️ Kiến trúc Hệ thống (MVC)

Dự án tuân thủ nghiêm ngặt mô hình thiết kế **Model - View - Controller**:

* **📂 Model:**
    * Xử lý logic nghiệp vụ: Thêm/Xóa node (môn học).
    * Thực thi thuật toán Tarjan để tính toán SCC.
    * `FileManager`: Module chịu trách nhiệm lưu trữ và đọc dữ liệu từ file (JSON/CSV).
* **💻 View:**
    * Giao diện người dùng xây dựng bằng `PyQt6`.
    * Hiển thị biểu đồ trực quan sử dụng `matplotlib` được nhúng vào PyQt.
    * Các dialog nhập liệu và bảng hiển thị danh sách môn học.
* **🎮 Controller:**
    * Điều phối tương tác giữa View và Model.
    * Nhận tín hiệu từ nút bấm (Add, Connect, Analyze), gọi Model xử lý và cập nhật lại View.

## ✨ Tính năng Chính

1.  **Quản lý Môn học (Nodes):** Thêm mới, chỉnh sửa tên, xóa môn học.
2.  **Quản lý Liên kết (Edges):** Tạo mối quan hệ tiên quyết (Prerequisite) giữa các môn học.
3.  **Trực quan hóa Đồ thị:** Vẽ đồ thị tự động với `matplotlib`, hiển thị rõ hướng mũi tên và trọng số (nếu có).
4.  **Phân tích Tarjan:**
    * Tự động chạy thuật toán Tarjan.
    * Tô màu nổi bật các nhóm SCC (Thành phần liên thông mạnh).
    * Cảnh báo nếu phát hiện vòng lặp luẩn quẩn trong lộ trình.
5.  **Lưu trữ Dữ liệu:** Lưu và tải lại lộ trình thông qua module `FileManager`.

## 🧮 Thuật toán Tarjan (Pseudo-code)

Thuật toán sử dụng cơ chế **Depth-First Search (DFS)** kết hợp với **Stack** để tìm SCC với độ phức tạp thời gian $O(|V| + |E|)$.

```text

```

## ⚙️ Cài đặt và Chạy chương trình

### Bước 1: Cài đặt thư viện python cần thiết để chạy chương trình
Mở Terminal tại thư mục dự án và chạy lệnh:
> Chương trình này được viết bằng ngôn ngữ python 3.11 nên sử dụng đúng phiên bản để tránh lỗi

```bash
pip install --upgrade pip
pip install PyQt6 networkx matplotlib
```
or
```bash
pip install --upgrade pip
pip install -r requiremts.txt
```

### Bước 2: Chạy chương trình
Mở Terminal tại thư mục dự án và chạy lệnh:
```bash
python3 main.py