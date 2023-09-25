import bcrypt
from dbCreateUser import dbCreateUser

def createUser(conn):
    """
    Create a new user into the users table
    """
    # create a new user
    firstName = input('Enter your first name: ')
    lastName = input('Enter your last name: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    mobilePhone = input('Enter your mobile phone: ')

    # converting password to array of bytes
    bytes = password.encode('utf-8')

    # generating the salt
    salt = bcrypt.gensalt()

    # Hashing the password
    hash = bcrypt.hashpw(bytes, salt)

    user = (firstName, lastName, email, hash.decode(), mobilePhone)
    dbCreateUser(conn, user)
    return True


