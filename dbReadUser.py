def dbReadUser(conn, id):
  """
  Find user by id
  """
  cur = conn.cursor()
  cur.execute("SELECT * FROM users WHERE id = ?", (id,))

  row = cur.fetchone()
  if row is None:
    raise ValueError("User not found")
  
  return row