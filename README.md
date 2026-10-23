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
## 3. Hướng dẫn cài đặt và khởi chạy dự án

- Bước 1: Clone kho lưu trữ
  `git clone https://github.com/vuhuy127/cdtn1-huynhvuhuy-l2.git`
- Bước 2: Di chuyển vào thư mục dự án
  `cd cdtn1-huynhvuhuy-l2`
- Bước 3: Tạo môi trường ảo Python
  `python -m venv venv`
- Bước 4: Kích hoạt môi trường ảo (PowerShell)
  `.\venv\Scripts\Activate.ps1`
- Bước 5: Cài đặt các thư viện phụ thuộc
  `python -m pip install -r requirements.txt`
- Bước 6: Chạy kiểm thử tự động (Unit Tests)
  `pytest -v`
- Bước 7: Khởi chạy ứng dụng
  `python -m uvicorn src.main:app --reload`
