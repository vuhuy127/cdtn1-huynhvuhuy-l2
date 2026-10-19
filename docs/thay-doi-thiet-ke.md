# Tài liệu điều chỉnh thiết kế sau phản hồi Bài tập 1 (BT1)
- **Họ và tên:** Huỳnh Vũ Huy
- **Mã sinh viên:** 2374802010173
- **Lớp:** CNTT05
- **Đề tài:** Luồng L2 - Tiếp nhận và phân loại yêu cầu bảo hành (Smart CRM – Mekong Mobile)

## Danh sách các điểm điều chỉnh (TD-01 đến TD-03)

### TD-01: Bổ sung ràng buộc trạng thái phiếu (Ticket Status)
- **Phản hồi của GV:** Cần làm rõ các mốc chuyển trạng thái của phiếu bảo hành để tránh việc nhảy cóc trạng thái không hợp lệ trong quá trình xử lý.
- **Quyết định:** SỬA. Bổ sung biểu đồ chuyển đổi trạng thái nghiêm ngặt vào tài liệu thiết kế.
- **Lý do:** Đảm bảo tính nhất quán của dữ liệu vòng đời phiếu từ lúc tạo đến khi đóng.
- **Ảnh hưởng:** Cập nhật lại sơ đồ luồng dữ liệu (DFD) và định nghĩa các trường dữ liệu ở bảng `tickets`.

### TD-02: Chuẩn hóa định dạng mã định danh thiết bị (IMEI/Serial)
- **Phản hồi của GV:** Cần quy định rõ kiểu dữ liệu và độ dài của mã IMEI/Serial để tránh lỗi khi tra cứu nhanh.
- **Quyết định:** SỬA. Cố định chiều dài trường IMEI là chuỗi ký tự gồm đúng 15 chữ số.
- **Lý do:** Phù hợp với chuẩn thiết bị thực tế của Mekong Mobile và tối ưu hóa truy vấn index cơ sở dữ liệu.
- **Ảnh hưởng:** Cập nhật DDL của bảng `devices`.

### TD-03: Giữ nguyên phạm vi (Scope) không xử lý thanh toán tự động
- **Phản hồi của GV:** Cần lưu ý không ôm đồm các tính năng ngoài luồng L2.
- **Quyết định:** GIỮ. Giữ nguyên ranh giới tính năng (WON'T scope).
- **Lý do:** Tập trung hoàn toàn vào việc tiếp nhận, phân loại và tính SLA cho phiếu bảo hành trong Sprint này.
- **Ảnh hưởng:** Không có thay đổi về code, giữ nguyên cấu trúc phân rã chức năng.
