# TP2 — Test Report

**Execution command:** `python -m pytest -q`  
**Execution environment:** Python 3.13.5, FastAPI 0.128.2, Pydantic 2.13.5, Pytest 9.0.2, HTTPX 0.28.1  
**Result:** 12/12 PASS (100%) — executed locally in the assistant build workspace. GitHub Actions results for the new branch are pending until GitHub finishes the workflow.

| TC ID | Test type | Preconditions | Steps | Test data | Expected result | Actual result | P/F |
|---|---|---|---|---|---|---|---|
| TC-01 | Happy path | App started | GET `/` | None | HTTP 200; welcome message | HTTP 200; message returned | PASS |
| TC-02 | Happy path | SQLite initialized | GET `/health` | None | HTTP 200; DB connected | HTTP 200; DB connected | PASS |
| TC-03 | Happy path | App started | POST valid ticket | Phone 10 digits; IMEI 15 digits; HIGH | HTTP 201; ticket ID and 24-hour SLA | HTTP 201; ID and due date returned | PASS |
| TC-04 | Happy path | Demo seed exists | GET list with limit=1 | `limit=1&offset=0` | HTTP 200; one item and pagination metadata | HTTP 200; one item and total returned | PASS |
| TC-05 | Happy path | Demo seed exists | GET detail | `TK-DEMO-001` | HTTP 200; matching ticket | HTTP 200; matching ticket | PASS |
| TC-06 | Happy path | Demo seed exists | PATCH status | `HOÀN TẤT` | HTTP 200; status updated | HTTP 200; status updated | PASS |
| TC-07 | Boundary | App started | POST with 9-digit phone | `090123456` | HTTP 422 | HTTP 422 | PASS |
| TC-08 | Boundary | App started | POST with 11-digit phone | `09012345678` | HTTP 422 | HTTP 422 | PASS |
| TC-09 | Boundary | App started | POST with 14-digit IMEI | `12345678901234` | HTTP 422 | HTTP 422 | PASS |
| TC-10 | Invalid data | App started | POST unsupported priority | `ROOT` | HTTP 422; value not echoed | HTTP 422; value not echoed | PASS |
| TC-11 | Security | SQLite initialized | POST SQL-like description; retrieve ticket | `'; DROP TABLE tickets; --` | Text stored literally; table remains available | HTTP 201; text retrieved; list still works | PASS |
| TC-12 | Reproducibility | Demo seed initialized | Run seed twice | Same two demo IDs | Row count unchanged | Count remains 2 | PASS |

## Evidence limitation

The 12 API/persistence tests above were executed in the local build workspace and passed. Docker is not installed in that environment, so the following required workshop evidence has **not** been captured or claimed: `docker compose ps` showing `healthy`, a clean-machine clone by tag `v1.0`, and the second Docker startup/volume check. Add genuine screenshots from a Docker-capable machine to `docs/screenshots/` before final submission.