# Lab 10 - Smart Home Mini

**Sinh viên:** Nguyễn Hải Đăng  
**MSSV:** 202418863

Chương trình Python mô phỏng một số thiết bị trong nhà thông minh: đèn, quạt và cửa. Bài tập sử dụng Factory để tạo thiết bị, Singleton để giữ cấu hình chung và Facade để gom thao tác thường dùng.

## Chức năng

- Bật/tắt đèn và quạt.
- Khóa/mở khóa cửa.
- Tạo thiết bị theo loại `light`, `fan` hoặc `door`.
- Lấy cấu hình nhà với cùng một đối tượng `HomeConfiguration`.
- Chọn chế độ Đi làm hoặc Đi ngủ qua `SmartHomeFacade`.

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
│   ├── home_configuration.py
│   └── smart_home_facade.py
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

Kết quả chạy: **5 kiểm tra thành công**.

## Thiết kế

- `IDevice` định nghĩa thao tác bật và tắt thiết bị.
- `ILockable` bổ sung thao tác khóa và mở khóa cho cửa.
- `DeviceFactory` chọn lớp thiết bị dựa trên loại đầu vào.
- `HomeConfiguration` giữ tên nhà và mức sáng ban đêm dùng chung.
- `SmartHomeFacade` gọi nhiều thiết bị theo chế độ Đi làm/Đi ngủ.
- UML lớp và phân tích thiết kế nằm trong [`docs/analysis-and-design.md`](docs/analysis-and-design.md).

## Câu hỏi phân tích

1. **Factory che giấu điều gì?** Nó che giấu việc chọn lớp cụ thể và gọi constructor tương ứng. Client chỉ truyền loại và tên thiết bị vào `DeviceFactory.create()`.
2. **Khi thêm `SmartCamera`, cần sửa thành phần nào?** Tạo lớp `SmartCamera` và thêm loại `camera` vào `DeviceFactory`. Nếu camera tham gia các chế độ nhà, cần cập nhật cả `SmartHomeFacade`.
3. **Singleton constructor nên có mức truy cập nào?** Trong C#, constructor thường để `private` để chỉ lớp Singleton tạo instance. Python không có constructor private tuyệt đối; ở đây `__new__` kiểm soát việc tạo instance.
4. **Vì sao Singleton thường là `sealed`?** Để lớp con không thay đổi cách tạo instance hoặc tạo một instance khác. Trong Python, `HomeConfiguration` chặn kế thừa bằng `__init_subclass__`.
5. **Singleton gây khó khăn gì cho unit test?** Trạng thái dùng chung có thể còn lại giữa các test, khiến thứ tự chạy ảnh hưởng kết quả. Test cần khôi phục cấu hình sau khi thay đổi.
6. **Nếu dùng DI với lifetime `AddSingleton`, có cần tự cài Singleton không?** Thường không. DI container đã quản lý vòng đời và cấp cùng một instance, đồng thời dễ thay thế dependency khi kiểm thử.
7. **Factory đang che giấu quyết định thiết kế nào?** Quyết định ánh xạ một chuỗi loại như `light` sang lớp cụ thể như `SmartLight` và cách khởi tạo lớp đó.
8. **Singleton bảo đảm điều gì và tạo rủi ro nào?** Nó bảo đảm các phần dùng chung một đối tượng cấu hình; đổi lại, trạng thái toàn cục làm giảm tính độc lập giữa các lần chạy và kiểm thử.
9. **Facade khác Factory thế nào?** Factory tạo đối tượng phù hợp; Facade phối hợp các đối tượng và cung cấp một thao tác mức cao.
10. **Bỏ Facade thì client phải biết thêm gì?** Client phải giữ tham chiếu đến từng thiết bị, biết thứ tự bật/tắt/khóa cho mỗi chế độ và tự lấy mức sáng ban đêm từ cấu hình.

Mã nguồn: [GitHub - Week-10](https://github.com/dangdoaimo2006-cloud/Week-10).
