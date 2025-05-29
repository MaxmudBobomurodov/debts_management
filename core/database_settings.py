import logging
from typing import Optional, Union, Any

import psycopg2
from psycopg2.extras import DictCursor, DictRow

from core.config import DB_CONFIG

logging.basicConfig(level=logging.INFO, filename="log.txt")
logger = logging.getLogger(__name__)


class DatabaseManager:
    def __init__(self):
        self.conn: Optional[psycopg2.extensions.connection] = None
        self.cursor: Optional[psycopg2.extensions.cursor] = None

    def __enter__(self) -> "DatabaseManager":
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(cursor_factory=DictCursor)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
            logger.error(msg="Transaction failed", exc_info=True)
        else:
            self.conn.commit()
            logger.info("Successfully executed")

        if self.conn:
            self.conn.close()

        if self.cursor:
            self.cursor.close()

    def execute(self, query: str, params: Union[tuple, dict, None] = None):
        self.cursor.execute(query, params)

    def fetchone(self, query: str, params: Union[tuple, dict, None] = None) -> Optional[DictRow]:
        self.execute(query, params)
        return self.cursor.fetchone()

    def fetchall(self, query: str, params: Union[tuple, dict, None] = None) -> list[tuple[Any, ...]]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

def execute_query(
    query: str,
    params: Union[tuple, dict, None] = None,
    fetch: Union[str, None] = None
) -> None | DictRow | list[tuple[Any, ...]]:
    try:
        with DatabaseManager() as db:
            if fetch == "one":
                return db.fetchone(query=query, params=params)
            elif fetch == "all":
                return db.fetchall(query=query, params=params)
            else:
                db.execute(query=query, params=params)
                return None
    except psycopg2.Error as e:
        logger.error(msg=f"Error while executing the query {e}", exc_info=True)
        return None
