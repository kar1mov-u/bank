import sqlite3
import models
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
    
    # Adds new user to the database
    def add_user(self,fullname,username,password,email,created_at):
        try:
            self.c.execute("INSERT INTO users(full_name,username,password,email,created_at) VALUES(?,?,?,?,?)", (fullname,username,password,email,created_at))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f'Database Error : {e}')



    #Checks if provided  username or email is UNIQUE,else makes sure to get unique both of them
    def check_exists(self,uname=True):
        if uname:
            while True:
                name=input('Enter username : ')
                self.c.execute("SELECT * FROM users WHERE username =? ",(name,))
                data=self.c.fetchall()
                if data:
                    print(f' Username : {name} is not avaiable')
                else:
                    return name
                    break
        else:
            while True:
                email=input('Enter email : ')
                self.c.execute("SELECT * FROM users WHERE email =? ",(email,))
                data=self.c.fetchall()
                if data:
                    print(f' Email address : {email} is not avaiable')
                else:
                    return email
                    break



    
    # Gets user's data from the database based on username, and checks validity with the password 
    def get_user_data(self,username,pas):
        try:
            self.c.execute("SELECT * FROM users WHERE username =?", (username,))
            data = self.c.fetchone()
            if data:
                pass_hash = data[3]
                if models.pas_check(pas,pass_hash):
                    return data
                else:
                    print('Invalid password or username')
            else:
                print('Invalid password or username')
        except sqlite3.Error as e:
            print(f'Database error in  get_user_data: {e}')


    def close(self):
        self.conn.commit()
        self.conn.close()