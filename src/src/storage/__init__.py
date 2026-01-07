# =====================================================================
## Script: __init__.py
## Path: src/storage/__init__.py
## Description: Khởi tạo package cho module lưu trữ.
# =====================================================================

# Import class chính từ file file_manager.py
from .file_manager import FileManager

# Chỉ định những gì sẽ được export khi dùng "from src.storage import *"
__all__ = ['FileManager']