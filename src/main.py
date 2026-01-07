# =====================================================================
## Script: main.py
## Path: src/main.py
## Description: Script chính để khởi chạy ứng dụng giao diện người dùng.
# =====================================================================

# Import các module hệ thống
import sys
import os

# Thêm đường dẫn gốc vào hệ thống để Python tìm thấy thư mục 'src'
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import các module cần thiết từ PyQt6 và module giao diện chính
from PyQt6.QtWidgets import QApplication
from src.ui.main_window import MainWindow

if __name__ == "__main__":
    # Khởi tạo ứng dụng PyQt
    app = QApplication(sys.argv)
    
    # 4. Hiển thị cửa sổ chính
    window = MainWindow()
    window.show()
    
    # 5. Vòng lặp sự kiện
    sys.exit(app.exec())