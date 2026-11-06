# Bug Log - Nhật ký Gỡ lỗi Dự án

## BUG-01 · Major · Lỗi thiếu khóa cứng phiên bản thư viện trong requirements.txt
1. **Mã và mức độ:** BUG-01 · MAJOR · Ảnh hưởng đến tính tái lập môi trường (Tiêu chí C6).
2. **Phát hiện bởi:** Nhận xét phản hồi Bài tập 2 của Giảng viên.
3. **Triệu chứng:** Tệp `requirements.txt` sử dụng tên thư viện tự do không ghi kèm phiên bản cố định (`==`), dẫn đến nguy cơ xung đột khi dựng lại trên máy khác.
4. **Cách tái lập:** Clone repo trên môi trường máy sạch và chạy `pip install -r requirements.txt`.
5. **Nguyên nhân:** Khởi tạo file requirements tự động bằng `pip freeze` nhưng thiếu tham số chốt phiên bản cụ thể.
6. **Cách sửa:** Khóa cố định phiên bản các thư viện chính (FastAPI, Pytest, Uvicorn, Pydantic) trong tệp `requirements.txt`.
7. **Commit và xác nhận:** https://github.com/vuhuy127/cdtn1-huynhvuhuy-l2/commit/38c625d2d65a0a8061ee519dee047818c5d4f3c9 — Đã kiểm tra lại tính tương thích: PASS.

---

## BUG-02 · Critical · Lỗi trả về mã lỗi 500 khi tra cứu ID phiếu không tồn tại (OWASP A02)
1. **Mã và mức độ:** BUG-02 · CRITICAL · Lỗi hệ thống để lộ vết ngăn xếp/lỗi kỹ thuật (500 Internal Server Error).
2. **Phát hiện bởi:** TC-07 (Kiểm thử tra cứu ID không tồn tại).
3. **Triệu chứng:** Gọi `GET /api/tickets/9999` trả về mã HTTP 500 thay vì mã 404.
4. **Cách tái lập:** Gửi request GET tới endpoint phiếu bảo hành với một ID ngẫu nhiên không có trong CSDL.
5. **Nguyên nhân:** Hàm xử lý ở tầng Service không kiểm tra kết quả `None` trước khi trả về response nên gây ra exception unhandled.
6. **Cách sửa:** Bổ sung khối kiểm tra `if not ticket: raise HTTPException(status_code=404, detail="Ticket not found")` tại route handler.
7. **Commit và xác nhận:** https://github.com/vuhuy127/cdtn1-huynhvuhuy-l2/commit/4e8a1d2 — Chạy lại TC-07 trả về mã HTTP 404: PASS.

---

## BUG-03 · Minor · Lỗi thiếu validate ký tự đặc biệt trong IMEI
1. **Mã và mức độ:** BUG-03 · MINOR · Lỗi dữ liệu sai định dạng đầu vào.
2. **Phát hiện bởi:** TC-10 (Kiểm thử định dạng chuỗi IMEI).
3. **Triệu chứng:** Chuỗi IMEI chứa 15 ký tự chữ cái vẫn vượt qua bộ lọc validation.
4. **Cách tái lập:** Nhập IMEI là `"ABCDEFGHIJKLMNO"` khi gọi tạo phiếu.
5. **Nguyên nhân:** Pydantic regex schema chỉ kiểm tra độ dài `min_length=15, max_length=15` mà thiếu biểu thức chính quy kiểm tra chữ số `^\d{15}$`.
6. **Cách sửa:** Cập nhật regex pattern cho trường IMEI thành `Field(..., regex=r"^\d{15}$")`.
7. **Commit và xác nhận:** https://github.com/vuhuy127/cdtn1-huynhvuhuy-l2/commit/7c3f2b1 — Chạy lại TC-10 trả về mã 422: PASS.
