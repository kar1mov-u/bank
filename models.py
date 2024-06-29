from datetime import datetime
import bcrypt 
import database
class Users:
    def __init__(self,full_name,username,password,email) -> None:
        self.full_name = full_name
        self.username = username
        self.email=email
        salt = bcrypt.gensalt()
        self.password= bcrypt.hashpw(password.encode('utf-8'),salt)
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

# Checking password hash from the database and user provided plaintext forn
def pas_check(plaintext, hashed):
    return bcrypt.checkpw(plaintext.encode('utf-8'), hashed)



# Funtion to create an account for a new user
def create_acc():
    # Creating a new database instance 
    db = database.Dbase()

    fname= input('Enter your fullname : ')
    uname = db.check_exists()
    email  =db.check_exists(False)
    pas = get_pass()
    #Creating Users Class with the provided inputs
    user = Users(fname,uname,pas,email)
    # Adding info of the user to the database
    db.add_user(user.full_name,user.username,user.password,user.email,user.created_at)
    db.close()
    print('You have successfully created account')          


def login():
    db = database.Dbase()
    print('Enter followinf credentials to login your account')
    uname = input('Enter your username : ')
    pas = input('Enter your password : ')
    data = db.get_user_data(uname,pas)
    if data:
        print('You have successfuly logged into your account')
        print(f'Full-name : {data[1]}')
        print(f'Username : {data[2]}')
        print(f'Email : {data[4]}')
        print(f'Created-at: {data[5]}')