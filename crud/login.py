from core.database_settings import execute_query , DatabaseManager

def register():
    name = input("enter your name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    if password != confirm_password:
        print("password does not match")
        return register()

    existing_user = execute_query("SELECT * FROM users WHERE USERNAME=%s AND PASSWORD=%s",(username,password), fetch="one")
    if existing_user:
        print("user already exists. Please choose a different username.")
        return register()

    params = (name, username, password)
    query = "INSERT INTO users (name, username, password) VALUES (%s, %s, %s)"
    execute_query(query, params)
    print("Registered successfully")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = execute_query("SELECT FROM users WHERE USERNAME=%s AND PASSWORD=%s", (username,password), fetch="one")
    if user:
        print(f"Welcome {user['name']}")
        return True
    else:
        print("User not found")
        return False
