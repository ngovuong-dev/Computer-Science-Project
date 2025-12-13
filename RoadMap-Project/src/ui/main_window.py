# =====================================================================
## Script: main_window.py
## Path: src/ui/main_window.py
## Description: Cửa sổ chính của ứng dụng quản lý lộ trình môn học với giao diện PyQt.
# =====================================================================

from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QMessageBox, 
                             QGroupBox, QTextEdit, QScrollArea)
from PyQt6.QtCore import Qt
from src.controllers.roadmap_controller import RoadmapController
from src.ui.widgets.graph_canvas import GraphCanvas

class MainWindow(QMainWindow):
    def __init__(self): # Hàm khởi tạo cửa sổ chính
        super().__init__()
        self.setWindowTitle("Roadmap Manager - Tarjan Algorithm")
        self.setGeometry(100, 100, 1200, 750)
        self.controller = RoadmapController()
        
        # --- BỐ CỤC CHÍNH ---
        main_widget = QWidget() # Trung tâm của cửa sổ
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        # --- PANEL TRÁI ---
        left_scroll = QScrollArea() # Thêm thanh cuộn đề phòng màn hình bé
        left_scroll.setWidgetResizable(True) # Cho phép thay đổi kích thước
        left_scroll.setFixedWidth(300) # Chiều rộng cố định cho panel trái
        
        left_panel = QWidget() # Panel bên trái
        left_panel.setStyleSheet("background-color: #1e1e1e; color: #e0e0e0;") # Style Dark Mode cho panel trái

        left_layout = QVBoxLayout(left_panel) # Bố cục dọc


        # 1. NHẬP DỮ LIỆU
        g_input = QGroupBox("1. Quản lý Dữ liệu") # Nhóm nhập dữ liệu
        l_input = QVBoxLayout() # Bố cục dọc cho nhóm
        
        # Thêm môn (Có tên môn để hiển thị)
        l_input.addWidget(QLabel("--- Thêm Môn Học ---"))
        self.in_code = QLineEdit(); self.in_code.setPlaceholderText("Mã môn")
        self.in_name = QLineEdit(); self.in_name.setPlaceholderText("Tên môn")
        btn_add = QPushButton("Lưu Môn Học") 
        btn_add.clicked.connect(self.add_node)
        l_input.addWidget(self.in_code) 
        l_input.addWidget(self.in_name)
        l_input.addWidget(btn_add)
        l_input.addSpacing(10)
        
        # Thêm cạnh
        l_input.addWidget(QLabel("--- Nối Môn Tiên Quyết ---"))
        self.in_u = QLineEdit(); self.in_u.setPlaceholderText("Môn học trước")
        self.in_v = QLineEdit(); self.in_v.setPlaceholderText("Môn học sau")
        btn_link = QPushButton("Thêm Liên Kết"); btn_link.clicked.connect(self.add_edge)
        l_input.addWidget(self.in_u)
        l_input.addWidget(self.in_v)
        l_input.addWidget(btn_link)
        g_input.setLayout(l_input)

        # 2. XÓA DỮ LIỆU
        g_del = QGroupBox("2. Xóa Dữ liệu")
        l_del = QVBoxLayout()
        self.in_del = QLineEdit(); self.in_del.setPlaceholderText("Nhập mã môn cần xóa")
        btn_del = QPushButton("Xóa Môn"); btn_del.clicked.connect(self.delete_node)
        btn_del.setStyleSheet("background-color: #552222; color: #ffcccc;") # Màu đỏ trầm
        l_del.addWidget(self.in_del); l_del.addWidget(btn_del)
        g_del.setLayout(l_del)

        # 3. KẾT QUẢ TARJAN
        g_tarjan = QGroupBox("3. Phân tích Tarjan (SCC)")
        l_tarjan = QVBoxLayout()
        
        self.txt_result = QTextEdit()
        self.txt_result.setReadOnly(True)
        # Style hiển thị
        self.txt_result.setStyleSheet("""
            background-color: #111; 
            color: #00ff00; 
            font-family: Consolas; 
            font-size: 13px;
            border: 1px solid #444;
        """)
        
        btn_run = QPushButton("🔍 CHẠY KIỂM TRA LOGIC")
        btn_run.setStyleSheet("background-color: #cc0000; color: white; font-weight: bold; padding: 10px; font-size: 14px;")
        btn_run.clicked.connect(self.run_tarjan)
        
        btn_reset = QPushButton("Reset Toàn bộ môn học"); btn_reset.clicked.connect(self.reset_app)

        l_tarjan.addWidget(btn_run)
        l_tarjan.addWidget(self.txt_result)
        l_tarjan.addWidget(btn_reset)
        g_tarjan.setLayout(l_tarjan)

        # Ráp các khối vào Panel trái
        left_layout.addWidget(g_input)
        left_layout.addWidget(g_del)
        left_layout.addWidget(g_tarjan)
        left_layout.addStretch() # Đẩy mọi thứ lên trên

        left_scroll.setWidget(left_panel)

        # --- PANEL PHẢI (GRAPH) ---
        self.canvas = GraphCanvas(self)

        main_layout.addWidget(left_scroll)
        main_layout.addWidget(self.canvas)

        # Nút Thu Nhỏ (-)
        self.btn_zoom_out = QPushButton("−", self) # Dấu trừ
        self.setup_floating_button(self.btn_zoom_out, "#444444")
        self.btn_zoom_out.clicked.connect(lambda: self.canvas.zoom(1.2)) # Factor > 1 là thu nhỏ
        # Nút Phóng To (+)
        self.btn_zoom_in = QPushButton("+", self) # Dấu cộng
        self.setup_floating_button(self.btn_zoom_in, "#444444")
        self.btn_zoom_in.clicked.connect(lambda: self.canvas.zoom(0.8)) # Factor < 1 là phóng to
        
        # Cập nhật đồ thị ban đầu
        self.refresh_graph()

    # --- LOGIC XỬ LÝ ---
    def add_node(self): # Thêm môn học
        code = self.in_code.text()
        name = self.in_name.text()
        ok, msg = self.controller.add_subject(code, name)
        if ok:
            self.in_code.clear(); self.in_name.clear()
            self.refresh_graph()
        else:
            QMessageBox.warning(self, "Lỗi", msg)

    def add_edge(self): # Thêm liên kết
        ok, msg = self.controller.add_dependency(self.in_u.text(), self.in_v.text())
        if ok:
            self.in_u.clear(); self.in_v.clear()
            self.refresh_graph()
        else:
            QMessageBox.warning(self, "Lỗi", msg)

    def delete_node(self): # Xóa môn học
        code = self.in_del.text()
        if not code: return

        # Xác nhận trước khi xóa
        reply = QMessageBox.question(self, 'Xác nhận', 
                                     f"Bạn có chắc muốn xóa môn {code}?\nMọi liên kết nối với nó cũng sẽ mất.",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            # Lưu ý: Cần đảm bảo Controller có hàm delete_subject như đã code trước đó
            try:
                ok, msg = self.controller.delete_subject(code)
                if ok:
                    self.in_del.clear()
                    self.refresh_graph()
                    QMessageBox.information(self, "Thành công", msg)
                else:
                    QMessageBox.warning(self, "Lỗi", msg)
            except AttributeError:
                QMessageBox.critical(self, "Lỗi Code", "Controller chưa có hàm delete_subject. Hãy cập nhật Controller!")

    def run_tarjan(self): # Chạy thuật toán Tarjan và hiển thị kết quả
        # 1. Chạy Tarjan
        cycles, safe_nodes = self.controller.run_tarjan_algorithm()
        
        # 2. Lấy dữ liệu tên môn học để hiển thị cho đẹp
        all_data = self.controller.get_graph_data()["subjects"]
        
        report = "=== KẾT QUẢ PHÂN TÍCH TARJAN ===\n\n"
        
        # Hiển thị Vòng lặp (Lỗi)
        if cycles:
            report += f"❌ CẢNH BÁO: PHÁT HIỆN {len(cycles)} VÒNG LẶP!\n"
            report += "Sinh viên sẽ bị kẹt, không thể tốt nghiệp.\n"
            report += "-" * 30 + "\n"
            
            for i, group in enumerate(cycles):
                report += f"🛑 NHÓM VÒNG LẶP #{i+1}:\n"
                for code in group:
                    # Lấy tên môn, nếu không có thì để N/A
                    name = all_data.get(code, {}).get("name", "N/A")
                    report += f"   • [{code}] - {name}\n"
                report += "\n"
        else:
            report += "✅ CHÚC MỪNG: LỘ TRÌNH HỢP LỆ.\n"
            report += "Không phát hiện phụ thuộc vòng.\n\n"
            
        report += "-" * 30 + "\n"
        
        # Hiển thị các môn an toàn
        if safe_nodes:
            report += f"ℹ️ Các môn an toàn ({len(safe_nodes)} môn):\n"
            for code in safe_nodes:
                name = all_data.get(code, {}).get("name", "N/A")
                report += f"   ✓ {code}: {name}\n"

        self.txt_result.setText(report)

        # 3. Highlight màu đỏ trên đồ thị
        nodes_in_cycle = []
        for group in cycles:
            nodes_in_cycle.extend(group)
            
        self.refresh_graph(highlight=nodes_in_cycle)
        
        if cycles:
            QMessageBox.critical(self, "Lỗi Logic", "Phát hiện vòng lặp môn học! Xem chi tiết ở khung kết quả.")

    # --- HÀM HỖ TRỢ SETUP STYLE CHO NÚT TRÒN ---
    def setup_floating_button(self, btn, bg_color):
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setFixedSize(50, 50)
        # Style bo tròn, viền trắng, đổ bóng nhẹ
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg_color}; 
                color: white; 
                font-size: 24px;
                border-radius: 25px; 
                border: 2px solid #555;
            }}
            QPushButton:hover {{ 
                background-color: #666666; 
                border-color: white;
            }}
            QPushButton:pressed {{
                background-color: #222;
            }}
        """)
    
    # === CẬP NHẬT VỊ TRÍ KHI KÉO DÃN CỬA SỔ ===
    def resizeEvent(self, event):
        # Lấy kích thước cửa sổ hiện tại
        w = self.width()
        h = self.height()
        
        # Khoảng cách từ lề phải
        margin_right = 70
        
        # 1. Nút Zoom Out
        self.btn_zoom_out.move(w - margin_right, h - 130) # 70 + 60
        
        # 2. Nút Zoom In
        self.btn_zoom_in.move(w - margin_right, h - 190)  # 130 + 60
        
        super().resizeEvent(event)

    def reset_app(self): # Reset toàn bộ dữ liệu
        confirm = QMessageBox.question(self, "Reset", "Xóa sạch dữ liệu làm lại từ đầu?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.Yes:
            self.controller.clear_data()
            self.txt_result.clear()
            self.refresh_graph()

    def refresh_graph(self, highlight=[]): # Cập nhật lại đồ thị
        d = self.controller.get_graph_data()
        self.canvas.plot(d["subjects"].keys(), d["edges"], highlight)