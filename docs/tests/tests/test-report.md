# Test Report - Báo cáo Kết quả Kiểm thử Buổi 14

**Tổng số test case:** 11 | **PASS:** 11 | **FAIL:** 0

| Mã TC | Tiền điều kiện | Các bước thực hiện | Dữ liệu thử | Kết quả mong đợi | Ưu tiên | Kết quả thực tế | P/F |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Hệ thống sẵn sàng | Call POST /api/tickets/ | SĐT: `0912345678`, IMEI: `123456789012345` | Mã HTTP 200/201, trả về mã phiếu mới | Cao | Mã HTTP 200, tạo thành công phiếu | **PASS** |
| **TC-02** | Hệ thống sẵn sàng | Call POST /api/tickets/ | SĐT: `091234567` (9 số - dưới biên) | Mã HTTP 422, thông báo SĐT phải đúng 10 số | Cao | Mã HTTP 422, trả về lỗi validation SĐT | **PASS** |
| **TC-03** | Hệ thống sẵn sàng | Call POST /api/tickets/ | SĐT: `09123456789` (11 số - trên biên) | Mã HTTP 422, thông báo SĐT phải đúng 10 số | Cao | Mã HTTP 422, trả về lỗi validation SĐT | **PASS** |
| **TC-04** | Hệ thống sẵn sàng | Call POST /api/tickets/ | IMEI: `12345678901234` (14 số - dưới biên) | Mã HTTP 422, thông báo IMEI phải đúng 15 số | Cao | Mã HTTP 422, trả về lỗi validation IMEI | **PASS** |
| **TC-05** | Hệ thống sẵn sàng | Call POST /api/tickets/ | IMEI: `1234567890123456` (16 số - trên biên) | Mã HTTP 422, thông báo IMEI phải đúng 15 số | Cao | Mã HTTP 422, trả về lỗi validation IMEI | **PASS** |
| **TC-06** | Thẻ/Mã lỗi rỗng | Call POST /api/tickets/ | Thiếu trường `error_category` | Mã HTTP 422, ghi rõ tên trường bị thiếu | Trung bình | Mã HTTP 422, trả lỗi thiếu trường bắt buộc | **PASS** |
| **TC-07** | Phiếu ID=9999 không tồn tại | Call GET /api/tickets/9999 | ID: `9999` | Mã HTTP 404 Not Found (không trả về 500) | Cao | Mã HTTP 404 với thông báo "Ticket not found" | **PASS** |
| **TC-08** | Không có token / Sai quyền | Call PATCH /api/tickets/1 với token tài khoản khác | User Token A, Ticket thuộc User B | Mã HTTP 403 Forbidden (OWASP A01) | Cao | Mã HTTP 403, không sửa được dữ liệu | **PASS** |
| **TC-09** | CSDL chưa khởi tạo | Chạy lại lệnh seed/migration lần 2 | Data seed mẫu | Migration thành công, không nhân đôi bản ghi | Cao | Đã chạy lại seed, dữ liệu giữ nguyên không bị trùng | **PASS** |
| **TC-10** | Dữ liệu sai định dạng | Truyền chuỗi chữ vào IMEI | IMEI: `"ABCDEFGHIJKLMNO"` | Mã HTTP 422 Unprocessable Entity | Trung bình | Mã HTTP 422, báo lỗi định dạng IMEI | **PASS** |
| **TC-11** | Chạy toàn bộ test | Gõ lệnh `pytest -q` | Tất cả test trong `tests/` | 11/11 tests PASS trong terminal | Cao | 11 passed in 0.42s | **PASS** |

*Ảnh chụp màn hình minh chứng được lưu trữ tại thư mục `docs/screenshots/` (từ `TC-01.png` đến `TC-11.png`).*
