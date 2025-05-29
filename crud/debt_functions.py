from core.database_settings import execute_query
from datetime import datetime

def give_debt():
    from_user = input("enter your user id: ")
    to_user = input("enter user id you want to give debts: ")
    quantity = int(input("enter quantity: "))
    status = False
    created_at = datetime.now()

    params = (from_user, to_user,quantity,status,created_at)
    query = "INSERT INTO DEBTS (from_user,to_user,quantity,status,created_at) VALUES(%s,%s,%s,%s,%s)"
    execute_query(query,params)
    print("Successfully given")

def view_lest_of_debts():
    query = "SELECT * FROM DEBTS ORDER BY id;"
    return execute_query(query,fetch="all")

def view_total_debts_given():
    user_id = input("enter user id: ")
    query = "SELECT * FROM debts WHERE from_user = %s AND status = false;"
    debts = execute_query(query, (user_id,), fetch="all")
    sum_of_debts = 0
    for debt in debts:
            sum_of_debts += debt[3]
    print(f"user ID:{user_id}\n total debts given: {sum_of_debts}")


def show_all_users():
    query = "SELECT * FROM users;"
    return execute_query(query,fetch="all")

def update_status():
    try:
        debts_id = int(input("Enter debt ID: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    status = input("Did you pay (yes/no): ").strip().lower()
    if status == "yes":
        s = True
    elif status == "no":
        s = False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return

    query = "UPDATE debts SET status = %s WHERE id = %s;"
    execute_query(query, (s, debts_id))
    print("Status updated successfully.")

update_status()
