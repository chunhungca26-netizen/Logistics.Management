# =====================================================================
# TÍNH KẾ THỪA (INHERITANCE) & ĐÓNG GÓI (ENCAPSULATION) CHO TÀI XẾ
# =====================================================================

class User:
    """Lớp cơ sở chứa thông tin cơ bản của một người dùng"""
    def __init__(self, user_id: str, name: str, phone: str):
        self.__user_id = user_id
        self.__name = name
        self.__phone = phone

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Tên không được để trống!")
        self.__name = value.strip()

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        if not value.strip():
            raise ValueError("Số điện thoại không được để trống!")
        self.__phone = value.strip()


class Driver(User):
    """Lớp Driver kế thừa từ User, bổ sung thông tin hành nghề vận tải"""
    def __init__(self, user_id: str, name: str, phone: str, license_number: str):
        super().__init__(user_id, name, phone)
        self.__license_number = license_number
        self.__is_available = True
        self.__current_vehicle_id = None

    @property
    def license_number(self):
        return self.__license_number

    @license_number.setter
    def license_number(self, value: str):
        if not value.strip():
            raise ValueError("Số bằng lái không được để trống!")
        self.__license_number = value.strip()

    @property
    def is_available(self):
        return self.__is_available

    @is_available.setter
    def is_available(self, status: bool):
        if not isinstance(status, bool):
            raise ValueError("Trạng thái hoạt động phải là kiểu True/False!")
        self.__is_available = status

    @property
    def current_vehicle_id(self):
        return self.__current_vehicle_id

    @current_vehicle_id.setter
    def current_vehicle_id(self, vehicle_id):
        self.__current_vehicle_id = vehicle_id
