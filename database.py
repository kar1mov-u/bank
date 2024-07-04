import sqlite3
import models

'''
conn=sqlite3.connect('bank.db')
c=conn.cursor()
# Create the customers table
c.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        created_at DATE NOT NULL
    )
""")
# Create the bank_cards table
c.execute("""
    CREATE TABLE IF NOT EXISTS bank_cards (
        card_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        card_number TEXT NOT NULL,
        balance REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES customers(user_id)
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
            self.c.execute("INSERT INTO customers(full_name,username,password,email,created_at) VALUES(?,?,?,?,?)", (fullname,username,password,email,created_at))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f'Database Error : {e}')



    #Checks if provided  username or email is UNIQUE,else makes sure to get unique both of them
    def check_exists(self,uname=True):
        if uname:
            while True:
                name=input('Enter username : ')
                self.c.execute("SELECT * FROM customers WHERE username =? ",(name,))
                data=self.c.fetchall()
                if data:
                    print(f' Username : {name} is not avaiable')
                else:
                    return name
                    break
        else:
            while True:
                email=input('Enter email : ')
                self.c.execute("SELECT * FROM customers WHERE email =? ",(email,))
                data=self.c.fetchall()
                if data:
                    print(f' Email address : {email} is not avaiable')
                else:
                    return email
                    break



    
    # Gets user's data from the database based on username, and checks validity with the password 
    def get_user_data(self,username,pas):
        try:
            self.c.execute("SELECT * FROM customers WHERE username =?", (username,))
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



    def add_card(self,uid):
        card_num = input('Enter your card number')
        balance = input('Enter a balance : ')
        if card_num and balance:
            try:
                self.c.execute("INSERT INTO bank_cards (user_id, card_number, balance) VALUES (?, ?, ?)", (uid, card_num, balance))
                self.conn.commit()
                print(f'You have successfully added bank card : {card_num}')
            except sqlite3.Error as e:
                print(f'Database error in add_card : {e}')

    def balance_check(self,uid):

        try:
            self.c.execute("SELECT card_number,balance FROM bank_cards WHERE user_id=?",(uid,))
            data = self.c.fetchall()
            if data:
                for i in data:
                    print(f'CARD : {i[0]}  |   Balance : {i[1]}')
                    print('---------------------------------')
            else:
                print('You do not have any cards')
        except sqlite3.Error as e:
            print(f'Database error : {e}')

    def close(self):
        self.conn.commit()
        self.conn.close()