import sqlite3
conn = sqlite3.connect('bank.db')
c = conn.cursor()


conn.commit()
conn.close()