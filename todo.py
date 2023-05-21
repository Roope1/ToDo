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
    tasks.init_existing()

    while True:
        user_choice = user_action()

        match user_choice:
            case "1":
                new_task = tasks.add_new_task()
                
            case "2":
                tasks.show_all()
                
            case "3":
                tasks.change_task_status()
                
            case "4":
                tasks.delete_task()
                
            case "5":
                tasks.edit_task()
                
            case "0":
                tasks.close()
                exit(0)
                
            case default:
                print(f"'{user_choice}' is not a valid option!")


if __name__ == "__main__":
    main()