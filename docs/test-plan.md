# TP1 — Test Plan

## 1. Scope

Test the implemented L2 FastAPI prototype: root and health endpoints; ticket creation, listing, detail retrieval, and status update; input validation; parameterized SQLite persistence; and repeatable sample-data initialization.

Out of scope: frontend/UI, login and role-based authorization, production deployment, load testing, penetration testing, and encryption-at-rest verification. These are not implemented in this prototype.

## 2. Test types and techniques

The test set contains 12 cases across five required types:

| Test type | Cases | Technique |
|---|---|---|
| Happy path | TC-01–TC-06 | Valid request / expected response |
| Boundary | TC-07–TC-09 | Boundary Value Analysis for 10-digit phone and 15-digit IMEI |
| Invalid data | TC-10 | Invalid enumeration value |
| Security | TC-11 | SQL-like payload; verify parameterized query treats input as data |
| Reproducibility | TC-12 | Execute seed repeatedly and compare row count |

## 3. Entry, exit, and success criteria

- Entry: Python 3.12+ and dependencies from `requirements.txt` are installed.
- Execute: `python -m pytest -q`.
- Exit: all 12 test cases pass; no Critical bug remains open in the implemented scope.
- Every reported result must correspond to an executed test. Docker white-box testing is recorded separately and is not claimed until run on a Docker-capable clean machine.

## 4. Environment and test data

- Runtime: Python 3.13.5 in the current verification environment; CI is configured for Python 3.12 and 3.13.
- Framework: FastAPI TestClient, HTTPX, Pytest.
- Database: isolated temporary SQLite file per test.
- Demo data: two synthetic tickets, inserted with `INSERT OR IGNORE`.
- Personal data: only synthetic phone and IMEI values are used.