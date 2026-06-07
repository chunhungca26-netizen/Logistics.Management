from abc import ABC, abstractmethod

# =====================================================================
# TÍNH TRỪU TƯỢNG (ABSTRACTION) - Abstract Base Class
# =====================================================================
class Vehicle(ABC):
    def __init__(self, vehicle_id: str, brand: str, payload: float):
        # TÍNH ĐÓNG GÓI (ENCAPSULATION) - Thuộc tính Private
        self.__vehicle_id = vehicle_id
        self.__brand = brand
        self.__payload = payload

    @property
    def vehicle_id(self):
        return self.__vehicle_id

    @property
    def brand(self):
        return self.__brand

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, value):
        if value < 0:
            raise ValueError("Tải trọng không được phép nhỏ hơn 0!")
        self.__payload = value

    @abstractmethod
    def calculate_fee(self, distance: float, package_type: str) -> float:
        pass

    @abstractmethod
    def get_type_name(self) -> str:
        pass


# =====================================================================
# TÍNH KẾ THỪA (INHERITANCE) & ĐA HÌNH (POLYMORPHISM)
# =====================================================================

class Motorbike(Vehicle):
    """Xe máy: phù hợp hàng nhỏ, cước phí 5.000đ/km"""
    def __init__(self, vehicle_id: str, brand: str, payload: float):
        super().__init__(vehicle_id, brand, payload)

    def calculate_fee(self, distance: float, package_type: str) -> float:
        base_fee = distance * 5_000
        if package_type.lower() == "fragile":
            return base_fee + 10_000
        return base_fee

    def get_type_name(self) -> str:
        return "Xe máy"


class LightTruck(Vehicle):
    """Xe tải nhẹ: phù hợp hàng cồng kềnh, cước phí 15.000đ/km"""
    def __init__(self, vehicle_id: str, brand: str, payload: float):
        super().__init__(vehicle_id, brand, payload)

    def calculate_fee(self, distance: float, package_type: str) -> float:
        base_fee = distance * 15_000
        if package_type.lower() == "bulky":
            return base_fee + 50_000
        return base_fee

    def get_type_name(self) -> str:
        return "Xe tải nhẹ"


class RefrigeratedTruck(Vehicle):
    """Xe đông lạnh: phù hợp hàng cần bảo quản, cước phí 25.000đ/km"""
    def __init__(self, vehicle_id: str, brand: str, payload: float, temperature: float):
        super().__init__(vehicle_id, brand, payload)
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    def calculate_fee(self, distance: float, package_type: str) -> float:
        base_fee = distance * 25_000
        return base_fee + 100_000  # Phụ phí đông lạnh cố định

    def get_type_name(self) -> str:
        return "Xe đông lạnh"
