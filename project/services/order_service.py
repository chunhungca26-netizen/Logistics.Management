import json
import os
import csv
from datetime import datetime
from models.order import Order

class OrderService:
    def __init__(self, driver_service, vehicle_service, data_file="data/orders.json"):
        self.driver_service = driver_service
        self.vehicle_service = vehicle_service
        self.data_file = data_file
        self.orders = []
        self.load_from_json()

    # ----------------------------------------------------------------
    # TRANSACTION LOGIC - Tạo đơn hàng (nghiệp vụ phức tạp)
    # ----------------------------------------------------------------
    def create_order(self, customer_name: str, distance: float, package_type: str):
        """Tạo đơn hàng mới: tự động phân công tài xế + xe + tính phí đa hình"""
        order = Order(customer_name, distance, package_type)

        available_drivers = self.driver_service.get_available_drivers()
        if not available_drivers:
            print("  ❌ Không có tài xế rảnh để nhận đơn!")
            return None

        available_vehicles = self.vehicle_service.get_available_vehicles(package_type)
        if not available_vehicles:
            print("  ❌ Không có xe phù hợp với loại hàng này!")
            return None

        driver = available_drivers[0]
        vehicle = available_vehicles[0]

        # ĐA HÌNH: gọi calculate_fee() của từng loại xe khác nhau
        fee = vehicle.calculate_fee(distance, package_type)

        order.assigned_driver_id = driver.user_id
        order.assigned_vehicle_id = vehicle.vehicle_id
        order.total_fee = fee
        order.status = "Đang giao"

        driver.is_available = False
        driver.current_vehicle_id = vehicle.vehicle_id

        self.orders.append(order)
        self.save_to_json()
        self.driver_service.save_to_json()

        print(f"\n  ✅ Tạo đơn thành công!")
        print(f"  Mã đơn    : #{order.order_id}")
        print(f"  Tài xế    : {driver.name} ({driver.phone})")
        print(f"  Xe        : {vehicle.brand} - {vehicle.get_type_name()} ({vehicle.vehicle_id})")
        print(f"  Cước phí  : {fee:,.0f} VNĐ")
        return order

    def complete_order(self, order_id: str):
        """Hoàn thành đơn, trả tài xế về trạng thái rảnh"""
        for order in self.orders:
            if order.order_id == order_id:
                order.status = "Hoàn thành"
                driver = self.driver_service.find_by_id(order.assigned_driver_id)
                if driver:
                    driver.is_available = True
                    driver.current_vehicle_id = None
                self.save_to_json()
                self.driver_service.save_to_json()
                print(f"  ✅ Đơn #{order_id} đã hoàn thành!")
                return True
        print(f"  ❌ Không tìm thấy đơn #{order_id}")
        return False

    def cancel_order(self, order_id: str):
        """Hủy đơn hàng đang chờ xử lý"""
        for order in self.orders:
            if order.order_id == order_id:
                if order.status == "Hoàn thành":
                    print("  ❌ Không thể hủy đơn đã hoàn thành!")
                    return False
                # Trả tài xế về rảnh nếu đang giao
                if order.assigned_driver_id:
                    driver = self.driver_service.find_by_id(order.assigned_driver_id)
                    if driver:
                        driver.is_available = True
                        driver.current_vehicle_id = None
                        self.driver_service.save_to_json()
                order.status = "Đã hủy"
                self.save_to_json()
                print(f"  ✅ Đã hủy đơn #{order_id}")
                return True
        print(f"  ❌ Không tìm thấy đơn #{order_id}")
        return False

    # ----------------------------------------------------------------
    # CRUD - Get / Search / Sort
    # ----------------------------------------------------------------
    def get_all_orders(self):
        return self.orders

    def find_by_id(self, order_id: str):
        for o in self.orders:
            if o.order_id == order_id.upper():
                return o
        return None

    def search_by_customer(self, keyword: str):
        """Tìm đơn theo tên khách hàng"""
        keyword = keyword.lower()
        return [o for o in self.orders if keyword in o.customer_name.lower()]

    def sort_by_fee(self, descending: bool = True):
        """Sắp xếp đơn theo cước phí"""
        return sorted(self.orders, key=lambda o: o.total_fee, reverse=descending)

    def sort_by_distance(self, descending: bool = True):
        """Sắp xếp đơn theo khoảng cách"""
        return sorted(self.orders, key=lambda o: o.distance, reverse=descending)

    # ----------------------------------------------------------------
    # THỐNG KÊ & BÁO CÁO
    # ----------------------------------------------------------------
    def get_statistics(self):
        """Thống kê tổng hợp"""
        total_orders = len(self.orders)
        completed = [o for o in self.orders if o.status == "Hoàn thành"]
        delivering = [o for o in self.orders if o.status == "Đang giao"]
        cancelled = [o for o in self.orders if o.status == "Đã hủy"]
        pending = [o for o in self.orders if o.status == "Chờ xử lý"]

        total_revenue = sum(o.total_fee for o in completed)

        # Thống kê theo loại hàng
        pkg_stats = {}
        for o in self.orders:
            pkg = o.package_type
            if pkg not in pkg_stats:
                pkg_stats[pkg] = {"count": 0, "revenue": 0}
            pkg_stats[pkg]["count"] += 1
            if o.status == "Hoàn thành":
                pkg_stats[pkg]["revenue"] += o.total_fee

        # Top 3 đơn có cước cao nhất
        top3 = sorted(self.orders, key=lambda o: o.total_fee, reverse=True)[:3]

        return {
            "total_orders": total_orders,
            "completed": len(completed),
            "delivering": len(delivering),
            "cancelled": len(cancelled),
            "pending": len(pending),
            "total_revenue": total_revenue,
            "pkg_stats": pkg_stats,
            "top3": top3
        }

    def export_to_csv(self, filepath="data/orders_report.csv"):
        """Xuất danh sách đơn hàng ra file CSV"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        try:
            with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Mã đơn", "Khách hàng", "Khoảng cách (km)",
                    "Loại hàng", "Cước phí (VNĐ)", "Trạng thái",
                    "Tài xế ID", "Xe ID", "Thời gian tạo"
                ])
                for o in self.orders:
                    writer.writerow([
                        o.order_id, o.customer_name, o.distance,
                        o.package_type, f"{o.total_fee:.0f}", o.status,
                        o.assigned_driver_id or "", o.assigned_vehicle_id or "",
                        o.created_at
                    ])
            print(f"  ✅ Xuất CSV thành công: {filepath}")
            return True
        except Exception as e:
            print(f"  ❌ Lỗi xuất CSV: {e}")
            return False

    def export_drivers_csv(self, filepath="data/drivers_report.csv"):
        """Xuất danh sách tài xế ra CSV"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        try:
            drivers = self.driver_service.get_all_drivers()
            with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                writer.writerow(["Mã tài xế", "Họ tên", "Số điện thoại", "Bằng lái", "Trạng thái"])
                for d in drivers:
                    status = "Rảnh" if d.is_available else "Đang giao"
                    writer.writerow([d.user_id, d.name, d.phone, d.license_number, status])
            print(f"  ✅ Xuất CSV thành công: {filepath}")
            return True
        except Exception as e:
            print(f"  ❌ Lỗi xuất CSV: {e}")
            return False

    # ----------------------------------------------------------------
    # FILE I/O (JSON)
    # ----------------------------------------------------------------
    def save_to_json(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        data_to_save = []
        for o in self.orders:
            data_to_save.append({
                "order_id": o.order_id,
                "customer_name": o.customer_name,
                "distance": o.distance,
                "package_type": o.package_type,
                "status": o.status,
                "assigned_driver_id": o.assigned_driver_id,
                "assigned_vehicle_id": o.assigned_vehicle_id,
                "total_fee": o.total_fee,
                "created_at": o.created_at
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
                    o = Order(item["customer_name"], item["distance"], item["package_type"])
                    o.order_id = item["order_id"]
                    o.status = item["status"]
                    o.assigned_driver_id = item["assigned_driver_id"]
                    o.assigned_vehicle_id = item["assigned_vehicle_id"]
                    o.total_fee = item["total_fee"]
                    o.created_at = item.get("created_at", "N/A")
                    self.orders.append(o)
        except Exception:
            self.orders = []
