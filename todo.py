import task_lib

def user_action() -> str:
    print("*** Actions ***")
    print("1. Add new task")
    print("2. Show all tasks")
    print("3. Change task status")
    print("4. Delete task")
    print("5. Edit task")
    print("0. Quit")

    choice = input("What do you want to do?: ")

    return choice


def main() -> None:
    tasks = task_lib.Tasks()
    tasks.init_db()


    
    # TODO: MOVE TO LIB
    # add all existing tasks to the list
    for task in tasks.fetch_tasks():
        new_task = task_lib.Task(task[1],task[2], task[3])
        tasks.add_existing(new_task)


    while True:
        user_choice = user_action()

        match user_choice:
            case "1":
                new_task = tasks.add_new_task()
                
            case "2":
                tasks.show_all()
                
            case "3":
                change_task_status()
                
            case "4":
                delete_task()
                
            case "5":
                edit_task()
                
            case "0":
                tasks.close()
                exit(0)
                
            case default:
                print(f"'{user_choice}' is not a valid option!")


if __name__ == "__main__":
    main()