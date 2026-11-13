"""SQLite connection and schema helpers for the L2 prototype."""
from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


def database_path() -> Path:
    return Path(os.getenv("DATABASE_PATH", "data/tickets.db"))


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    path = database_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path, timeout=15)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def init_db() -> None:
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tickets (
                ticket_id TEXT PRIMARY KEY,
                customer_phone TEXT NOT NULL CHECK(length(customer_phone) = 10),
                imei TEXT NOT NULL CHECK(length(imei) = 15),
                issue_category TEXT NOT NULL
                    CHECK(issue_category IN ('MAN_HINH', 'PIN', 'SAC', 'PHAN_MEM')),
                description TEXT NOT NULL,
                priority TEXT NOT NULL
                    CHECK(priority IN ('LOW', 'MEDIUM', 'HIGH', 'URGENT')),
                status TEXT NOT NULL
                    CHECK(status IN ('MỚI', 'ĐANG XỬ LÝ', 'HOÀN TẤT', 'ĐÃ HỦY')),
                created_at TEXT NOT NULL,
                due_date TEXT NOT NULL
            )
            """
        )


def database_is_ready() -> bool:
    with get_connection() as connection:
        connection.execute("SELECT 1").fetchone()
    return True