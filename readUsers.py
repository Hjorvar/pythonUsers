from dbReadUsers import dbReadUsers

def readUsers(conn):
    users = dbReadUsers(conn)
    for user in users:
        print(f"First Name: {user['firstName']}, "
              f"Last Name: {user['lastName']}, "
              f"Email: {user['email']}, "
              f"Password: {user['password']}")