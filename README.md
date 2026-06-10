# 🚚 HỆ THỐNG QUẢN LÝ GIAO HÀNG / LOGISTICS MANAGEMENT SYSTEM

---

## 1. Dự án

| Thông tin | Chi tiết |
|---|---|
| **Tên dự án** | Logistics Management System |
| **Môn học** | Phương pháp lập trình (Programming Methods 1) |
| **Giảng viên** | Dr. Trần Văn Long – Khoa Tin học, ĐH Sư phạm Huế |
| **Sinh viên** | Chu Thị Nhung |
| **Email** | chunhungca26@gmail.com |
| **GitHub** | https://github.com/chunhungca26-netizen/LogisticsManagement |
| **Ngôn ngữ** | Python 3.8+ |
| **Giao diện** | CLI (Command Line Interface) |
| **Lưu trữ** | JSON |

---

## 2. Giới thiệu dự án

Hệ thống Quản lý Giao hàng / Logistics là một ứng dụng dòng lệnh (CLI) được xây dựng bằng Python, mô phỏng hoạt động thực tế của một đơn vị vận chuyển hàng hóa. Hệ thống cho phép quản lý toàn bộ quy trình từ việc đăng ký tài xế, quản lý đội xe, tạo và xử lý đơn hàng, đến thống kê doanh thu và xuất báo cáo.

Dự án được thiết kế theo mô hình **Lập trình Hướng đối tượng (OOP)** kết hợp với **kiến trúc phân tầng (Layered Architecture)**, đảm bảo mã nguồn rõ ràng, dễ bảo trì và mở rộng. Toàn bộ 4 tính chất đặc trưng của OOP được thể hiện một cách rõ ràng và có chủ đích thông qua cấu trúc các lớp trong dự án.

---

## 3. Mục tiêu dự án

- Xây dựng hệ thống quản lý logistics hoàn chỉnh theo mô hình OOP với đầy đủ 4 tính chất: **Đóng gói, Kế thừa, Đa hình, Trừu tượng**.
- Áp dụng **kiến trúc phân tầng** (models / services / views) để tách biệt dữ liệu, logic và giao diện.
- Triển khai đầy đủ **CRUD** (Thêm, Xem, Sửa, Xóa) cho 3 thực thể: Tài xế, Phương tiện, Đơn hàng.
- Cài đặt **tìm kiếm và sắp xếp** dữ liệu linh hoạt.
- Thực hiện **nghiệp vụ giao dịch phức tạp**: tự động phân công tài xế, lựa chọn xe phù hợp và tính cước phí dựa trên đa hình.
- **Lưu trữ bền vững** dữ liệu bằng JSON, đảm bảo không mất dữ liệu khi tắt chương trình.
- Cung cấp tính năng **thống kê nâng cao** và **xuất báo cáo CSV**.
- Quản lý mã nguồn chuyên nghiệp bằng **Git & GitHub**.

---

## 4. Các file trong dự án

| File | Mô tả |
|---|---|
| `main.py` | Điểm khởi chạy chương trình, khởi tạo các service và gọi menu |
| `models/vehicle.py` | Abstract class `Vehicle` và 3 lớp con: `Motorbike`, `LightTruck`, `RefrigeratedTruck` |
| `models/driver.py` | Lớp cha `User` và lớp con `Driver` |
| `models/order.py` | Lớp `Order` đại diện cho một đơn hàng giao vận |
| `models/__init__.py` | Export các lớp trong models |
| `services/vehicle_service.py` | Business logic quản lý phương tiện (CRUD, tìm kiếm, sắp xếp, JSON I/O) |
| `services/driver_service.py` | Business logic quản lý tài xế (CRUD, tìm kiếm, sắp xếp, JSON I/O) |
| `services/order_service.py` | Business logic quản lý đơn hàng, transaction logic, thống kê, xuất CSV |
| `services/__init__.py` | Export các service |
| `views/menu.py` | Giao diện CLI: toàn bộ menu tương tác với người dùng |
| `views/__init__.py` | Export menu |
| `data/vehicles.json` | Dữ liệu phương tiện (tự động sinh ra khi chạy) |
| `data/drivers.json` | Dữ liệu tài xế (tự động sinh ra khi chạy) |
| `data/orders.json` | Dữ liệu đơn hàng (tự động sinh ra khi chạy) |
| `data/orders_report.csv` | Báo cáo đơn hàng xuất ra (khi dùng chức năng export) |
| `data/drivers_report.csv` | Báo cáo tài xế xuất ra (khi dùng chức năng export) |
| `README.md` | Tài liệu mô tả dự án |

