# =====================================================================
## Script: roadmap_controller.py
## Path: src/controllers/roadmap_controller.py
## Description: Lớp controller giao tiếp giữa UI và tầng lưu trữ/thuật toán.
# =====================================================================

import networkx as nx
from src.storage.file_manager import FileManager
from src.algorithms.tarjan_algorithm import TarjanAlgorithm

class RoadmapController:
    def __init__(self): # Hàm khởi tạo
        self.storage = FileManager()
        self.data = self.storage.load_data() # Format: {'subjects': {}, 'edges': [['A','B']]}

    def add_subject(self, code, name): # Thêm môn học
        code = code.upper().strip() # Chuẩn hoá mã môn học
        name = name.strip()
        # Kiểm tra đầu vào
        if not code or not name:
            return False, "Mã và tên môn học không được để trống!"

        self.data["subjects"][code] = {"name": name} # Thêm môn học vào dữ liệu
        self.storage.save_data(self.data) # Lưu dữ liệu lại
        return True, "Thêm môn học thành công"

    def delete_subject(self, code): # Xoá môn học
        code = code.upper().strip() # Chuẩn hoá mã môn học
        # Kiểm tra môn học có tồn tại không
        if code not in self.data["subjects"]:
            return False, "Môn học không tồn tại!"
        
        # Xóa môn trong danh sách subjects
        del self.data["subjects"][code]
        
        # Xóa tất cả các liên kết dính tới môn này (Cả đầu ra và đầu vào)
        # Lọc giữ lại những cạnh KHÔNG chứa code
        new_edges = [edge for edge in self.data["edges"] if code not in edge]
        self.data["edges"] = new_edges
        
        self.storage.save_data(self.data)
        return True, "Đã xóa môn {code} và các liên kết liên quan."

    def add_dependency(self, u, v): # Thêm liên kết phụ thuộc
        # Chuẩn hoá mã môn học
        u = u.upper().strip()
        v = v.upper().strip()

        # Không thêm nếu chưa có môn học
        if u not in self.data["subjects"] or v not in self.data["subjects"]:
            return False, "Vui lòng tạo môn học trước khi nối!"
        
        # Thêm liên kết nếu chưa tồn tại
        edge = [u, v]
        if edge not in self.data["edges"]:
            # Thêm liên kết và lưu dữ liệu lại
            self.data["edges"].append(edge)
            self.storage.save_data(self.data)
            return True, "Thêm thành công"
        return False, "Liên kết đã tồn tại"

    def delete_dependency(self, u, v): # Xoá liên kết phụ thuộc
        u, v = u.upper().strip(), v.upper().strip()
        edge = [u, v]
        if edge in self.data["edges"]:
            self.data["edges"].remove(edge)
            self.storage.save_data(self.data)
            return True, f"Đã gỡ bỏ liên kết {u} -> {v}"
        return False, "Liên kết không tồn tại."

    def get_graph_data(self): # Lấy dữ liệu đồ thị
        return self.data

    def run_tarjan_algorithm(self): # Chạy thuật toán kiểm tra vòng lặp
        # Chuyển đổi dữ liệu sang format danh sách kề cho Tarjan
        adj_list = {code: [] for code in self.data["subjects"]} # Khởi tạo danh sách kề 
        for u, v in self.data["edges"]: # Thêm cạnh vào danh sách kề 
            if u in adj_list: 
                adj_list[u].append(v)
            else: 
                adj_list[u] = [v]
        
        # Khởi tạo và chạy Tarjan
        solver = TarjanAlgorithm(adj_list)
        sccs = solver.run()

        # Phân loại kết quả
        # Nhóm nào > 1 phần tử là BAD (Cycle), = 1 là GOOD.
        cycles = [group for group in sccs if len(group) > 1]
        safe_nodes = [group[0] for group in sccs if len(group) == 1]

        return cycles, safe_nodes
    
    def clear_data(self): # Xoá toàn bộ dữ liệu
        self.data = {"subjects": {}, "edges": []}
        self.storage.save_data(self.data)