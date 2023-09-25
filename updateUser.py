def updateUser(conn, user):
    """
    update user's first name, last name, email, password, mobile phone
    """
    sql = ''' UPDATE users
              SET firstName = ? ,
                  lastName = ? ,
                  email = ?,
                  password = ?,
                  mobilePhone = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return True
