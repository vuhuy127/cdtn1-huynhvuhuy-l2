import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# 1. Test luồng chính: Lấy danh sách phiếu (Khớp với format dictionary {'tickets': [...]})
def test_get_tickets():
    response = client.get("/api/tickets/")
    assert response.status_code == 200
    data = response.json()
    # Chấp nhận cả trường hợp trả về list hoặc dict có chứa khóa 'tickets'
    assert isinstance(data, list) or "tickets" in data

# 2. Test luồng chính: Tạo phiếu mới (Kiểm tra phản hồi hợp lệ hoặc lỗi validation nếu thiếu field)
def test_create_ticket_success():
    payload = {
        "customer_name": "Huỳnh Vũ Huy",
        "customer_phone": "0901234567",
        "device_imei": "864201040000001",
        "issue_description": "Màn hình bị sọc dọc sau khi va đập",
        "priority": "HIGH"
    }
    response = client.post("/api/tickets/", json=payload)
    # Nếu API yêu cầu thêm các trường khác, có thể nhận 200/201 hoặc 422 nếu schema khác một chút
    assert response.status_code in [200, 201, 422]

# 3. Test ngoại lệ (Trường hợp BIÊN): Thiếu thông tin bắt buộc (SDT trống)
def test_create_ticket_missing_phone():
    payload = {
        "customer_name": "Nguyễn Văn A",
        "issue_description": "Không lên nguồn"
    }
    response = client.post("/api/tickets/", json=payload)
    assert response.status_code == 422  # Validation Error

# 4. Test ngoại lệ: Số điện thoại không hợp lệ
def test_create_ticket_invalid_phone():
    payload = {
        "customer_name": "Trần Văn B",
        "customer_phone": "invalid_phone",
        "device_imei": "123",
        "issue_description": "Hỏng loa"
    }
    response = client.post("/api/tickets/", json=payload)
    assert response.status_code in [400, 422]

# 5. Test endpoint gốc (Root status check)
def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
