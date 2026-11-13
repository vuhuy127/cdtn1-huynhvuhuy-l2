# API Documentation — Mekong Mobile Smart CRM L2

Base URL: http://localhost:8000
Interactive schema: http://localhost:8000/docs
Content type: application/json
Authentication: not implemented. All endpoints are currently public and must not be exposed to real customer data.

**Evidence:** The success-response examples below were copied from the Docker smoke-test execution on the GitHub-hosted runner (workflow run 43426101102, 13 November 2026). Phone numbers and IMEIs shown are synthetic demo values.

## 1. GET /

### 1. Method and path
GET /

### 2. Business description
Returns a simple status message confirming that the L2 API process is responding.

### 3. Authentication and permissions
No authentication or role-based permissions are implemented.

### 4. Request parameters and body
No path parameters, query parameters, or request body.
Actual request: GET http://localhost:8000/

### 5. Successful response body
HTTP 200 OK — actual response:

~~~json
{"message":"Mekong Mobile Smart CRM - L2 API is running"}
~~~

### 6. Possible error codes
- 500 Internal Server Error: unexpected server-side exception; no custom business error is defined for this endpoint.

### 7. Limitations and special behavior
This endpoint checks API reachability only. It does not verify database readiness; use GET /health for that purpose.

## 2. GET /health

### 1. Method and path
GET /health

### 2. Business description
Checks whether the application can open its configured SQLite database.

### 3. Authentication and permissions
No authentication or role-based permissions are implemented.

### 4. Request parameters and body
No path parameters, query parameters, or request body.
Actual request: GET http://localhost:8000/health

### 5. Successful response body
HTTP 200 OK — actual response:

~~~json
{"status":"healthy","database":"connected"}
~~~

### 6. Possible error codes
- 503 Service Unavailable: the database connection/check failed; response body is {"status":"unhealthy","database":"unavailable"}.

### 7. Limitations and special behavior
This endpoint checks database connectivity, not application authorization or the availability of external services. Docker uses this endpoint for its healthcheck.

## 3. POST /api/tickets/

### 1. Method and path
POST /api/tickets/

### 2. Business description
Accepts a warranty request, validates the supplied customer/device fields, creates a ticket and calculates its SLA due date from priority.

### 3. Authentication and permissions
No token or role is required because authentication and authorization are not implemented in the current prototype. This is a development limitation, not a recommendation for production.

### 4. Request parameters and body
No path or query parameters. Content-Type: application/json.

| Field | Type | Required | Constraint / allowed values |
|---|---|---|---|
| customer_phone | string | Yes | Exactly 10 digits |
| imei | string | Yes | Exactly 15 digits |
| issue_category | string | Yes | MAN_HINH, PIN, SAC, PHAN_MEM |
| description | string | Yes | 5–1000 characters; must not be blank |
| priority | string | No | LOW, MEDIUM, HIGH, URGENT; default MEDIUM |

Actual request body used by the CI smoke test:

~~~json
{
  "customer_phone": "0901234567",
  "imei": "123456789012345",
  "issue_category": "MAN_HINH",
  "description": "CI documentation example ticket",
  "priority": "HIGH"
}
~~~

### 5. Successful response body
HTTP 201 Created — actual response from the same CI execution:

~~~json
{
  "message": "Ticket created successfully",
  "data": {
    "ticket_id": "TK-88C38545A2",
    "customer_phone": "0901234567",
    "imei": "123456789012345",
    "issue_category": "MAN_HINH",
    "description": "CI documentation example ticket",
    "priority": "HIGH",
    "status": "MỚI",
    "created_at": "2026-11-13T12:33:20.740673+00:00",
    "due_date": "2026-11-14T12:33:20.740673+00:00"
  }
}
~~~

### 6. Possible error codes
- 422 Unprocessable Entity: required field missing, unexpected field, invalid phone/IMEI format, unsupported category/priority, or invalid description.

### 7. Limitations and special behavior
SLA durations: LOW 72 hours, MEDIUM 48 hours, HIGH 24 hours and URGENT 12 hours. New tickets start with status MỚI. The API currently returns phone and IMEI values in ticket responses; use synthetic data only.

## 4. GET /api/tickets/

### 1. Method and path
GET /api/tickets/

### 2. Business description
Returns a page of warranty tickets together with total count and pagination metadata.

### 3. Authentication and permissions
No authentication or role-based permissions are implemented.

### 4. Request parameters and body
No request body.

| Query parameter | Type | Required | Constraint / default |
|---|---|---|---|
| limit | integer | No | 1–100; default 20 |
| offset | integer | No | Must be >= 0; default 0 |

Actual request: GET http://localhost:8000/api/tickets/

### 5. Successful response body
HTTP 200 OK — actual response from the CI runner (timestamps are UTC):

