if __name__ == "__main__":
    # 1. Khởi tạo
    manager = FileManager()
    
    # 2. Tạo dữ liệu giả
    dummy_data = {
        "subjects": {"TEST01": {"name": "Môn Test Tiếng Việt"}},
        "edges": [["TEST01", "TEST02"]]
    }
    
    # 3. Ghi thử
    print("Đang ghi dữ liệu...")
    manager.save_data(dummy_data)
    
    # 4. Đọc lại
    print("Đang đọc lại...")
    loaded_data = manager.load_data()
    print("Kết quả đọc được:", loaded_data)
    
    # 5. Kiểm tra file trên ổ cứng
    if os.path.exists(DATA_FILE):
        print("✅ Kiểm tra thành công! File JSON đã được tạo.")
    else:
        print("❌ Lỗi: File chưa được tạo.")

