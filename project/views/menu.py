from models.driver import Driver
from models.vehicle import Motorbike, LightTruck, RefrigeratedTruck


def print_separator(char="=", length=55):
    print(char * length)


def print_header(title: str):
    print_separator()
    print(f"  {title}")
    print_separator()


class LogisticsMenu:
    def __init__(self, order_service):
        self.order_service = order_service
        self.driver_service = order_service.driver_service
        self.vehicle_service = order_service.vehicle_service

    # ================================================================
    # MAIN MENU
    # ================================================================
    def display_main_menu(self):
        while True:
            print("\n" + "=" * 55)
            print("       HỆ THỐNG QUẢN LÝ GIAO HÀNG / LOGISTICS")
            print("=" * 55)
            print("  1. Quản lý Tài xế")
            print("  2. Quản lý Phương tiện")
            print("  3. Quản lý Đơn hàng")
            print("  4. Thống kê & Báo cáo")
            print("  0. Thoát")
            print("-" * 55)
            choice = input("  Chọn chức năng: ").strip()

            if choice == "1":
                self.driver_menu()
            elif choice == "2":
                self.vehicle_menu()
            elif choice == "3":
                self.order_menu()
            elif choice == "4":
                self.report_menu()
            elif choice == "0":
                print("\n  Tạm biệt! Dữ liệu đã được lưu.\n")
                break
            else:
                print("  ⚠️  Lựa chọn không hợp lệ, vui lòng thử lại.")

    # ================================================================
    # MENU TÀI XẾ
    # ================================================================
    def driver_menu(self):
        while True:
            print("\n--- QUẢN LÝ TÀI XẾ ---")
            print("  1. Thêm tài xế mới")
            print("  2. Xem danh sách tài xế")
            print("  3. Cập nhật thông tin tài xế")
            print("  4. Xóa tài xế")
            print("  5. Tìm kiếm tài xế")
            print("  6. Sắp xếp tài xế theo tên")
            print("  0. Quay lại")
            choice = input("  Chọn: ").strip()

            if choice == "1":
                self.add_driver()
            elif choice == "2":
                self.list_drivers(self.driver_service.get_all_drivers())
            elif choice == "3":
                self.update_driver()
            elif choice == "4":
                self.delete_driver()
            elif choice == "5":
                self.search_driver()
            elif choice == "6":
                self.sort_drivers()
            elif choice == "0":
                break
            else:
                print("  ⚠️  Lựa chọn không hợp lệ.")

    def add_driver(self):
        print("\n-- Thêm Tài Xế Mới --")
        user_id = input("  Mã tài xế    : ").strip()
        if not user_id:
            print("  ❌ Mã tài xế không được để trống!")
            return
        if self.driver_service.find_by_id(user_id):
            print(f"  ❌ Mã tài xế '{user_id}' đã tồn tại!")
            return
        name     = input("  Họ tên       : ").strip()
        phone    = input("  Số điện thoại: ").strip()
        license_ = input("  Số bằng lái  : ").strip()
        if not all([name, phone, license_]):
            print("  ❌ Vui lòng nhập đầy đủ thông tin!")
            return
        try:
            driver = Driver(user_id, name, phone, license_)
            self.driver_service.add_driver(driver)
            print(f"  ✅ Đã thêm tài xế: {name} ({user_id})")
        except ValueError as e:
            print(f"  ❌ Lỗi: {e}")

    def update_driver(self):
        print("\n-- Cập Nhật Tài Xế --")
        user_id = input("  Nhập mã tài xế cần cập nhật: ").strip()
        d = self.driver_service.find_by_id(user_id)
        if not d:
            print(f"  ❌ Không tìm thấy tài xế '{user_id}'")
            return
        print(f"  Đang sửa: {d.name} | SĐT: {d.phone} | Bằng: {d.license_number}")
        print("  (Bỏ trống = giữ nguyên)")
        new_name    = input("  Họ tên mới       : ").strip()
        new_phone   = input("  SĐT mới          : ").strip()
        new_license = input("  Số bằng lái mới  : ").strip()
        ok = self.driver_service.update_driver(
            user_id,
            new_name=new_name or None,
            new_phone=new_phone or None,
            new_license=new_license or None
        )
        if ok:
            print("  ✅ Cập nhật thành công!")
        else:
            print("  ❌ Cập nhật thất bại.")

    def delete_driver(self):
        print("\n-- Xóa Tài Xế --")
        user_id = input("  Nhập mã tài xế cần xóa: ").strip()
        d = self.driver_service.find_by_id(user_id)
        if not d:
            print(f"  ❌ Không tìm thấy tài xế '{user_id}'")
            return
        if not d.is_available:
            print(f"  ❌ Tài xế '{d.name}' đang giao hàng, không thể xóa!")
            return
        confirm = input(f"  ⚠️  Xác nhận xóa tài xế '{d.name}'? (y/n): ").strip().lower()
        if confirm == "y":
            self.driver_service.delete_driver(user_id)
            print(f"  ✅ Đã xóa tài xế {d.name}.")
        else:
            print("  Đã hủy thao tác.")

    def search_driver(self):
        print("\n-- Tìm Kiếm Tài Xế --")
        print("  1. Tìm theo ID")
        print("  2. Tìm theo tên")
        sub = input("  Chọn: ").strip()
        if sub == "1":
            uid = input("  Nhập mã tài xế: ").strip()
            d = self.driver_service.search_by_id(uid)
            results = [d] if d else []
        elif sub == "2":
            kw = input("  Nhập từ khóa tên: ").strip()
            results = self.driver_service.search_by_name(kw)
        else:
            print("  ⚠️  Lựa chọn không hợp lệ.")
            return
        if not results:
            print("  Không tìm thấy kết quả nào.")
        else:
            self.list_drivers(results)

    def sort_drivers(self):
        print("\n-- Sắp Xếp Tài Xế --")
        print("  1. Tên A → Z")
        print("  2. Tên Z → A")
        sub = input("  Chọn: ").strip()
        desc = sub == "2"
        sorted_list = self.driver_service.sort_by_name(descending=desc)
        self.list_drivers(sorted_list)

    def list_drivers(self, drivers):
        if not drivers:
            print("  (Chưa có tài xế nào)")
            return
        print(f"\n  {'Mã':<10} {'Tên':<20} {'SĐT':<14} {'Bằng lái':<14} {'Trạng thái'}")
        print("  " + "-" * 70)
        for d in drivers:
            status = "✅ Rảnh" if d.is_available else "🚚 Đang giao"
            print(f"  {d.user_id:<10} {d.name:<20} {d.phone:<14} {d.license_number:<14} {status}")

    # ================================================================
    # MENU PHƯƠNG TIỆN
    # ================================================================
    def vehicle_menu(self):
        while True:
            print("\n--- QUẢN LÝ PHƯƠNG TIỆN ---")
            print("  1. Thêm xe mới")
            print("  2. Xem danh sách xe")
            print("  3. Cập nhật thông tin xe")
            print("  4. Xóa xe")
            print("  5. Tìm kiếm xe theo hãng")
            print("  6. Sắp xếp xe theo tải trọng")
            print("  0. Quay lại")
            choice = input("  Chọn: ").strip()

            if choice == "1":
                self.add_vehicle()
            elif choice == "2":
                self.list_vehicles(self.vehicle_service.get_all_vehicles())
            elif choice == "3":
                self.update_vehicle()
            elif choice == "4":
                self.delete_vehicle()
            elif choice == "5":
                self.search_vehicle()
            elif choice == "6":
                self.sort_vehicles()
            elif choice == "0":
                break
            else:
                print("  ⚠️  Lựa chọn không hợp lệ.")

    def add_vehicle(self):
        print("\n-- Thêm Phương Tiện Mới --")
        print("  Loại xe: 1. Xe máy   2. Xe tải nhẹ   3. Xe đông lạnh")
        v_type = input("  Chọn loại: ").strip()
        v_id   = input("  Mã xe     : ").strip()
        if not v_id:
            print("  ❌ Mã xe không được để trống!")
            return
        if self.vehicle_service.find_by_id(v_id):
            print(f"  ❌ Mã xe '{v_id}' đã tồn tại!")
            return
        brand = input("  Hãng xe   : ").strip()
        if not brand:
            print("  ❌ Hãng xe không được để trống!")
            return
        try:
            payload = float(input("  Tải trọng (kg): ").strip())
            if payload < 0:
                raise ValueError
        except ValueError:
            print("  ❌ Tải trọng phải là số dương!")
            return

        try:
            if v_type == "1":
                vehicle = Motorbike(v_id, brand, payload)
            elif v_type == "2":
                vehicle = LightTruck(v_id, brand, payload)
            elif v_type == "3":
                temp = float(input("  Nhiệt độ bảo quản (°C): ").strip())
                vehicle = RefrigeratedTruck(v_id, brand, payload, temp)
            else:
                print("  ❌ Loại xe không hợp lệ!")
                return
            self.vehicle_service.add_vehicle(vehicle)
            print(f"  ✅ Đã thêm xe: {brand} ({v_id})")
        except Exception as e:
            print(f"  ❌ Lỗi: {e}")

    def update_vehicle(self):
        print("\n-- Cập Nhật Xe --")
        v_id = input("  Nhập mã xe cần cập nhật: ").strip()
        v = self.vehicle_service.find_by_id(v_id)
        if not v:
            print(f"  ❌ Không tìm thấy xe '{v_id}'")
            return
        print(f"  Đang sửa: {v.brand} | Tải trọng: {v.payload} kg")
        print("  (Bỏ trống = giữ nguyên)")
        new_brand = input("  Hãng xe mới    : ").strip()
        new_payload_str = input("  Tải trọng mới  : ").strip()
        new_payload = None
        if new_payload_str:
            try:
                new_payload = float(new_payload_str)
            except ValueError:
                print("  ❌ Tải trọng phải là số!")
                return
        ok = self.vehicle_service.update_vehicle(v_id, new_brand or None, new_payload)
        if ok:
            print("  ✅ Cập nhật thành công!")
        else:
            print("  ❌ Cập nhật thất bại.")

    def delete_vehicle(self):
        print("\n-- Xóa Xe --")
        v_id = input("  Nhập mã xe cần xóa: ").strip()
        v = self.vehicle_service.find_by_id(v_id)
        if not v:
            print(f"  ❌ Không tìm thấy xe '{v_id}'")
            return
        confirm = input(f"  ⚠️  Xác nhận xóa xe '{v.brand}' ({v_id})? (y/n): ").strip().lower()
        if confirm == "y":
            self.vehicle_service.delete_vehicle(v_id)
            print(f"  ✅ Đã xóa xe {v.brand}.")
        else:
            print("  Đã hủy thao tác.")

    def search_vehicle(self):
        kw = input("\n  Nhập hãng xe cần tìm: ").strip()
        results = self.vehicle_service.search_by_brand(kw)
        if not results:
            print("  Không tìm thấy kết quả nào.")
        else:
            self.list_vehicles(results)

    def sort_vehicles(self):
        print("\n-- Sắp Xếp Xe --")
        print("  1. Tải trọng cao → thấp")
        print("  2. Tải trọng thấp → cao")
        sub = input("  Chọn: ").strip()
        desc = sub != "2"
        sorted_list = self.vehicle_service.sort_by_payload(descending=desc)
        self.list_vehicles(sorted_list)

    def list_vehicles(self, vehicles):
        if not vehicles:
            print("  (Chưa có xe nào)")
            return
        print(f"\n  {'Mã xe':<12} {'Hãng':<18} {'Loại xe':<16} {'Tải trọng':>10}")
        print("  " + "-" * 60)
        for v in vehicles:
            print(f"  {v.vehicle_id:<12} {v.brand:<18} {v.get_type_name():<16} {v.payload:>8} kg")

    # ================================================================
    # MENU ĐƠN HÀNG
    # ================================================================
    def order_menu(self):
        while True:
            print("\n--- QUẢN LÝ ĐƠN HÀNG ---")
            print("  1. Tạo đơn hàng mới")
            print("  2. Xem danh sách đơn hàng")
            print("  3. Hoàn thành đơn hàng")
            print("  4. Hủy đơn hàng")
            print("  5. Tìm kiếm đơn theo khách hàng")
            print("  6. Sắp xếp đơn theo cước phí")
            print("  7. Sắp xếp đơn theo khoảng cách")
            print("  0. Quay lại")
            choice = input("  Chọn: ").strip()

            if choice == "1":
                self.create_order()
            elif choice == "2":
                self.list_orders(self.order_service.get_all_orders())
            elif choice == "3":
                self.complete_order()
            elif choice == "4":
                self.cancel_order()
            elif choice == "5":
                self.search_order()
            elif choice == "6":
                self.sort_orders_by_fee()
            elif choice == "7":
                self.sort_orders_by_distance()
            elif choice == "0":
                break
            else:
                print("  ⚠️  Lựa chọn không hợp lệ.")

    def create_order(self):
        print("\n-- Tạo Đơn Hàng Mới --")
        customer = input("  Tên khách hàng: ").strip()
        if not customer:
            print("  ❌ Tên khách hàng không được để trống!")
            return
        try:
            distance = float(input("  Khoảng cách (km): ").strip())
            if distance <= 0:
                raise ValueError
        except ValueError:
            print("  ❌ Khoảng cách phải là số dương!")
            return
        print("  Loại hàng: normal (thường) / fragile (dễ vỡ) / bulky (cồng kềnh) / cold (đông lạnh)")
        pkg_type = input("  Loại hàng: ").strip().lower()
        if pkg_type not in ["normal", "fragile", "bulky", "cold"]:
            print("  ❌ Loại hàng không hợp lệ!")
            return
        self.order_service.create_order(customer, distance, pkg_type)

    def complete_order(self):
        order_id = input("  Nhập mã đơn cần hoàn thành: ").strip().upper()
        self.order_service.complete_order(order_id)

    def cancel_order(self):
        order_id = input("  Nhập mã đơn cần hủy: ").strip().upper()
        self.order_service.cancel_order(order_id)

    def search_order(self):
        kw = input("  Nhập tên khách hàng: ").strip()
        results = self.order_service.search_by_customer(kw)
        if not results:
            print("  Không tìm thấy kết quả nào.")
        else:
            self.list_orders(results)

    def sort_orders_by_fee(self):
        print("\n-- Sắp Xếp Theo Cước Phí --")
        print("  1. Cao → Thấp")
        print("  2. Thấp → Cao")
        sub = input("  Chọn: ").strip()
        desc = sub != "2"
        sorted_list = self.order_service.sort_by_fee(descending=desc)
        self.list_orders(sorted_list)

    def sort_orders_by_distance(self):
        print("\n-- Sắp Xếp Theo Khoảng Cách --")
        print("  1. Xa → Gần")
        print("  2. Gần → Xa")
        sub = input("  Chọn: ").strip()
        desc = sub != "2"
        sorted_list = self.order_service.sort_by_distance(descending=desc)
        self.list_orders(sorted_list)

    def list_orders(self, orders):
        if not orders:
            print("  (Chưa có đơn hàng nào)")
            return
        print(f"\n  {'Mã đơn':<10} {'Khách hàng':<20} {'Loại':<10} {'KC(km)':>7} {'Cước phí':>14} {'Trạng thái'}")
        print("  " + "-" * 78)
        for o in orders:
            print(f"  {o.order_id:<10} {o.customer_name:<20} {o.package_type:<10} "
                  f"{o.distance:>7.1f} {o.total_fee:>12,.0f}đ  {o.status}")

    # ================================================================
    # MENU THỐNG KÊ & BÁO CÁO
    # ================================================================
    def report_menu(self):
        while True:
            print("\n--- THỐNG KÊ & BÁO CÁO ---")
            print("  1. Xem thống kê tổng hợp")
            print("  2. Xuất danh sách đơn hàng ra CSV")
            print("  3. Xuất danh sách tài xế ra CSV")
            print("  0. Quay lại")
            choice = input("  Chọn: ").strip()

            if choice == "1":
                self.show_statistics()
            elif choice == "2":
                self.order_service.export_to_csv()
            elif choice == "3":
                self.order_service.export_drivers_csv()
            elif choice == "0":
                break
            else:
                print("  ⚠️  Lựa chọn không hợp lệ.")

    def show_statistics(self):
        stats = self.order_service.get_statistics()
        print("\n" + "=" * 55)
        print("          THỐNG KÊ TỔNG HỢP HỆ THỐNG")
        print("=" * 55)
        print(f"  Tổng số đơn hàng   : {stats['total_orders']}")
        print(f"  ✅ Hoàn thành      : {stats['completed']}")
        print(f"  🚚 Đang giao       : {stats['delivering']}")
        print(f"  ⏳ Chờ xử lý      : {stats['pending']}")
        print(f"  ❌ Đã hủy         : {stats['cancelled']}")
        print(f"  💰 Doanh thu       : {stats['total_revenue']:,.0f} VNĐ")
        print(f"\n  Tổng tài xế        : {len(self.driver_service.get_all_drivers())}")
        print(f"  Tài xế đang rảnh   : {len(self.driver_service.get_available_drivers())}")
        print(f"  Tổng phương tiện   : {len(self.vehicle_service.get_all_vehicles())}")

        if stats["pkg_stats"]:
            print("\n  --- Thống kê theo loại hàng ---")
            pkg_labels = {"normal": "Thường", "fragile": "Dễ vỡ", "bulky": "Cồng kềnh", "cold": "Đông lạnh"}
            for pkg, s in stats["pkg_stats"].items():
                label = pkg_labels.get(pkg, pkg)
                print(f"  {label:<12}: {s['count']} đơn | DT hoàn thành: {s['revenue']:,.0f} VNĐ")

        if stats["top3"]:
            print("\n  --- Top 3 đơn cước phí cao nhất ---")
            for i, o in enumerate(stats["top3"], 1):
                print(f"  #{i} [{o.order_id}] {o.customer_name} - {o.total_fee:,.0f} VNĐ ({o.status})")

        print("=" * 55)
