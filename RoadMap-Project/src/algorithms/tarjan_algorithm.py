# =====================================================================
## Script: tarjan_algorithm.py
## Path: src/algorithms/tarjan_algorithm.py
## Description: Triển khai thuật toán Tarjan để tìm thành phần liên thông mạnh (SCC) trong đồ thị hướng.
# =====================================================================

import sys

# Tăng giới hạn đệ quy cho đồ thị lớn
sys.setrecursionlimit(2000)

class TarjanAlgorithm:
    def __init__(self, graph_dict): # Hàm khởi tạo
        # Khởi tạo thuộc tính
        self.graph = graph_dict # Danh sách kề dưới dạng dictionary
        self.ids = {} # dictionary lưu id khám phá
        self.low = {} # dictionary lưu low-link values
        self.on_stack = {} # dictionary đánh dấu node trên stack
        self.stack = [] # stack để theo dõi các node trong quá trình DFS
        self.id_counter = 0 # Bộ đếm id khám phá
        self.sccs = [] # Kết quả: danh sách các SCC
        
        # Khởi tạo giá trị mặc định cho các node trong graph
        for node in self.graph:
            self.ids[node] = -1
            self.low[node] = 0
            self.on_stack[node] = False

    def dfs(self, at): # Hàm DFS theo Tarjan
        self.stack.append(at) # Đẩy node hiện tại vào stack
        self.on_stack[at] = True # Đánh dấu node đang trên stack
        # Gián đặt id và low-link value
        self.ids[at] = self.low[at] = self.id_counter
        self.id_counter += 1

        # Duyệt qua các node kề 

        for to in self.graph.get(at, []):
            # Xử lý trường hợp:
            # Nếu node con chưa được khởi tạo trong ids (có thể do dữ liệu không đồng bộ)
            if to not in self.ids:
                self.ids[to] = -1; self.low[to]=0; self.on_stack[to]=False
            
            # Trường hợp node con chưa được khám phá
            if self.ids[to] == -1:
                self.dfs(to) # Đệ quy DFS
                self.low[at] = min(self.low[at], self.low[to]) # Cập nhật low-link value
            
            # Trường hợp node con đã được khám phá và đang trên stack
            elif self.on_stack[to]:
                self.low[at] = min(self.low[at], self.ids[to]) # Cập nhật low-link value

        # Sau khi duyệt xong các con, kiểm tra nếu `at` là root của SCC
        if self.ids[at] == self.low[at]:
            current_scc = []
            while True:
                node = self.stack.pop()
                self.on_stack[node] = False # Đánh dấu node không còn trên stack
                current_scc.append(node) # Thêm node vào SCC hiện tại
                if node == at: # Nếu đã pop đến node gốc của SCC thì dừng
                    break 
            self.sccs.append(current_scc) # Thêm SCC tìm được vào kết quả

    def run(self): # Chạy thuật toán Tarjan
        # Khởi chạy DFS từ mỗi node chưa được khám phá
        for node in list(self.graph.keys()):
            # Nếu node chưa được khám phá, bắt đầu DFS từ đó
            if self.ids.get(node, -1) == -1:
                self.dfs(node)
        return self.sccs