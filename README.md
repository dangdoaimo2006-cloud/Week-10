# Lab 10 - Smart Home Mini

**Sinh viên:** Nguyễn Hải Đăng  
**MSSV:** 202418863

Chương trình Python mô phỏng một số thiết bị trong nhà thông minh: đèn, quạt và cửa. Bài tập minh họa cách tạo thiết bị bằng Factory và dùng một cấu hình chung bằng Singleton.

## Chức năng

- Bật/tắt đèn và quạt.
- Khóa/mở khóa cửa.
- Tạo thiết bị theo loại `light`, `fan` hoặc `door`.
- Lấy cấu hình nhà với cùng một đối tượng `HomeConfiguration`.
- Sơ đồ UML mô tả thêm cách tổ chức các thao tác nhà thông minh bằng Facade.

## Cấu trúc

```text
week10/
├── README.md
├── main.py
├── docs/
│   └── analysis-and-design.md
├── src/
│   ├── devices.py
│   ├── device_factory.py
│   └── home_configuration.py
└── tests/
    └── test_devices.py
```

## Chạy chương trình

Yêu cầu Python 3.10 trở lên, không cần cài thêm thư viện.

```bash
python main.py
```

Chạy kiểm tra:

```bash
python -m unittest discover -s tests -v
```

## Thiết kế

- `IDevice` định nghĩa thao tác bật và tắt thiết bị.
- `ILockable` bổ sung thao tác khóa và mở khóa cho cửa.
- `DeviceFactory` chọn lớp thiết bị dựa trên loại đầu vào.
- `HomeConfiguration` giữ tên nhà và mức sáng ban đêm dùng chung.
- UML lớp và phân tích thiết kế nằm trong [`docs/analysis-and-design.md`](docs/analysis-and-design.md).

Factory giúp phần chạy chương trình không cần tự chọn constructor của từng thiết bị. Singleton giúp các phần của ứng dụng dùng chung cấu hình. Facade được dùng trong sơ đồ để thể hiện cách gom nhiều thao tác thành các chế độ như Đi làm và Đi ngủ.

Mã nguồn: [GitHub - Week-10](https://github.com/dangdoaimo2006-cloud/Week-10).
