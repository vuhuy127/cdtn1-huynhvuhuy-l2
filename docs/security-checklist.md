# TP5 — Security Checklist

| # | Required check | Status | Evidence / reason |
|---|---|---|---|
| 1 | No secrets in repository; `.env` excluded | **ĐÃ LÀM** | `.gitignore` excludes `.env`; `.env.example` contains only the host port; `.dockerignore` excludes `.env`. Recheck `git log --all -- .env` before public release. |
| 2 | Application-level input validation | **ĐÃ LÀM** | `src/routes/ticket_router.py`: phone and IMEI patterns, category/priority Literal values, description length; TC-07–TC-10. |
| 3 | Access control: users can only read/update their own data | **CHƯA LÀM** | No login, token, user ownership, or authorization policy is implemented. Do not expose this prototype to real customers. |
| 4 | Passwords / sensitive data hashed or encrypted | **CHƯA LÀM** | The prototype does not store passwords, but customer phone and IMEI are stored as plain SQLite values; encryption-at-rest is not implemented. |
| 5 | Error messages do not expose stack traces, table names, or connection strings | **ĐÃ LÀM** | 404 returns `Ticket not found`; validation handler omits submitted input; TC-10 and TC-11. Unexpected production exceptions still require deployment-level monitoring. |
| 6 | Logs do not contain passwords, tokens, or unnecessary personal data | **CHƯA LÀM** | No explicit redacted audit-logging policy or log review is implemented. Avoid enabling request-body logging. |
| 7 | Dependencies pinned and basic vulnerability checks performed | **CHƯA LÀM** | All direct dependencies are pinned in `requirements.txt`; automated vulnerability scanning has not yet been run, so the combined requirement is not claimed as complete. |

**Scope note:** This is a student prototype, not a production-ready service. Authentication, authorization, encryption of personal data, audit logging, and dependency vulnerability scanning remain release blockers for real customer data.