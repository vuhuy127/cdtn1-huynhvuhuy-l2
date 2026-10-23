import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# 1. Test luồng chính: Lấy danh sách phiếu
def test_get_tickets():
    response = client.get("/api/tickets/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# 2. Test luồng chính: Tạo phiếu mới thành công
def test_create_ticket_success():
    payload = {
        "customer_name": "Huỳnh Vũ Huy",
        "customer_phone": "0901234567",
        "device_imei": "864201040000001",
        "issue_description": "Màn hình bị sọc dọc sau khi va đập",
        "priority": "HIGH"
    }
    response = client.post("/api/tickets/", json=payload)
    assert response.status_code in [200, 201]
    assert "ticket_id" in response.json() or "id" in response.json()

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
    assert "message" in response.json()
