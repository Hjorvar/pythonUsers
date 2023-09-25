def dbReadUsers(conn):
    """
    Query all rows in the users table
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM users ORDER BY firstName")

    rows = cur.fetchall()
    users = []
    for row in rows:
        user = {
            'firstName': row[0],
            'lastName': row[1],
            'email': row[2],
            'password': row[3]
        }
        users.append(user)

    return users
