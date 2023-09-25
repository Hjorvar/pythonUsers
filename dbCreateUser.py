def dbCreateUser(conn, user):
  sql = '''INSERT INTO users(firstName, lastName, email, password, mobilePhone)
            VALUES(?,?,?,?,?)'''
  cur = conn.cursor()
  cur.execute(sql, user)
  conn.commit()
  return True