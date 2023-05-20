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
            try:
                self.con = sqlite3.connect(f"{db.DB_NAME}")
                self.cur = self.con.cursor()
                self.cur.execute(f"{db.SCHEMA}")

                self.cur.execute(f"SELECT * FROM {db.TABLE_NAME}")
                print("Database connection successful!\n")

            except Exception:
                print("Something went wrong")
                exit(1)

    def fetch_tasks(self) -> list():
        self.tasks = []
        res = self.cur.execute(f"SELECT * FROM {db.TABLE_NAME}")
        return res.fetchall()


    def show_all(self) -> None:
        for task in self.tasks:
            print(task)

    def add_existing(self, task: Task) -> None:
        self.tasks.append(task)

    def add_new_task(self) -> Task:
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
    
    def change_task_status():
        pass

    def delete_task():
        pass

    def edit_task():
        pass


    def close(self) -> None:
        self.con.commit()
        self.cur.close()
        self.con.close()
        return None
