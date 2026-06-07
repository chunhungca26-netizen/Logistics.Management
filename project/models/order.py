import uuid
from datetime import datetime

class Order:
    """Lớp đại diện cho một đơn hàng giao vận"""
    def __init__(self, customer_name: str, distance: float, package_type: str):
        self.__order_id = str(uuid.uuid4())[:8].upper()
        self.__customer_name = customer_name
        self.__distance = distance
        self.__package_type = package_type
        self.__status = "Chờ xử lý"
        self.__assigned_driver_id = None
        self.__assigned_vehicle_id = None
        self.__total_fee = 0.0
        self.__created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    # --- GETTERS ---
    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def order_id(self, value):
        self.__order_id = value

    @property
    def customer_name(self):
        return self.__customer_name

    @property
    def distance(self):
        return self.__distance

    @property
    def package_type(self):
        return self.__package_type

    @property
    def status(self):
        return self.__status

    @property
    def assigned_driver_id(self):
        return self.__assigned_driver_id

    @property
    def assigned_vehicle_id(self):
        return self.__assigned_vehicle_id

    @property
    def total_fee(self):
        return self.__total_fee

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    # --- SETTERS ---
    @status.setter
    def status(self, value: str):
        self.__status = value

    @assigned_driver_id.setter
    def assigned_driver_id(self, driver_id: str):
        self.__assigned_driver_id = driver_id

    @assigned_vehicle_id.setter
    def assigned_vehicle_id(self, vehicle_id: str):
        self.__assigned_vehicle_id = vehicle_id

    @total_fee.setter
    def total_fee(self, fee: float):
        self.__total_fee = fee

    def __str__(self):
        return (f"[Đơn #{self.__order_id}] KH: {self.__customer_name} | "
                f"Loại: {self.__package_type} | "
                f"KC: {self.__distance} km | "
                f"Phí: {self.__total_fee:,.0f} VNĐ | "
                f"Trạng thái: {self.__status}")
