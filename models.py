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
def password_first():
    pas=''
    pas2=''
    while len(pas)<8:
        pas=input('Enter a password')

    while pas!=pas2:
        pas2=input('Enter a password')
    return pas