# 🗺️ Roadmap Manager - Tarjan Algorithm

![Python](https://img.shields.io/badge/Python-3.11-blue)
![GUI](https://img.shields.io/badge/GUI-PyQt6-green)

> **Roadmap Manager** là ứng dụng quản lý lộ trình học tập/dự án dựa trên đồ thị, sử dụng thuật toán Tarjan để phân tích sự phụ thuộc và phát hiện các vòng lặp trong lộ trình.

## 📖 Giới thiệu

Dự án này được xây dựng để giải quyết bài toán quản lý các môn học hoặc tác vụ có tính phụ thuộc lẫn nhau. Ứng dụng cho phép người dùng trực quan hóa lộ trình dưới dạng đồ thị có hướng và sử dụng thuật toán Tarjan để tìm ra các Thành phần Liên thông Mạnh.

Nếu một thành phần liên thông mạnh có nhiều hơn 1 đỉnh, điều đó báo hiệu một "vòng lặp chết" (Dead lock) trong lộ trình học tập (Ví dụ: Môn A cần Môn B, nhưng Môn B lại cần Môn C, Môn D lại cần môn A và B).

## 🏗️ Kiến trúc Hệ thống (MVC)

Dự án tuân thủ nghiêm ngặt mô hình thiết kế **Model - View - Controller**:

* **📂 Model:**
    * Xử lý logic nghiệp vụ: Thêm/Xóa node (môn học).
    * Thực thi thuật toán Tarjan để tính toán SCC.
    * `FileManager`: Module chịu trách nhiệm lưu trữ và đọc dữ liệu từ file (JSON).
* **💻 View:**
    * Giao diện người dùng xây dựng bằng `PyQt6`.
    * Hiển thị biểu đồ trực quan sử dụng `matplotlib` được nhúng vào PyQt.
    * Các nhập liệu và bảng hiển thị danh sách môn học.
* **🎮 Controller:**
    * Điều phối tương tác giữa View và Model.
    * Nhận tín hiệu từ nút bấm (Add, Connect, Analyze), gọi Model xử lý và cập nhật lại View.

## ✨ Tính năng Chính

1.  **Quản lý Môn học (Nodes):** Thêm mới, xóa môn học.
2.  **Quản lý Liên kết (Edges):** Tạo mối quan hệ tiên quyết giữa các môn học.
3.  **Trực quan hóa Đồ thị:** Vẽ đồ thị tự động với `matplotlib`, hiển thị rõ hướng mũi tên và trọng số (nếu có).
4.  **Phân tích Tarjan:**
    * Tự động chạy thuật toán Tarjan.
    * Tô màu nổi bật các nhóm SCC (Thành phần liên thông mạnh).
    * Cảnh báo nếu phát hiện vòng lặp luẩn quẩn trong lộ trình.
5.  **Lưu trữ Dữ liệu:** Lưu và tải lại lộ trình thông qua module `FileManager` và bằng file `Json`.
6. **Phóng to và thu nhỏ Đồ thị:** 2 nút tròn có nhiệm vụ phóng to thu nhỏ đồ thị để dễ xem hơn.

## 🧮 Thuật toán Tarjan (Pseudo-code)

Thuật toán sử dụng cơ chế **Duyệt chiều sâu (DFS)** kết hợp với **Ngăn xếp (Stack)** để tìm SCC với độ phức tạp thời gian O(|V| + |E|).

```text
ALGORITHM Tarjan
INPUT:  Đồ thị G = (Vertices V, Edges E)
OUTPUT: Danh sách các thành phần liên thông mạnh (Strongly Connected Components)

// Khởi tạo biến toàn cục với các giá trị mặc định
id_counter = 0
stack = Empty Stack
ids = Array of size |V| initialized to -1 (unvisited)
low = Array of size |V| initialized to 0
onStack = Array of size |V| initialized to False
scc_result = Empty List
// Chạy vòng lập các node trong đồ thị để đặt giá trị mặc định
For node in graph:
    ids = -1
    low = 0
    onStack = False

// Hàm duyệt theo chiều sâu (Depth First Search)
FUNCTION TARJAN(at):
    stack.push(at)
    onStack[at] = True
    ids[at] = low[at] = id_counter
    id_counter = id_counter + 1

    // Duyệt qua các node kề (neighbors)
    FOR each node 'to' in Neighbors(at):
        IF 'to' not in self.ids THEN
            // Trường hợp 1: Node con chưa được khởi tạo
            ids = -1
            low = 0
            onStack = False
        ELSE IF ids[to] == -1 THEN
            // Trường hợp 2: Node con chưa được thăm
            DFS(to)
            low[at] = MIN(low[at], low[to])
        ELSE IF onStack[to] == True THEN
            // Trường hợp 2: Node con đang trong stack (Back Edge)
            // Đây là dấu hiệu của vòng lặp
            low[at] = MIN(low[at], ids[to])

    // Kiểm tra chốt của SCC (Root of SCC)
    IF ids[at] == low[at] THEN
        new_component = Empty List
        WHILE True THEN:
            node = stack.pop()
            onStack[node] = False
            ADD node TO new_component
            IF node == at THEN
                break
        ADD new_component TO scc_result
FUNCTION RUN():
    // Khởi chạy DFS từ mỗi node chưa được khám phá
    FOR node in list(graph.kes()) THEN
        // Nếu node chưa được khám phá, bắt đầu DFS từ đó
        TARJAN(node)
    RETURN scc_result
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
pip install -r requirments.txt
```

### Bước 2: Chạy chương trình python
Mở Terminal tại thư mục dự án và chạy lệnh:
```bash
python main.py