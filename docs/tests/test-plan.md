# Test Plan - Phân hệ Mekong Mobile Smart CRM (L2)

## 1. Phạm vi kiểm thử (Scope)
* **Chức năng kiểm thử:**
  * Endpoint tiếp nhận phiếu bảo hành `POST /api/tickets/`.
  * Endpoint tra cứu phiếu bảo hành `GET /api/tickets/{ticket_id}`.
  * Validation định dạng số điện thoại (10 chữ số) và mã IMEI (15 chữ số).
  * Quy tắc nghiệp vụ kiểm tra trạng thái phiếu trùng và phân loại danh mục lỗi.
* **Chủ ý KHÔNG kiểm thử:**
  * Giao diện người dùng (UI Frontend): Chưa phát triển ở giai đoạn này.
  * Kiểm thử hiệu năng và chịu tải (Performance/Load testing): Thuộc phạm vi Chuyên đề tốt nghiệp 2.

## 2. Phân bổ loại test và Kỹ thuật chọn dữ liệu
* **Tổng số test case:** 11 test case.
* **Phân bổ tầng kiểm thử:** 7 Unit tests (FastAPI logic), 2 Integration tests (Service + DB/Fixtures), 2 API/End-to-End tests (TestClient).
* **Kỹ thuật chọn dữ liệu:** Phân vùng tương đương (Equivalence Partitioning) và Giá trị biên (Boundary Value Analysis) cho độ dài SĐT (9, 10, 11 số) và IMEI (14, 15, 16 số).
* **Đảm bảo đủ 5 loại test:** Luồng đúng (Happy path), Giá trị biên (Boundary), Dữ liệu sai (Invalid data), Bảo mật (Security A01), Tính tái lập (Reproducibility).

## 3. Tiêu chí thành công (Success Criteria)
* 100% test case trong Test Report có kết quả thực tế và ảnh chụp minh chứng.
* Bộ kiểm thử đạt PASS 100% bằng một lệnh chạy `pytest -q`.
* Không còn bug mức độ Critical đang mở.

## 4. Môi trường và Dữ liệu thử
* **Môi trường:** Python 3.11+, FastAPI TestClient, Pytest.
* **Dữ liệu thử:** Sử dụng Pytest Fixtures (`conftest.py`) và tệp seed dữ liệu sạch để khởi tạo lại trạng thái trước mỗi lần chạy test.
