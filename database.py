DB_NAME = "tasks.db"
TABLE_NAME = "tasks"
SCHEMA = f""" CREATE TABLE {TABLE_NAME} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name VARCHAR(255) NOT NULL,
    status VARCHAR(255),
    task_description VARCHAR(255)
);
 """
