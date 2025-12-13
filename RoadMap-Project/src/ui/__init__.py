# =====================================================================
## Script: __init__.py
## Path: src/ui/__init__.py
## Description: Khởi tạo package cho module giao diện người dùng.
# =====================================================================

# Import class chính từ file main_window.py
from .main_window import MainWindow

# Chỉ định những gì sẽ được export khi dùng "from src.ui import *"
__all__ = ['MainWindow']