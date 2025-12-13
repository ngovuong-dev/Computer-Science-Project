# =====================================================================
## Script: file_manager.py
## Path: src/storage/file_manager.py
## Description: Quản lý việc đọc và ghi dữ liệu roadmap vào file JSON.
# =====================================================================

import json
import os

DATA_FILE = "data/roadmap.json"

class FileManager:
    def __init__(self): # Hàm khởi tạo
        self._ensure_file_exists()

    def _ensure_file_exists(self): # Đảm bảo file dữ liệu tồn tại
        if not os.path.exists("data"): # Tạo thư mục data nếu chưa có
            os.makedirs("data")
        if not os.path.exists(DATA_FILE): # Tạo file JSON nếu chưa có
            # Cấu trúc mặc định
            default_data = {"subjects": {}, "edges": []} # Định nghĩa cấu trúc dữ liệu
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(default_data, f)

    def load_data(self): # Đọc dữ liệu từ file JSON
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Lỗi đọc file: {e}")
            return {"subjects": {}, "edges": []}

    def save_data(self, data): # Ghi dữ liệu vào file JSON
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Lỗi ghi file: {e}")