import json
import os
from models.vehicle import Motorbike, LightTruck, RefrigeratedTruck

class VehicleService:
    def __init__(self, data_file="data/vehicles.json"):
        self.data_file = data_file
        self.vehicles = []
        self.load_from_json()

    # ----------------------------------------------------------------
    # CRUD
    # ----------------------------------------------------------------
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        self.save_to_json()

    def get_all_vehicles(self):
        return self.vehicles

    def find_by_id(self, vehicle_id: str):
        for v in self.vehicles:
            if v.vehicle_id.lower() == vehicle_id.lower():
                return v
        return None

    def update_vehicle(self, vehicle_id: str, new_brand: str = None, new_payload: float = None):
        """Cập nhật thông tin xe theo ID"""
        v = self.find_by_id(vehicle_id)
        if not v:
            return False
        try:
            if new_brand:
                # vehicle_id và brand dùng property, cần gán lại qua setter nếu có
                # Brand không có setter -> tạo object mới thay thế
                idx = self.vehicles.index(v)
                if isinstance(v, Motorbike):
                    new_v = Motorbike(v.vehicle_id, new_brand, new_payload if new_payload is not None else v.payload)
                elif isinstance(v, LightTruck):
                    new_v = LightTruck(v.vehicle_id, new_brand, new_payload if new_payload is not None else v.payload)
                elif isinstance(v, RefrigeratedTruck):
                    new_v = RefrigeratedTruck(v.vehicle_id, new_brand, new_payload if new_payload is not None else v.payload, v.temperature)
                self.vehicles[idx] = new_v
            elif new_payload is not None:
                v.payload = new_payload
            self.save_to_json()
            return True
        except Exception as e:
            print(f"  Lỗi cập nhật: {e}")
            return False

    def delete_vehicle(self, vehicle_id: str):
        """Xóa xe theo ID"""
        v = self.find_by_id(vehicle_id)
        if not v:
            return False
        self.vehicles.remove(v)
        self.save_to_json()
        return True

    # ----------------------------------------------------------------
    # TÌM KIẾM & SẮP XẾP
    # ----------------------------------------------------------------
    def search_by_brand(self, keyword: str):
        """Tìm xe theo hãng (không phân biệt hoa thường)"""
        keyword = keyword.lower()
        return [v for v in self.vehicles if keyword in v.brand.lower()]

    def sort_by_payload(self, descending: bool = True):
        """Sắp xếp xe theo tải trọng"""
        return sorted(self.vehicles, key=lambda v: v.payload, reverse=descending)

    def get_available_vehicles(self, package_type: str):
        """Lọc xe phù hợp với loại hàng"""
        result = []
        for v in self.vehicles:
            pt = package_type.lower()
            if pt == "fragile" and isinstance(v, Motorbike):
                result.append(v)
            elif pt == "bulky" and isinstance(v, LightTruck):
                result.append(v)
            elif pt == "cold" and isinstance(v, RefrigeratedTruck):
                result.append(v)
            elif pt == "normal":
                result.append(v)
        return result

    # ----------------------------------------------------------------
    # FILE I/O (JSON)
    # ----------------------------------------------------------------
    def save_to_json(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        data_to_save = []
        for v in self.vehicles:
            entry = {
                "type": type(v).__name__,
                "vehicle_id": v.vehicle_id,
                "brand": v.brand,
                "payload": v.payload,
            }
            if isinstance(v, RefrigeratedTruck):
                entry["temperature"] = v.temperature
            data_to_save.append(entry)
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)

    def load_from_json(self):
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data_list = json.load(f)
                for item in data_list:
                    t = item["type"]
                    if t == "Motorbike":
                        v = Motorbike(item["vehicle_id"], item["brand"], item["payload"])
                    elif t == "LightTruck":
                        v = LightTruck(item["vehicle_id"], item["brand"], item["payload"])
                    elif t == "RefrigeratedTruck":
                        v = RefrigeratedTruck(item["vehicle_id"], item["brand"], item["payload"], item["temperature"])
                    else:
                        continue
                    self.vehicles.append(v)
        except Exception:
            self.vehicles = []