---

## 5. Cấu trúc thư mục dự án

```
LogisticsManagement/
└── project/
    ├── main.py
    ├── README.md
    ├── models/
    │   ├── __init__.py
    │   ├── vehicle.py          ← ABC + 3 lớp con (Inheritance, Polymorphism, Abstraction)
    │   ├── driver.py           ← User → Driver (Inheritance, Encapsulation)
    │   └── order.py            ← Order (Encapsulation)
    ├── services/
    │   ├── __init__.py
    │   ├── vehicle_service.py  ← CRUD + Search + Sort + JSON I/O
    │   ├── driver_service.py   ← CRUD + Search + Sort + JSON I/O
    │   └── order_service.py    ← Transaction Logic + Statistics + CSV Export
    ├── views/
    │   ├── __init__.py
    │   └── menu.py             ← Toàn bộ giao diện CLI
    └── data/                   ← Tự động sinh ra khi chạy lần đầu
        ├── vehicles.json
        ├── drivers.json
        ├── orders.json
        ├── orders_report.csv
        └── drivers_report.csv
```

---

## 6. Cấu trúc mã nguồn (Modular Design)

Dự án áp dụng **Kiến trúc 3 tầng (3-Layer Architecture)** nhằm tách biệt hoàn toàn giữa dữ liệu, logic và giao diện:

```
┌─────────────────────────────────────────────┐
│              views/menu.py                  │  ← Tầng Giao diện (Presentation Layer)
│         (Giao tiếp với người dùng)          │
└──────────────────┬──────────────────────────┘
                   │ gọi
┌──────────────────▼──────────────────────────┐
│   services/  (vehicle / driver / order)     │  ← Tầng Logic Nghiệp vụ (Service Layer)
│   (Xử lý CRUD, transaction, thống kê)       │
└──────────────────┬──────────────────────────┘
                   │ sử dụng
┌──────────────────▼──────────────────────────┐
│    models/  (Vehicle, Driver, Order)        │  ← Tầng Dữ liệu (Data / Model Layer)
│    (Định nghĩa cấu trúc đối tượng OOP)      │
└─────────────────────────────────────────────┘
                   │ lưu/đọc
┌──────────────────▼──────────────────────────┐
│            data/*.json                      │  ← Lưu trữ vĩnh viễn (JSON)
└─────────────────────────────────────────────┘
```

