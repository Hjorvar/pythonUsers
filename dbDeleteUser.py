def dbDeleteUser(conn, id):
  sql = 'DELETE FROM users WHERE id=?'
  cur = conn.cursor()
  try:
    cur.execute(sql, (id,))
    conn.commit()
  except:
    print("Deletion failed")
    return False