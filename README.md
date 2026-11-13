# Lab 10 - Smart Home Mini

**Sinh viên:** Nguyễn Hải Đăng  
**MSSV:** 202418863

Bài tập mô phỏng nhà thông minh. Phần code hiện làm một phần nhỏ: abstraction thiết bị, ba loại thiết bị và Factory. UML có phác thảo thêm Singleton và Facade để làm định hướng; hai phần đó chưa được cài đặt.

## Chạy chương trình

Yêu cầu Python 3.10 trở lên, không cần cài thư viện ngoài.

```bash
python main.py
```

Chạy kiểm tra các tình huống chính:

```bash
python -m unittest discover -s tests -v
```

Kết quả hiện tại: **2 kiểm tra đạt** cho Factory.

Mã nguồn: [GitHub - Week-10](https://github.com/dangdoaimo2006-cloud/Week-10).

## Các pattern

- **Đã viết - Factory**: `src/device_factory.py` tạo thiết bị theo tên loại.
- **Có trong UML, chưa code - Singleton**: cấu hình dùng chung.
- **Có trong UML, chưa code - Facade**: gom thao tác thiết bị thành chế độ Đi làm/Đi ngủ.

## Cấu trúc

```text
week10/
├── README.md
├── main.py
├── docs/
│   └── analysis-and-design.md
├── src/
│   ├── __init__.py
│   ├── devices.py
│   └── device_factory.py
└── tests/
    └── test_devices.py
```

## UML

Sơ đồ lớp và trách nhiệm từng lớp nằm tại [`docs/analysis-and-design.md`](docs/analysis-and-design.md).

## Ghi chú thiết kế

- Factory che giấu quyết định chọn lớp cụ thể và chuẩn hóa việc tạo đối tượng. Khi thêm loại mới, factory vẫn cần được cập nhật.
- Singleton dự kiến bảo đảm các lần truy cập cấu hình dùng cùng một đối tượng; trạng thái dùng chung có thể khiến kiểm thử khó cô lập.
- Facade dự kiến gom nhiều lệnh thiết bị thành chế độ. Factory tạo đối tượng, còn Facade phối hợp sử dụng đối tượng.
- Nếu bỏ Facade, client phải tự gọi các thao tác riêng của thiết bị theo đúng thứ tự.

## Giới hạn

Code mới mô phỏng trạng thái trong bộ nhớ, chưa kết nối thiết bị thật. Singleton và Facade mới có trong phần thiết kế, chưa được cài đặt.
