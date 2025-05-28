from core.database_settings import execute_query

users = """
create table users
(
    id       SERIAL PRIMARY KEY,
    name     VARCHAR(50),
    username VARCHAR(50),
    password VARCHAR(50)
);
"""
debts = """
CREATE TABLE IF NOT EXISTS DEBTS(
    id         serial primary key,
    from_user  INT REFERENCES users (id),
    to_user    INT REFERENCES users (id),
    quantity   DECIMAL(10, 2),
    status     BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

def initializing_table():
    execute_query(query=users)
    execute_query(query=debts)