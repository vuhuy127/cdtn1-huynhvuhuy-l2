# Ghi nhận thay đổi thiết kế — BT3 / L2

## Mục tiêu

Đồng bộ prototype thực tế với phạm vi API L2 và yêu cầu đóng gói BT3. Tài liệu này mô tả những thay đổi có trong mã nguồn, không khẳng định các chức năng chưa triển khai.

## Thay đổi trong phiên bản BT3

1. Thay `fake_db` trong RAM bằng SQLite để dữ liệu còn sau khi khởi động lại.
2. Hoàn thiện tầng `config`, `repositories`, `services`, `routes`.
3. Thêm kiểm tra định dạng số điện thoại 10 chữ số, IMEI 15 chữ số, danh mục, mức ưu tiên và mô tả.
4. Thêm API xem chi tiết phiếu, cập nhật trạng thái và phân trang danh sách.
5. Thêm `/health`, dữ liệu mẫu khởi tạo lặp an toàn, Dockerfile và Docker Compose healthcheck.
6. Sửa bộ test: payload khớp API và test tạo phiếu chỉ chấp nhận HTTP 201; mở rộng lên 12 test case.
7. Cập nhật API docs, ERD và Deployment Guide theo endpoint và bảng thực tế.

## Phạm vi dữ liệu

Prototype BT3 hiện triển khai một bảng SQLite `tickets`. Đây là mô hình lưu trữ thực tế của phiên bản prototype hiện tại; không thay thế toàn bộ ERD nghiệp vụ tổng thể nếu các tài liệu phân tích trước đó có thêm bảng khách hàng, thiết bị, linh kiện hoặc người dùng.

## Hạn chế còn lại

- Chưa có đăng nhập, JWT, vai trò hoặc phân quyền theo chủ sở hữu phiếu.
- Chưa mã hóa dữ liệu cá nhân trong SQLite.
- Chưa có audit log đã khử dữ liệu cá nhân.
- Chưa chạy quét lỗ hổng dependency.
- Chưa có bằng chứng chạy Docker trên máy trắng trong môi trường build hiện tại.