~~~json
{
  "items": [
    {
      "ticket_id": "TK-DEMO-001",
      "customer_phone": "0912345678",
      "imei": "123456789012345",
      "issue_category": "MAN_HINH",
      "description": "Demo ticket: screen has vertical lines",
      "priority": "HIGH",
      "status": "MỚI",
      "created_at": "2026-11-13T12:33:14.637750+00:00",
      "due_date": "2026-11-14T12:33:14.637750+00:00"
    },
    {
      "ticket_id": "TK-DEMO-002",
      "customer_phone": "0987654321",
      "imei": "543210987654321",
      "issue_category": "PIN",
      "description": "Demo ticket: battery drains quickly",
      "priority": "MEDIUM",
      "status": "ĐANG XỬ LÝ",
      "created_at": "2026-11-13T12:33:14.637750+00:00",
      "due_date": "2026-11-15T12:33:14.637750+00:00"
    }
  ],
  "total": 2,
  "limit": 20,
  "offset": 0
}
~~~

### 6. Possible error codes
- 422 Unprocessable Entity: limit or offset is outside the allowed range or cannot be parsed as an integer.

### 7. Limitations and special behavior
Results are ordered by created_at descending. This endpoint currently has no filtering, sorting option or access control.

## 5. GET /api/tickets/{ticket_id}

### 1. Method and path
GET /api/tickets/{ticket_id}

### 2. Business description
Returns one warranty ticket selected by its ticket identifier.

### 3. Authentication and permissions
No authentication or ownership-based authorization is implemented.

### 4. Request parameters and body
Path parameter ticket_id (string) is required. No query parameter or request body.
Actual request: GET http://localhost:8000/api/tickets/TK-DEMO-001

### 5. Successful response body
HTTP 200 OK — actual response:

~~~json
{
  "data": {
    "ticket_id": "TK-DEMO-001",
    "customer_phone": "0912345678",
    "imei": "123456789012345",
    "issue_category": "MAN_HINH",
    "description": "Demo ticket: screen has vertical lines",
    "priority": "HIGH",
    "status": "MỚI",
    "created_at": "2026-11-13T12:33:14.637750+00:00",
    "due_date": "2026-11-14T12:33:14.637750+00:00"
  }
}
~~~

### 6. Possible error codes
- 404 Not Found: no ticket matches the supplied ID; response body: {"detail":"Ticket not found"}.

### 7. Limitations and special behavior
The endpoint returns the current stored fields, including phone and IMEI. The prototype does not restrict access by customer or employee identity.

## 6. PATCH /api/tickets/{ticket_id}/status

### 1. Method and path
PATCH /api/tickets/{ticket_id}/status

### 2. Business description
Changes the status of an existing warranty ticket.

### 3. Authentication and permissions
No authentication or role-based permissions are implemented.

### 4. Request parameters and body
Path parameter ticket_id (string) is required. Content-Type: application/json. No query parameters.

| Field | Type | Required | Allowed values |
|---|---|---|---|
| status | string | Yes | MỚI, ĐANG XỬ LÝ, HOÀN TẤT, ĐÃ HỦY |

Actual request used by the CI smoke test:

~~~http
PATCH /api/tickets/TK-DEMO-001/status
Content-Type: application/json

{"status":"HOÀN TẤT"}
~~~

### 5. Successful response body
HTTP 200 OK — actual response:

~~~json
{
  "message": "Ticket status updated",
  "data": {
    "ticket_id": "TK-DEMO-001",
    "customer_phone": "0912345678",
    "imei": "123456789012345",
    "issue_category": "MAN_HINH",
    "description": "Demo ticket: screen has vertical lines",
    "priority": "HIGH",
    "status": "HOÀN TẤT",
    "created_at": "2026-11-13T12:33:14.637750+00:00",
    "due_date": "2026-11-14T12:33:14.637750+00:00"
  }
}
~~~

### 6. Possible error codes
- 404 Not Found: the ticket ID does not exist.
- 422 Unprocessable Entity: missing status field or unsupported status value.

### 7. Limitations and special behavior
This endpoint validates the status value but does not enforce a business transition matrix (for example, it does not prevent moving a completed ticket back to MỚI). Status history/audit trail is not implemented.

## Common validation error format

Validation failures use HTTP 422 and return a detail array containing loc, msg and type. Submitted field values are omitted from the custom validation response to avoid echoing phone numbers or IMEIs.

## Authentication and deployment security note

Authentication, JWT, roles, owner-level access control, CORS allowlisting and HTTPS termination are not implemented in the current prototype. The local Docker endpoint uses HTTP. For a real deployment, place the application behind a TLS-enabled reverse proxy or a managed HTTPS platform, and implement authorization before processing real customer information.
