# =====================================================================
## Script: graph_canvas.py
## Path: src/ui/widgets/graph_canvas.py
## Description: Widget để hiển thị đồ thị môn học sử dụng Matplotlib và NetworkX.
# =====================================================================

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import networkx as nx

# Kế thừa từ FigureCanvasQTAgg 
class GraphCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None): # Hàm khởi tạo
        # Màu nền tối cho đồ thị (Dark Mode)
        plt.style.use('dark_background') 
        # Tạo Figure
        self.fig, self.ax = plt.subplots(figsize=(6, 6))        
        # Gọi constructor của lớp cha
        super().__init__(self.fig)
        # Gán parent widget (để nhúng vào giao diện PyQt)
        self.setParent(parent)

    def plot(self, subjects, edges, highlight_nodes=[]): # Vẽ đồ thị
        # Xóa hình cũ
        self.ax.clear()
        
        # Tạo đồ thị NetworkX
        G = nx.DiGraph()
        for s in subjects: 
            G.add_node(s)
        G.add_edges_from(edges)

        # Tính toán bố cục (Layout)
        try:
            # Layout kiểu lò xo (Spring) nhìn đẹp nhất
            pos = nx.spring_layout(G, k=0.9, seed=42)
        except:
            # Dự phòng nếu layout lỗi
            pos = nx.shell_layout(G)
            
        # Xác định màu sắc (Đỏ cho lỗi, Xanh cho bình thường)
        colors = []
        for n in G.nodes():
            if n in highlight_nodes:
                colors.append('#ff3333') # Đỏ
            else:
                colors.append('#00cc99') # Xanh ngọc

        # Vẽ đồ thị
        nx.draw(G, pos, ax=self.ax, 
                with_labels=True, 
                node_color=colors, 
                node_size=1800, 
                edge_color="#1A1A1A", 
                font_color='white', 
                font_weight='bold', 
                arrowsize=15, 
                width=1.5)
        
        # Cập nhật hiển thị
        self.draw()
    
    def zoom(self, factor):
        """
        Phóng to/Thu nhỏ bằng cách thay đổi giới hạn trục.
        factor < 1: Phóng to (Thu hẹp vùng nhìn)
        factor > 1: Thu nhỏ (Mở rộng vùng nhìn)
        """
        # 1. Lấy giới hạn trục hiện tại
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()

        # 2. Tính tâm của biểu đồ
        x_center = (xlim[0] + xlim[1]) / 2
        y_center = (ylim[0] + ylim[1]) / 2

        # 3. Tính chiều rộng/cao mới dựa trên hệ số zoom
        new_width = (xlim[1] - xlim[0]) * factor
        new_height = (ylim[1] - ylim[0]) * factor

        # 4. Cập nhật giới hạn trục mới (giữ nguyên tâm)
        self.ax.set_xlim(x_center - new_width / 2, x_center + new_width / 2)
        self.ax.set_ylim(y_center - new_height / 2, y_center + new_height / 2)

        # 5. Vẽ lại
        self.draw()