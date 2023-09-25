from dbReadUser import dbReadUser
from dbDeleteUser import dbDeleteUser

def deleteUser(conn):
    """
    Delete user
    """
    id = input('Enter user id to be deleted: ')
    try:
        id = int(id)
    except ValueError:
        print("Invalid id")
        return False
    
    user = dbReadUser(conn, id)
    print(f"Are you sure you want to delete user {user[1]} {user[2]} (id: {user[0]})?")
    confirmation = input("Type 'yes' to confirm: ")
    if confirmation.lower() != "yes":
        print("Deletion cancelled")
        return False
    dbDeleteUser(conn, id)
    print("User deleted successfully")
    return True