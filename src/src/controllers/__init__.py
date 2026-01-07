# =====================================================================
## Script: __init__.py
## Path: src/controllers/__init__.py
## Description: Khởi tạo package cho module controllers.
# =====================================================================

# Import class chính từ file roadmap_controller.py
from .roadmap_controller import RoadmapController

# Chỉ định những gì sẽ được export khi dùng "from src.controllers import *"
__all__ = ['RoadmapController']