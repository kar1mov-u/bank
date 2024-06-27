import sqlite3

'''

conn=sqlite3.connect('bank.db')
c=conn.cursor()
# Create the users table
c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        created_at DATE NOT NULL
    )
""")
conn.commit()
conn.close()
'''

class Dbase:
    def __init__(self) -> None:
        self.conn=sqlite3.connect('bank.db')
        self.c = self.conn.cursor()
    
    def add_user(self,fullname,username,password,email,created_at):
        self.c.execute("INSERT INTO users(full_name,username,password,email,created_at) VALUES(?,?,?,?,?)", (fullname,username,password,email,created_at))
    def close(self):
        self.conn.commit()
        self.conn.close()