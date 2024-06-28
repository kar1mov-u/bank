from datetime import datetime
import bcrypt 
class Users:
    def __init__(self,full_name,username,password,email) -> None:
        self.username = username
        self.email=email
        salt = bcrypt.gensalt()
        self.password= bcrypt.hashpw(password.encode('utf-8'),salt)
        self.full_name = full_name
        self.created_at=datetime.now().date()
    
# Getting a password from a user for 1st time
def get_pass():
    pass1 = input('Enter a password: ')
    mess = ''
    while True:
        pass2=input(mess + 'Enter password again :')  
        if pass2==pass1:
            break
        else:
            mess='Wrong !!!'
    return pass1

def pas_check(plaintext, hashed):
    return bcrypt.checkpw(plaintext.encode('utf-8'), hashed)


