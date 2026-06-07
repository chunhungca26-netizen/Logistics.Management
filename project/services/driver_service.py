import json
import os
from models.driver import Driver

class DriverService:
    def __init__(self, data_file="data/drivers.json"):
        self.data_file = data_file
        self.drivers = []
        self.load_from_json()

    # ----------------------------------------------------------------
    # CRUD
    # ----------------------------------------------------------------
    def add_driver(self, driver: Driver):
        self.drivers.append(driver)
        self.save_to_json()

    def get_all_drivers(self):
        return self.drivers

    def find_by_id(self, user_id: str):
        for d in self.drivers:
            if d.user_id.lower() == user_id.lower():
                return d
        return None

    def update_driver(self, user_id: str, new_name: str = None, new_phone: str = None, new_license: str = None):
        """Cập nhật thông tin tài xế"""
        d = self.find_by_id(user_id)
        if not d:
            return False
        try:
            if new_name:
                d.name = new_name
            if new_phone:
                d.phone = new_phone
            if new_license:
                d.license_number = new_license
            self.save_to_json()
            return True
        except Exception as e:
            print(f"  Lỗi cập nhật: {e}")
            return False

    def delete_driver(self, user_id: str):
        """Xóa tài xế theo ID"""
        d = self.find_by_id(user_id)
        if not d:
            return False
        self.drivers.remove(d)
        self.save_to_json()
        return True

    # ----------------------------------------------------------------
    # TÌM KIẾM & SẮP XẾP
    # ----------------------------------------------------------------
    def search_by_name(self, keyword: str):
        """Tìm tài xế theo tên (không phân biệt hoa thường)"""
        keyword = keyword.lower()
        return [d for d in self.drivers if keyword in d.name.lower()]

    def search_by_id(self, user_id: str):
        """Tìm chính xác theo ID"""
        return self.find_by_id(user_id)

    def sort_by_name(self, descending: bool = False):
        """Sắp xếp tài xế theo tên"""
        return sorted(self.drivers, key=lambda d: d.name.lower(), reverse=descending)

    def get_available_drivers(self):
        """Lọc ra danh sách tài xế đang rảnh"""
        return [d for d in self.drivers if d.is_available]

    # ----------------------------------------------------------------
    # FILE I/O (JSON)
    # ----------------------------------------------------------------
    def save_to_json(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        data_to_save = []
        for d in self.drivers:
            data_to_save.append({
                "user_id": d.user_id,
                "name": d.name,
                "phone": d.phone,
                "license_number": d.license_number,
                "is_available": d.is_available,
                "current_vehicle_id": d.current_vehicle_id
            })
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)

    def load_from_json(self):
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data_list = json.load(f)
                for item in data_list:
                    d = Driver(item["user_id"], item["name"], item["phone"], item["license_number"])
                    d.is_available = item["is_available"]
                    d.current_vehicle_id = item["current_vehicle_id"]
                    self.drivers.append(d)
        except Exception:
            self.drivers = []
