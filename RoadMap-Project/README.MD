# 🗺️ Roadmap Manager - Tarjan Algorithm Visualizer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![GUI](https://img.shields.io/badge/GUI-PyQt6-green)
![Graph](https://img.shields.io/badge/Analysis-NetworkX-orange)
![Structure](https://img.shields.io/badge/Architecture-MVC-red)

> **Roadmap Manager** là ứng dụng quản lý lộ trình học tập/dự án dựa trên đồ thị, sử dụng thuật toán Tarjan để phân tích sự phụ thuộc và phát hiện các vòng lặp (circular dependencies) trong lộ trình.

## 📖 Giới thiệu

Dự án này được xây dựng để giải quyết bài toán quản lý các môn học hoặc tác vụ có tính phụ thuộc lẫn nhau (Pre-requisites). Ứng dụng cho phép người dùng trực quan hóa lộ trình dưới dạng đồ thị có hướng (Directed Graph) và sử dụng thuật toán Tarjan để tìm ra các Thành phần Liên thông Mạnh (Strongly Connected Components - SCC).

Nếu một SCC có nhiều hơn 1 đỉnh, điều đó báo hiệu một "vòng lặp chết" (deadlock) trong lộ trình học tập (Ví dụ: Môn A cần Môn B, nhưng Môn B lại cần Môn A).

## 🏗️ Kiến trúc Hệ thống (MVC Pattern)

Dự án tuân thủ nghiêm ngặt mô hình thiết kế **Model - View - Controller**:

* **📂 Model:**
    * Quản lý dữ liệu đồ thị sử dụng thư viện `networkx`.
    * Xử lý logic nghiệp vụ: Thêm/Sửa/Xóa node (môn học), edge (liên kết).
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
algorithm Tarjan_SCC(Graph G):
    Input: Đồ thị G = (V, E)
    Output: Tập hợp các SCC

    index = 0
    stack = []
    indices = {}  # Lưu chỉ số index của mỗi node
    lowlink = {}  # Lưu chỉ số thấp nhất có thể truy cập
    onStack = {}  # Kiểm tra node có trong stack không
    SCCs = []

    function strongconnect(v):
        indices[v] = index
        lowlink[v] = index
        index = index + 1
        stack.push(v)
        onStack[v] = true

        for (v, w) in E:
            if w is not visited:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            else if w in stack:
                lowlink[v] = min(lowlink[v], indices[w])

        # Nếu v là nút gốc của một SCC
        if lowlink[v] == indices[v]:
            new_scc = []
            repeat:
                w = stack.pop()
                onStack[w] = false
                new_scc.add(w)
            until w == v
            SCCs.add(new_scc)

    for v in V:
        if v is not visited:
            strongconnect(v)
    
    return SCCs