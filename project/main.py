from services.driver_service import DriverService
from services.vehicle_service import VehicleService
from services.order_service import OrderService
from views.menu import LogisticsMenu


def main():
    print("\n  Đang khởi động hệ thống, nạp dữ liệu...")

    # Khởi tạo services (tự động load JSON cũ nếu có)
    vehicle_service = VehicleService()
    driver_service = DriverService()
    order_service = OrderService(driver_service, vehicle_service)

    print("  ✅ Sẵn sàng!")

    # Khởi tạo và chạy menu
    menu = LogisticsMenu(order_service)
    menu.display_main_menu()


if __name__ == "__main__":
    main()
