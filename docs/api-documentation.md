# API Documentation — Mekong Mobile Smart CRM L2

Base URL: `http://localhost:8000`  
Interactive schema: `/docs`  
Content type: `application/json`  
Authentication: **Not implemented** in this academic prototype. Do not expose the API to real customer data.

## 1. GET `/`

- **Purpose:** Return the API welcome/status message.
- **Authentication:** None.
- **Path/query parameters:** None.
- **Request body:** None.
- **Success:** `200 OK`.
- **Errors:** No application-specific error response is defined.
- **Example response:**

```json
{"message":"Mekong Mobile Smart CRM - L2 API is running"}
```

## 2. GET `/health`

- **Purpose:** Check application and SQLite connectivity.
- **Authentication:** None.
- **Path/query parameters:** None.
- **Request body:** None.
- **Success:** `200 OK` when SQLite is reachable.
- **Errors:** `503 Service Unavailable` when the database cannot be reached.
- **Example response:**

```json
{"status":"healthy","database":"connected"}
```

## 3. POST `/api/tickets/`

- **Purpose:** Create a warranty intake ticket.
- **Authentication:** None; authorization is not implemented.
- **Path/query parameters:** None.
- **Request body:**

```json
{
  "customer_phone": "0901234567",
  "imei": "123456789012345",
  "issue_category": "MAN_HINH",
  "description": "Screen shows vertical lines after impact",
  "priority": "HIGH"
}
```

- **Validation:** Phone must contain exactly 10 digits; IMEI exactly 15 digits; category must be `MAN_HINH`, `PIN`, `SAC`, or `PHAN_MEM`; priority must be `LOW`, `MEDIUM`, `HIGH`, or `URGENT`; description length is 5–1000 characters.
- **Success:** `201 Created`; response contains `message` and `data` with the ticket ID, submitted fields, status, creation time, and SLA due date.
- **Errors:** `422 Unprocessable Entity` for invalid or missing fields.
- **SLA:** LOW 72 hours; MEDIUM 48 hours; HIGH 24 hours; URGENT 12 hours.

## 4. GET `/api/tickets/`

- **Purpose:** List tickets.
- **Authentication:** None; authorization is not implemented.
- **Query parameters:** `limit` integer 1–100 (default 20); `offset` integer ≥ 0 (default 0).
- **Request body:** None.
- **Success:** `200 OK`; response contains `items`, `total`, `limit`, and `offset`.
- **Errors:** `422 Unprocessable Entity` when pagination parameters are invalid.
- **Example:** `GET /api/tickets/?limit=20&offset=0`.

## 5. GET `/api/tickets/{ticket_id}`

- **Purpose:** Retrieve one ticket by its ID.
- **Authentication:** None; authorization is not implemented.
- **Path parameter:** `ticket_id` string, e.g. `TK-DEMO-001`.
- **Request body:** None.
- **Success:** `200 OK`, response contains `data`.
- **Errors:** `404 Not Found` with `{"detail":"Ticket not found"}`.

## 6. PATCH `/api/tickets/{ticket_id}/status`

- **Purpose:** Update a ticket's status.
- **Authentication:** None; authorization is not implemented.
- **Path parameter:** `ticket_id` string.
- **Request body:** `{"status":"ĐANG XỬ LÝ"}`. Allowed values: `MỚI`, `ĐANG XỬ LÝ`, `HOÀN TẤT`, `ĐÃ HỦY`.
- **Success:** `200 OK`; response contains updated ticket data.
- **Errors:** `404 Not Found` for unknown ID; `422 Unprocessable Entity` for invalid status.

## Error response format

Validation errors use HTTP 422 and return `detail` entries containing `loc`, `msg`, and `type`. Submitted values are omitted from the response to avoid echoing phone numbers or IMEIs. Unknown ticket IDs return HTTP 404.