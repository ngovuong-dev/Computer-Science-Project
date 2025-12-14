# 🎓 STU Roadmap Manager - Tarjan Core

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Algorithm](https://img.shields.io/badge/Algorithm-Tarjan-red)

**STU Roadmap Manager** là ứng dụng hỗ trợ xây dựng lộ trình môn học và kiểm tra tính logic của chương trình đào tạo. Ứng dụng tập trung vào việc phát hiện lỗi vòng lặp (cycle) - nguyên nhân khiến sinh viên không thể tốt nghiệp - bằng thuật toán **Tarjan**.

---

## 🚀 Tính năng chính

Ứng dụng cung cấp 3 chức năng cốt lõi để thao tác với đồ thị môn học:

### 1. Thêm Môn học (Add Subject)
* Cho phép nhập **Mã môn** và **Tên môn**.
* Thiết lập mối quan hệ tiên quyết (Môn A là điều kiện để học Môn B).
* Tự động vẽ node và mũi tên lên đồ thị ngay sau khi thêm.

### 2. Xóa Môn học (Delete Subject)
* Nhập mã môn cần xóa.
* Hệ thống sẽ xóa node đó và **tự động loại bỏ tất cả các liên kết** (mũi tên) đi vào hoặc đi ra từ node đó, đảm bảo đồ thị không bị lỗi.

### 3. Kiểm tra Logic (Run Tarjan)
* Kích hoạt thuật toán **Tarjan** để duyệt toàn bộ đồ thị.
* **Kết quả:**
    * Nếu lộ trình hợp lệ: Thông báo an toàn.
    * Nếu có vòng lặp (Ví dụ: A cần B, B cần A): Hệ thống sẽ **tô màu đỏ** các môn học gây lỗi để cảnh báo người dùng.

---

## 🛠️ Công nghệ sử dụng

* **Ngôn ngữ:** Python 3.x
* **Giao diện:** PyQt6
* **Xử lý đồ thị:** NetworkX (Cấu trúc dữ liệu), Matplotlib (Vẽ hình)
* **Thuật toán:** Tarjan's Algorithm (Tìm thành phần liên thông mạnh - SCC)

---

## ⚙️ Cài đặt và Chạy chương trình

### Bước 1: Cài đặt thư viện
Mở Terminal tại thư mục dự án và chạy lệnh:

```bash
pip install PyQt6 networkx matplotlib
