# TP3 — Bug Log

The three issues below were identified during the repository audit and corrected in the BT3 implementation. The fix commit URL is added after the GitHub commit is created.

## BUG-01 — MAJOR — Ticket data was volatile

1. **ID / Severity:** BUG-01 / MAJOR.
2. **Detected by:** Repository code review and restart-persistence requirement.
3. **Symptom:** Tickets were stored in the module-level `fake_db` dictionary and disappeared when the process restarted.
4. **Reproduction:** Create a ticket, stop the API process, restart it, then request the ticket list.
5. **Root cause:** No database connection or repository persistence layer was implemented.
6. **Fix:** Added SQLite schema, connection management, repository methods, and a named Docker volume.
7. **Commit / verification:** Resolved in the BT3 implementation commit; verified by TC-03, TC-04, TC-05 and TC-12. Commit: `PENDING_COMMIT_URL`.

## BUG-02 — MAJOR — Invalid phone / IMEI / category / priority values were not validated

1. **ID / Severity:** BUG-02 / MAJOR.
2. **Detected by:** Boundary and invalid-input review.
3. **Symptom:** The API accepted arbitrary strings for phone, IMEI, issue category, and priority.
4. **Reproduction:** POST a ticket with a 9-digit phone number, non-numeric IMEI, or unsupported priority.
5. **Root cause:** The original Pydantic request model declared plain `str` fields without format or enum constraints.
6. **Fix:** Added Pydantic v2 patterns, Literal enumerations, description constraints, and a safe validation error handler.
7. **Commit / verification:** Resolved in the BT3 implementation commit; verified by TC-07 through TC-10. Commit: `PENDING_COMMIT_URL`.

## BUG-03 — MAJOR — The original create-ticket test could pass when creation failed

1. **ID / Severity:** BUG-03 / MAJOR.
2. **Detected by:** Test-suite audit.
3. **Symptom:** `test_create_ticket_success` accepted HTTP 422 as a successful outcome and sent field names not used by the API.
4. **Reproduction:** Run the original test with its mismatched payload; a validation failure could still satisfy the assertion.
5. **Root cause:** The test assertion allowed `[200, 201, 422]` and the payload contained obsolete keys.
6. **Fix:** Replaced the weak test with a valid payload and an exact HTTP 201 assertion; expanded the suite to 12 independent cases.
7. **Commit / verification:** Resolved in the BT3 implementation commit; verified by TC-03 and the full 12-case suite. Commit: `PENDING_COMMIT_URL`.