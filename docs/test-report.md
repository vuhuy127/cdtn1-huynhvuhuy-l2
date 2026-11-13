# BT3 - Test Report

## 1. Local automated test execution

**Command:** python -m pytest -v

**Platform:** Windows (win32).

**Environment:** Python 3.12.10, Pytest 9.0.2, Pluggy 1.7.0, AnyIO 4.16.0.

**Result:** 12/12 PASS (100%) in 2.29 seconds.

**Warning:** One DeprecationWarning from Starlette TestClient concerning the deprecated anyio.abc.BlockingPortal alias. No test failed.

## 2. GitHub Actions execution

**Verified successful workflow:** https://github.com/vuhuy127/cdtn1-huynhvuhuy-l2/actions/runs/43448579437

| Job | Result | Verification |
|---|---|---|
| test (3.12) | PASS | Dependency install, compileall, 12 Pytest cases |
| test (3.13) | PASS | Dependency install, compileall, 12 Pytest cases |
| docker-smoke | PASS | Docker build, healthcheck healthy, API smoke checks, seed idempotency, ticket persistence after restart |

All three jobs completed successfully on GitHub-hosted runners.

## 3. Test cases

| TC ID | Test type | Preconditions | Steps | Test data | Expected result | Actual result | P/F |
|---|---|---|---|---|---|---|---|
| TC-01 | Happy path | App started | GET / | None | HTTP 200; welcome message | HTTP 200; message returned | PASS |
| TC-02 | Happy path | SQLite initialized | GET /health | None | HTTP 200; DB connected | HTTP 200; DB connected | PASS |
| TC-03 | Happy path | App started | POST valid ticket | Phone 10 digits; IMEI 15 digits; HIGH | HTTP 201; ticket ID and 24-hour SLA | HTTP 201; ID and due date returned | PASS |
| TC-04 | Happy path | Demo seed exists | GET list with limit=1 | limit=1&offset=0 | HTTP 200; one item and pagination metadata | HTTP 200; one item and total returned | PASS |
| TC-05 | Happy path | Demo seed exists | GET detail | TK-DEMO-001 | HTTP 200; matching ticket | HTTP 200; matching ticket | PASS |
| TC-06 | Happy path | Demo seed exists | PATCH status | HOÀN TẤT | HTTP 200; status updated | HTTP 200; status updated | PASS |
| TC-07 | Boundary | App started | POST with 9-digit phone | 090123456 | HTTP 422 | HTTP 422 | PASS |
| TC-08 | Boundary | App started | POST with 11-digit phone | 09012345678 | HTTP 422 | HTTP 422 | PASS |
| TC-09 | Boundary | App started | POST with 14-digit IMEI | 12345678901234 | HTTP 422 | HTTP 422 | PASS |
| TC-10 | Invalid data | App started | POST unsupported priority | ROOT | HTTP 422; value not echoed | HTTP 422; value not echoed | PASS |
| TC-11 | Security | SQLite initialized | POST SQL-like description; retrieve ticket | '; DROP TABLE tickets; -- | Text stored literally; table remains available | HTTP 201; text retrieved; list still works | PASS |
| TC-12 | Reproducibility | Demo seed initialized | Run seed twice | Same two demo IDs | Row count unchanged | Count remains 2 | PASS |

## 4. Docker smoke test result

On the GitHub-hosted runner, Docker Compose built and started the app. The workflow asserted Docker health status healthy, called GET /, GET /health, GET /api/tickets/ and GET /api/tickets/TK-DEMO-001, seeded demo data twice and verified that the ticket count stayed at 2, created a ticket, updated a status, restarted the app and retrieved the created ticket again.

All steps passed.

## 5. Remaining local evidence

The code and Docker workflow are verified in GitHub CI. The student's separate Windows clean-folder clone of the final public tag and genuine local screenshots for the PDF are still required.

Do not present CI logs as screenshots from the student's personal machine.
