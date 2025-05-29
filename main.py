from core.table_queries import initializing_table
from crud.login import register, login
from crud.debt_functions import give_debt,view_lest_of_debts, view_total_debts_given, show_all_users , update_status



def main_menu():
    print("""Menu:
    1.give debts
    2.view total debts given
    3.view list of debts given
    4.update debts
    5.show all users
    6.exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        give_debt()
    elif choice == "2":
        view_total_debts_given()
    elif choice == "3":
        debts = view_lest_of_debts()
        if not debts:
            print("No debts")

        for i in debts:
            if i['status']:
                status = "payed"
            else:
                status = "not payed"
            print(f"id: {i['id']}\nfrom_user: {i['from_user']}\nto_user: {i["to_user"]}\nquantity: {i["quantity"]}\nstatus: {status}\ncreated_at: {i['created_at']}")
    elif choice == "4":
        update_status()
    elif choice == "5":
        users = show_all_users()
        if users:
            for user in users:
                print(f"id: {user['id']}; name: {user['name']},username: {user['username']}")
        else:
            print("No users found!")
    elif choice == "6":
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

    return auth_menu()


if __name__ == '__main__':
    initializing_table()
    auth_menu()