**Nguyên tắc thiết kế áp dụng:**
- **SRP (Single Responsibility Principle):** Mỗi lớp/hàm chỉ đảm nhiệm một nhiệm vụ duy nhất. Ví dụ: `VehicleService` chỉ xử lý logic liên quan đến phương tiện, không can thiệp vào tài xế hay đơn hàng.
- **DRY (Don't Repeat Yourself):** Logic tìm kiếm, sắp xếp, đọc/ghi JSON được đóng gói vào từng service, không lặp lại ở view.
- **Separation of Concerns:** View không trực tiếp thao tác dữ liệu; service không in ra màn hình trực tiếp (ngoại trừ thông báo kết quả giao dịch).

---

## 7. Các hàm chính trong chương trình

### `models/vehicle.py`

| Lớp / Hàm | Mô tả |
|---|---|
| `Vehicle(ABC)` | Abstract Base Class định nghĩa interface bắt buộc cho mọi loại xe |
| `Vehicle.calculate_fee(distance, package_type)` | **@abstractmethod** – mỗi loại xe tính cước riêng |
| `Vehicle.get_type_name()` | **@abstractmethod** – trả về tên loại xe dạng tiếng Việt |
| `Vehicle.payload` (setter) | Validate tải trọng không âm |
| `Motorbike.calculate_fee()` | 5.000đ/km, thêm 10.000đ nếu hàng fragile |
| `LightTruck.calculate_fee()` | 15.000đ/km, thêm 50.000đ nếu hàng bulky |
| `RefrigeratedTruck.calculate_fee()` | 25.000đ/km + 100.000đ phụ phí đông lạnh cố định |

### `models/driver.py`

| Lớp / Hàm | Mô tả |
|---|---|
| `User.__init__(user_id, name, phone)` | Lớp cha, khởi tạo thông tin cơ bản người dùng |
| `User.name` (setter) | Validate tên không được rỗng |
| `User.phone` (setter) | Validate số điện thoại không được rỗng |
| `Driver.__init__(...)` | Kế thừa User, thêm `license_number`, `is_available`, `current_vehicle_id` |
| `Driver.is_available` (setter) | Validate phải là kiểu `bool` |
| `Driver.license_number` (setter) | Validate số bằng lái không được rỗng |

### `models/order.py`

| Lớp / Hàm | Mô tả |
|---|---|
| `Order.__init__(customer_name, distance, package_type)` | Tạo đơn hàng, tự sinh `order_id` ngẫu nhiên (UUID 8 ký tự) và ghi `created_at` |
| `Order.status` (setter) | Cập nhật trạng thái đơn hàng |
| `Order.total_fee` (setter) | Gán cước phí sau khi tính toán |
| `Order.__str__()` | Định dạng hiển thị đẹp khi print đơn hàng |

### `services/vehicle_service.py`

| Hàm | Mô tả |
|---|---|
| `add_vehicle(vehicle)` | Thêm xe mới vào danh sách và lưu JSON |
| `get_all_vehicles()` | Trả về toàn bộ danh sách xe |
| `find_by_id(vehicle_id)` | Tìm xe theo ID (không phân biệt hoa/thường) |
| `update_vehicle(vehicle_id, new_brand, new_payload)` | Cập nhật hãng xe hoặc tải trọng |
| `delete_vehicle(vehicle_id)` | Xóa xe theo ID |
| `search_by_brand(keyword)` | Tìm xe theo từ khóa tên hãng |
| `sort_by_payload(descending)` | Sắp xếp xe theo tải trọng |
| `get_available_vehicles(package_type)` | Lọc xe phù hợp với loại hàng |
| `save_to_json()` | Ghi toàn bộ dữ liệu xe ra file JSON |
| `load_from_json()` | Nạp dữ liệu xe từ file JSON khi khởi động |

### `services/driver_service.py`

| Hàm | Mô tả |
|---|---|
| `add_driver(driver)` | Thêm tài xế mới |
| `get_all_drivers()` | Trả về toàn bộ danh sách tài xế |
| `find_by_id(user_id)` | Tìm tài xế theo ID |
| `update_driver(user_id, new_name, new_phone, new_license)` | Cập nhật thông tin tài xế |
| `delete_driver(user_id)` | Xóa tài xế theo ID |
| `search_by_name(keyword)` | Tìm tài xế theo từ khóa tên |
| `search_by_id(user_id)` | Tìm chính xác theo ID |
| `sort_by_name(descending)` | Sắp xếp tài xế theo tên A-Z hoặc Z-A |
| `get_available_drivers()` | Lọc danh sách tài xế đang rảnh |
| `save_to_json()` / `load_from_json()` | Đọc/ghi dữ liệu JSON |

### `services/order_service.py`

| Hàm | Mô tả |
|---|---|
| `create_order(customer_name, distance, package_type)` | **Transaction logic:** tạo đơn + phân công tài xế + chọn xe + tính phí đa hình + cập nhật trạng thái |
| `complete_order(order_id)` | Hoàn thành đơn, trả tài xế về trạng thái rảnh |
| `cancel_order(order_id)` | Hủy đơn, tự trả tài xế về rảnh nếu đang giao |
| `get_all_orders()` | Trả về toàn bộ danh sách đơn |
| `find_by_id(order_id)` | Tìm đơn theo ID |
| `search_by_customer(keyword)` | Tìm đơn theo tên khách hàng |
| `sort_by_fee(descending)` | Sắp xếp đơn theo cước phí |
| `sort_by_distance(descending)` | Sắp xếp đơn theo khoảng cách |
| `get_statistics()` | Thống kê tổng hợp: số đơn, doanh thu, top 3, phân loại theo loại hàng |
| `export_to_csv(filepath)` | Xuất danh sách đơn hàng ra file CSV |
| `export_drivers_csv(filepath)` | Xuất danh sách tài xế ra file CSV |
| `save_to_json()` / `load_from_json()` | Đọc/ghi dữ liệu JSON |

---

## 8. Chức năng

### 8.1. Quản lý Tài xế

- **Thêm tài xế:** Nhập mã, họ tên, số điện thoại, số bằng lái. Kiểm tra trùng mã trước khi thêm.
- **Xem danh sách:** Hiển thị bảng đầy đủ gồm mã, tên, SĐT, bằng lái, trạng thái (Rảnh / Đang giao).
- **Cập nhật:** Sửa tên, SĐT, bằng lái theo mã tài xế. Trường nào bỏ trống sẽ giữ nguyên.
- **Xóa:** Xóa theo mã, có xác nhận. Không cho xóa tài xế đang giao hàng.
- **Tìm kiếm:** Tìm theo ID hoặc theo từ khóa tên (không phân biệt hoa/thường).
- **Sắp xếp:** Sắp xếp tên A→Z hoặc Z→A.

### 8.2. Quản lý Phương tiện

- **Thêm xe:** Chọn loại xe (Xe máy / Xe tải nhẹ / Xe đông lạnh), nhập mã, hãng, tải trọng. Xe đông lạnh cần thêm nhiệt độ bảo quản.
- **Xem danh sách:** Hiển thị bảng gồm mã, hãng, loại xe, tải trọng.
- **Cập nhật:** Sửa hãng xe và/hoặc tải trọng theo mã xe.
- **Xóa:** Xóa theo mã, có xác nhận.
- **Tìm kiếm:** Tìm theo từ khóa tên hãng xe.
- **Sắp xếp:** Sắp xếp theo tải trọng từ cao xuống thấp hoặc ngược lại.

### 8.3. Quản lý Đơn hàng

- **Tạo đơn hàng (Transaction Logic):** Nhập tên khách hàng, khoảng cách, loại hàng → hệ thống tự động phân công tài xế rảnh + xe phù hợp + tính cước phí đa hình → cập nhật trạng thái tài xế → lưu toàn bộ.
- **Xem danh sách:** Hiển thị bảng gồm mã đơn, khách hàng, loại hàng, khoảng cách, cước phí, trạng thái.
- **Hoàn thành đơn:** Cập nhật trạng thái đơn → Hoàn thành, tự trả tài xế về rảnh.
- **Hủy đơn:** Hủy đơn đang giao hoặc đang chờ, tự trả tài xế về rảnh.
- **Tìm kiếm:** Tìm đơn theo tên khách hàng.
- **Sắp xếp:** Theo cước phí (cao→thấp / thấp→cao) hoặc theo khoảng cách (xa→gần / gần→xa).

### 8.4. Thống kê & Báo cáo

- **Thống kê tổng hợp:** Tổng đơn hàng, số đơn theo từng trạng thái, tổng doanh thu từ đơn hoàn thành, số tài xế rảnh, tổng phương tiện.
- **Thống kê theo loại hàng:** Số đơn và doanh thu theo từng nhóm (Thường / Dễ vỡ / Cồng kềnh / Đông lạnh).
- **Top 3:** Hiển thị 3 đơn hàng có cước phí cao nhất.
- **Xuất CSV đơn hàng:** File `data/orders_report.csv` gồm 9 cột, encoding UTF-8 (mở được bằng Excel).
- **Xuất CSV tài xế:** File `data/drivers_report.csv` gồm 5 cột.

---

## 9. Tính năng nâng cao đã triển khai

### 9.1. Tính Trừu tượng (Abstraction) với ABC

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def calculate_fee(self, distance: float, package_type: str) -> float:
        pass

    @abstractmethod
    def get_type_name(self) -> str:
        pass
```

`Vehicle` là Abstract Base Class – không thể khởi tạo trực tiếp. Bất kỳ lớp con nào cũng **bắt buộc** phải override `calculate_fee()` và `get_type_name()`, đảm bảo tính nhất quán của toàn bộ hệ thống xe.

### 9.2. Tính Đóng gói (Encapsulation)

Tất cả thuộc tính nhạy cảm đều là **private** (`__attribute`) và được kiểm soát qua `@property` / setter với logic validation:

```python
class Vehicle(ABC):
    def __init__(self, vehicle_id, brand, payload):
        self.__vehicle_id = vehicle_id   # private
        self.__brand = brand             # private
        self.__payload = payload         # private

    @payload.setter
    def payload(self, value):
        if value < 0:
            raise ValueError("Tải trọng không được phép nhỏ hơn 0!")
        self.__payload = value

class Driver(User):
    @is_available.setter
    def is_available(self, status: bool):
        if not isinstance(status, bool):
            raise ValueError("Trạng thái hoạt động phải là kiểu True/False!")
        self.__is_available = status
```

### 9.3. Tính Kế thừa (Inheritance)

Hai cây kế thừa rõ ràng:

```
User
 └── Driver

Vehicle (ABC)
 ├── Motorbike
 ├── LightTruck
 └── RefrigeratedTruck
```

`Driver` kế thừa `User` bằng `super().__init__()`, tái sử dụng toàn bộ thuộc tính `user_id`, `name`, `phone` mà không cần viết lại.

### 9.4. Tính Đa hình (Polymorphism)

Hàm `create_order()` trong `OrderService` gọi `vehicle.calculate_fee()` – Python tự động điều phối sang đúng lớp con:

```python
# Gọi cùng một tên hàm, nhưng mỗi loại xe tính khác nhau
fee = vehicle.calculate_fee(distance, package_type)
# → Motorbike      : distance × 5.000 (+10.000 nếu fragile)
# → LightTruck     : distance × 15.000 (+50.000 nếu bulky)
# → RefrigeratedTruck: distance × 25.000 + 100.000
```

### 9.5. Transaction Logic (Nghiệp vụ giao dịch phức tạp)

Khi tạo đơn hàng, hệ thống thực hiện một chuỗi thao tác liên kết:

```
[1] Kiểm tra tài xế rảnh
        ↓
[2] Kiểm tra xe phù hợp với loại hàng
        ↓
[3] Tính cước phí qua Polymorphism (calculate_fee)
        ↓
[4] Cập nhật: đơn hàng → "Đang giao"
        ↓
[5] Cập nhật: tài xế → is_available = False
        ↓
[6] Lưu đồng bộ: orders.json + drivers.json
```

### 9.6. Thống kê & Xuất CSV

`get_statistics()` nhóm và phân tích dữ liệu theo nhiều chiều: theo trạng thái, theo loại hàng, theo cước phí. Kết quả xuất ra CSV với encoding `utf-8-sig` (tương thích Excel tiếng Việt).

---

## 10. Kiểm tra dữ liệu (Validation)

Hệ thống kiểm tra dữ liệu đầu vào ở **2 tầng**:

**Tầng View (menu.py) – kiểm tra trước khi tạo đối tượng:**

| Trường hợp | Xử lý |
|---|---|
| Mã tài xế / mã xe để trống | Báo lỗi, không tiếp tục |
| Mã tài xế / mã xe đã tồn tại | Báo lỗi trùng lặp |
| Tải trọng / khoảng cách không phải số | `try-except ValueError`, báo lỗi |
| Tải trọng âm | Báo lỗi ngay tại view |
| Khoảng cách ≤ 0 | Báo lỗi |
| Loại hàng không hợp lệ | Kiểm tra whitelist `["normal", "fragile", "bulky", "cold"]` |
| Xóa tài xế đang giao hàng | Từ chối, báo lý do |
| Xóa / sửa đối tượng không tồn tại | Báo lỗi "Không tìm thấy" |
| Hủy đơn đã hoàn thành | Từ chối, báo lý do |

**Tầng Model (setter) – kiểm tra khi gán thuộc tính:**

| Setter | Validation |
|---|---|
| `Vehicle.payload` | `value < 0` → raise ValueError |
| `Driver.is_available` | `not isinstance(status, bool)` → raise ValueError |
| `Driver.name` / `User.name` | Chuỗi rỗng → raise ValueError |
| `Driver.phone` / `User.phone` | Chuỗi rỗng → raise ValueError |
| `Driver.license_number` | Chuỗi rỗng → raise ValueError |

---

## 11. Cách khởi chạy chương trình

### Yêu cầu hệ thống

- Python **3.8** trở lên
- Không cần cài thêm thư viện bên ngoài (chỉ dùng thư viện chuẩn: `json`, `csv`, `uuid`, `os`, `datetime`, `abc`)

### Các bước chạy

**Bước 1:** Clone hoặc giải nén dự án

```bash
git clone https://github.com/chunhungca26-netizen/LogisticsManagement.git
# hoặc giải nén file zip
```

**Bước 2:** Di chuyển vào thư mục dự án

```bash
cd LogisticsManagement/project
```

**Bước 3:** Chạy chương trình

```bash
python main.py
```

> **Lưu ý:** Thư mục `data/` sẽ được tạo tự động khi lần đầu thêm dữ liệu. Không cần tạo thủ công.

### Kiểm tra phiên bản Python

```bash
python --version
# hoặc
python3 --version
```

---

## 12. Menu chương trình

```
=======================================================
       HỆ THỐNG QUẢN LÝ GIAO HÀNG / LOGISTICS
=======================================================
  1. Quản lý Tài xế
  2. Quản lý Phương tiện
  3. Quản lý Đơn hàng
  4. Thống kê & Báo cáo
  0. Thoát
-------------------------------------------------------
```

**Menu Quản lý Tài xế:**
```
--- QUẢN LÝ TÀI XẾ ---
  1. Thêm tài xế mới
  2. Xem danh sách tài xế
  3. Cập nhật thông tin tài xế
  4. Xóa tài xế
  5. Tìm kiếm tài xế         (theo ID hoặc tên)
  6. Sắp xếp tài xế theo tên (A→Z hoặc Z→A)
  0. Quay lại
```

**Menu Quản lý Phương tiện:**
```
--- QUẢN LÝ PHƯƠNG TIỆN ---
  1. Thêm xe mới
  2. Xem danh sách xe
  3. Cập nhật thông tin xe
  4. Xóa xe
  5. Tìm kiếm xe theo hãng
  6. Sắp xếp xe theo tải trọng
  0. Quay lại
```

**Menu Quản lý Đơn hàng:**
```
--- QUẢN LÝ ĐƠN HÀNG ---
  1. Tạo đơn hàng mới
  2. Xem danh sách đơn hàng
  3. Hoàn thành đơn hàng
  4. Hủy đơn hàng
  5. Tìm kiếm đơn theo khách hàng
  6. Sắp xếp đơn theo cước phí
  7. Sắp xếp đơn theo khoảng cách
  0. Quay lại
```

**Menu Thống kê & Báo cáo:**
```
--- THỐNG KÊ & BÁO CÁO ---
  1. Xem thống kê tổng hợp
  2. Xuất danh sách đơn hàng ra CSV
  3. Xuất danh sách tài xế ra CSV
  0. Quay lại
```

**Ví dụ loại hàng và cách tính phí:**

| Loại hàng | Keyword | Xe phù hợp | Cách tính cước |
|---|---|---|---|
| Hàng thường | `normal` | Bất kỳ xe nào | Theo đơn giá của từng xe |
| Hàng dễ vỡ | `fragile` | Xe máy | 5.000đ/km + 10.000đ phụ phí |
| Hàng cồng kềnh | `bulky` | Xe tải nhẹ | 15.000đ/km + 50.000đ phụ phí |
| Hàng đông lạnh | `cold` | Xe đông lạnh | 25.000đ/km + 100.000đ phụ phí |

---

## 13. Các tính năng nâng cao (Advanced Features)

### 13.1. Auto-assign (Phân công tự động)

Khi tạo đơn hàng, hệ thống **tự động** thực hiện toàn bộ logic mà không cần người dùng chọn thủ công:

- Kiểm tra danh sách tài xế đang rảnh → chọn tài xế đầu tiên trong hàng chờ.
- Lọc xe phù hợp với loại hàng (fragile → Motorbike, bulky → LightTruck, cold → RefrigeratedTruck, normal → bất kỳ).
- Tính cước phí theo đúng công thức của lớp xe được chọn (**Polymorphism**).
- Đánh dấu tài xế `is_available = False` và ghi `current_vehicle_id`.
- Lưu đồng bộ cả `orders.json` và `drivers.json` trong cùng một thao tác.

### 13.2. Auto-release (Giải phóng tự động)

Khi hoàn thành hoặc hủy đơn hàng:
- Tự động tìm tài xế được phân công từ `assigned_driver_id`.
- Cập nhật `is_available = True` và `current_vehicle_id = None`.
- Lưu lại ngay lập tức, đảm bảo tài xế có thể nhận đơn mới tiếp theo.

### 13.3. Thống kê đa chiều

`get_statistics()` trả về dictionary chứa:
- Tổng số đơn và phân loại theo 4 trạng thái.
- Tổng doanh thu (chỉ tính đơn **Hoàn thành**).
- Phân nhóm theo loại hàng: số đơn + doanh thu từng nhóm.
- Top 3 đơn hàng có cước phí cao nhất.

### 13.4. Xuất CSV tương thích Excel

File CSV xuất ra dùng `encoding="utf-8-sig"` – BOM marker giúp Excel tự nhận diện tiếng Việt mà không cần cài đặt thêm.

---

## 14. Quá trình làm việc (Workflow & Git)

### Quy trình phát triển

```
[1] Thiết kế cấu trúc OOP và phân tầng
        ↓
[2] Xây dựng tầng models (Vehicle, Driver, Order)
        ↓
[3] Xây dựng tầng services (CRUD + JSON I/O)
        ↓
[4] Bổ sung Search, Sort, Transaction Logic
        ↓
[5] Xây dựng tầng views (CLI Menu)
        ↓
[6] Thêm Thống kê & Export CSV
        ↓
[7] Kiểm thử, sửa lỗi, hoàn thiện README
```

### Git & GitHub

Repository: https://github.com/chunhungca26-netizen/LogisticsManagement

```bash
# Clone dự án
git clone https://github.com/chunhungca26-netizen/LogisticsManagement.git

# Xem lịch sử commit
git log --oneline
```

**Quy ước commit message:**
- `feat:` – thêm tính năng mới
- `fix:` – sửa lỗi
- `refactor:` – cải thiện cấu trúc code
- `docs:` – cập nhật tài liệu

---

## 15. Tự đánh giá theo thang điểm (10 điểm)

| # | Tiêu chí | Mô tả triển khai trong dự án | Điểm tối đa | Tự đánh giá |
|---|---|---|---|---|
| 1 | **Encapsulation** | Tất cả thuộc tính của `Vehicle`, `User`, `Driver`, `Order` đều là private (`__attribute`). Có getter/setter với logic validation (payload ≥ 0, is_available phải bool, name/phone không rỗng). | 0.5 | **0.5** |
| 2 | **Inheritance** | Hai cây kế thừa: `User → Driver` và `Vehicle → Motorbike / LightTruck / RefrigeratedTruck`. Dùng `super().__init__()` chuẩn, không lặp code. | 0.5 | **0.5** |
| 3 | **Polymorphism & Abstraction** | `Vehicle` là ABC với 2 `@abstractmethod`. 3 lớp con override `calculate_fee()` với công thức khác nhau. `OrderService.create_order()` gọi đa hình trực tiếp. | 1.0 | **1.0** |
| 4 | **Layered Architecture** | Phân tầng rõ ràng: `models/` / `services/` / `views/`. Import chéo đúng chiều (view → service → model). | 1.0 | **1.0** |
| 5 | **Clean Code (SRP)** | Tên lớp CamelCase, hàm/biến snake_case. Mỗi service chỉ xử lý 1 entity. Mỗi hàm chỉ làm 1 việc (add, delete, search là các hàm riêng biệt). | 0.5 | **0.5** |
| 6 | **Exception Handling** | `try-except` ở tất cả nơi nhập số (tải trọng, khoảng cách, nhiệt độ). Setter raise `ValueError` có thông báo rõ ràng. `load_from_json()` có `try-except` chống crash khi file hỏng. | 0.5 | **0.5** |
| 7 | **CRUD** | Đầy đủ Thêm / Xem / Sửa / Xóa cho cả 3 entity (Tài xế, Xe, Đơn hàng). Bảng hiển thị căn chỉnh, rõ ràng. Có xác nhận trước khi xóa. | 1.0 | **1.0** |
| 8 | **Search & Sort** | Tìm kiếm: theo ID, theo tên (tài xế), theo hãng (xe), theo tên khách hàng (đơn). Sắp xếp: tên A-Z/Z-A (tài xế), tải trọng (xe), cước phí và khoảng cách (đơn). | 1.0 | **1.0** |
| 9 | **Permanent Storage (File I/O)** | Dữ liệu tự động load khi khởi động (`load_from_json()`), lưu ngay sau mỗi thao tác thay đổi (`save_to_json()`). 3 file JSON riêng biệt cho 3 entity. | 1.0 | **1.0** |
| 10 | **Complex Transaction Logic** | `create_order()` thực hiện chuỗi logic: kiểm tra tài xế rảnh → kiểm tra xe phù hợp → tính phí đa hình → cập nhật trạng thái tài xế → lưu đồng bộ 2 file JSON. `complete_order()` và `cancel_order()` tự động giải phóng tài xế. | 1.0 | **1.0** |
| 11 | **Advanced Statistics & Export** | `get_statistics()` thống kê theo trạng thái, theo loại hàng, top 3 cước phí cao nhất. Xuất 2 file CSV (`orders_report.csv`, `drivers_report.csv`) encoding UTF-8 BOM tương thích Excel. | 1.0 | **1.0** |
| 12 | **Advanced Technology** | Sử dụng JSON làm persistent storage với cấu trúc dữ liệu rõ ràng, tự động serialize/deserialize đa hình (phân loại lại đúng lớp con khi load). | 0.5 | **0.4** |
| 13 | **Git & GitHub** | Có repository public trên GitHub. Có README.md đầy đủ. Commit message theo quy ước feat/fix/docs. | 0.5 | **0.4** |
| | | **TỔNG** | **10.0** | **9.8** |

> **Ghi chú tự đánh giá:**
> - Tiêu chí 12 tự đánh giá 0.4/0.5 vì dự án dùng JSON thay vì SQLite/Database, và giao diện là CLI thay vì GUI (đề cho chọn 1 trong 2 – đây là giải pháp hợp lệ nhưng ít điểm ấn tượng hơn).
> - Tiêu chí 13 tự đánh giá 0.4/0.5 vì lịch sử commit chưa đủ nhiều và liên tục trong quá trình phát triển.
