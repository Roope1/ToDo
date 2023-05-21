import sqlite3
from sqlite3 import Error
import database as db

class Task:
    def __init__(self, name: str, status: bool, description: str = None):
        self.name = name
        self.status = status
        self.description = description


class Tasks:

    statuses = ["Not started", "In progress", "Done"]

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

    # add all existing tasks to the list
    def init_existing(self) -> None:
        for task in self.fetch_tasks():
            new_task = Task(task[1],task[2], task[3])
            self.add_existing(new_task)       


    def fetch_tasks(self) -> list():
        self.tasks = []
        res = self.cur.execute(f"SELECT * FROM {db.TABLE_NAME}")
        return res.fetchall()


    def show_all(self) -> None:
        for task in self.tasks:
            print(task.name)


    def add_existing(self, task: Task) -> None:
        self.tasks.append(task)


    def add_new_task(self):
        # ask info
        name = input("Name of task: ")
        description = input("Description (optional): ")
        new_task = Task(name, "not started", description)

        # insert to db
        self.cur.execute(f"INSERT INTO {db.TABLE_NAME} \
        (task_name, status, task_description) \
        VALUES ('{name}','{Tasks.statuses[0]}', '{description}')")
        self.con.commit()

        self.tasks.append(new_task)
    

    def choose_task(self) -> Task:
        for i in range(len(self.tasks)):
            print(f"{i + 1}. {self.tasks[i].name}")
        choice = input("Select a task: ")
        
        # TODO: input validation
        return self.tasks[int(choice) - 1]


    def change_task_status(self) -> None:
        cur_task = self.choose_task()

        print(f"Select status for task: {cur_task.name}")
        print("1. Not started\n2. In progress\n3. Done")

        status_choice = input("Your choice: ")
        # TODO: input validation
        new_status = Tasks.statuses[int(status_choice) - 1]
        cur_task.status = new_status

        # updating DB
        self.cur.execute(f"UPDATE {db.TABLE_NAME} \
            SET status = '{new_status}' WHERE task_name = '{cur_task.name}';")
        self.con.commit()
        return None


    def delete_task(self) -> None:
        cur_task = self.choose_task()
        self.tasks.remove(cur_task)

        # remove from DB
        self.cur.execute(f"DELETE FROM {db.TABLE_NAME} \
            WHERE task_name = '{cur_task.name}'")
        self.con.commit()
        
        del cur_task
        return None

    def edit_task(self):
        cur_task = self.choose_task()
        new_name = input("Give the task a new name (leave empty to use the original): ")
        new_desc = input("Give the task a new description (leave empty to use orginal): ")
        if (new_name == ""):
            new_name = cur_task.name
        if (new_desc == ""):
            new_desc = cur_task.description
        
        # update DB
        self.cur.execute(f"UPDATE {db.TABLE_NAME}\
            SET task_name = '{new_name}, task_description = '{new_desc}'\
            WHERE task_name = {cur_task.name};")
        self.con.commit()

        cur_task.name = new_name
        cur_task.description = new_desc

        return None


    def close(self) -> None:
        self.con.commit()
        self.cur.close()
        self.con.close()
        return None
