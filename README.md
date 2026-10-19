## 2. Yêu cầu môi trường (Environment Setup)
- Ngôn ngữ: Python 3.10+
- Framework: FastAPI, Uvicorn
- Thư viện hỗ trợ: Pydantic, Pytest
- Cơ sở dữ liệu: SQLite (Phục vụ phát triển cục bộ Sprint 1) / PostgreSQL (Dự kiến cho môi trường Production)

## 6. Trạng thái hiện tại (Current Status - Sprint 1)
- Đã hoàn thành cấu trúc thư mục kiến trúc phân lớp (`src/config`, `src/models`, `src/services`, `src/routes`).
- Đã hiện thực logic khởi tạo phiếu bảo hành (`Ticket`), tự động tính toán thời hạn cam kết (SLA) dựa trên mức độ ưu tiên.
- Đã hoàn thành các endpoint API cơ bản (Tạo phiếu, tra cứu danh sách và chi tiết phiếu).
- Đã tích hợp ghi nhận tài liệu điều chỉnh thiết kế theo phản hồi Bài tập 1 tại `docs/thay-doi-thiet-ke.md`.
