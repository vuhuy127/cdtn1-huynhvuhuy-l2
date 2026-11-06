# Tài liệu điều chỉnh thiết kế sau phản hồi Bài tập 1 (BT1)
- **Họ và tên:** Huỳnh Vũ Huy
- **Mã sinh viên:** 2374802010173
- **Lớp:** CNTT05
- **Đề tài:** Luồng L2 - Tiếp nhận và phân loại yêu cầu bảo hành (Smart CRM – Mekong Mobile)

---

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

# Giải trình phản hồi Bài tập 2 & Quyết định xử lý kỹ thuật

## 1. Bảng giải trình phản hồi từ Giảng viên

| Nội dung nhận xét / Hạn chế BT2 | Quyết định xử lý kỹ thuật | Trạng thái |
| :--- | :--- | :--- |
| **1. Mã nguồn ít, mới có 3 endpoint, chưa đủ CRUD (S1)** | Quy hoạch rõ phạm vi prototype L2 tập trung vào các quy tắc nghiệp vụ cốt lõi (tạo phiếu, validation, kiểm tra bảo hành). Các endpoint bổ trợ khác sẽ được đưa vào phạm vi giới hạn của bài tập. | Đã ghi nhận |
| **2. Chưa có migration và seed dữ liệu (S3)** | Tạo thư mục `seeds/` chứa các câu lệnh/dữ liệu mẫu để phục vụ khởi tạo cơ sở dữ liệu sạch khi chạy test tự động. | Đã khắc phục |
| **3. Chưa có giao diện 3 màn hình và 3 trạng thái (S4)** | Ghi rõ trong tài liệu: Hệ thống tập trung hoàn thiện API Backend (FastAPI) chuẩn RESTful và kiểm thử qua Swagger UI / Pytest. Phần UI sẽ hoàn thiện ở mốc sau. | Đã ghi nhận |
| **4. Tệp requirements.txt chưa khóa phiên bản (C6)** | Cập nhật tệp `requirements.txt`, cố định phiên bản cho toàn bộ thư viện bằng dấu `==` (vd: `fastapi==0.110.0`, `pytest==8.0.0`). | Đã khắc phục |
| **5. Thiếu docs/ai-disclosure.md, README ngắn** | Bổ sung tệp `docs/ai-disclosure.md` (khai báo sử dụng AI) và viết lại tệp `README.md` với đầy đủ hướng dẫn thiết lập môi trường, chạy test. | Đã khắc phục |

---
