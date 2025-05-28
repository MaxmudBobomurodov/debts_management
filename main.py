from core.table_queries import initializing_table
from crud.login import register, login
def main_menu():
    print("""Menu:
    1.give debts
    2.take debts
    3.view total debts given
    4.view total debts taken
    5.view list of debts given
    6.view list of debts taken
    7.update debts
    8.show all users
    9.exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        pass
    elif choice == "8":
        pass
    elif choice == "9":
        auth_menu()
    else:
        print("Invalid choice")

    main_menu()

def auth_menu():
    print("""
    1.register
    2.login
    3.exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
        main_menu()
    elif choice == "2":
        if login():
            main_menu()
        else:
            print("Login failed, please try again!")
    elif choice == "3":
        print("Goodbye")
        return
    else:
        print("Invalid choice")
    auth_menu()


if __name__ == '__main__':
    initializing_table()
    auth_menu()
