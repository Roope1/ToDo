import sqlite3
from sqlite3 import Error
import database as db

class Task:
    def __init__(self, name: str, status: bool, description: str = None):
        self.name = name
        self.status = status
        self.description = description


class Tasks:
    

    def init_db(self) -> None:
        try:
            # create connection to database
            self.con = sqlite3.connect(f"{db.DB_NAME}")
            self.cur = self.con.cursor()

            # for testing the connection and check if any tables are present
            self.cur.execute(f"SELECT * FROM {db.TABLE_NAME}")

        except Error as e:     # db doesnt exist
            self.con = sqlite3.connect(f"{db.DB_NAME}")
            self.cur = self.con.cursor()
            self.cur.execute(f"{db.SCHEMA}")

        print("Database connection successful!\n")

    def fetch_tasks(self) -> list():
        self.tasks = []
        res = self.cur.execute(f"SELECT * FROM {db.TABLE_NAME}")
        return res.fetchall()


    def show_all(self):
        for task in self.tasks:
            print(task)

    def add_existing(self, task: Task):
        self.tasks.append(task)

    def add_new_task(self):
        # ask info
        name = input("Name of task: ")
        description = input("Description (optional): ")
        new_task = Task(name, "not started", description)

        # insert to db
        self.cur.execute(f"INSERT INTO {db.TABLE_NAME} \
        (task_name, status, task_description) \
        VALUES ('{name}','not started', '{description}')")
        self.con.commit()

        return new_task

