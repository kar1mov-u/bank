import models
from models import Users
from models import Bank
bnk = Bank()
print('Welcome to our Bank !')
print('Choose one of these options (Press q for exit program)')
while True:


    print('1 - Login')
    print('2 - Create Acc')
    print('3 - Display Information')
    print('4 - Add a bank card')
    print('5 - Check Balance')
    print('6 - Log-out')

    command = input()
    if command == '1':
        bnk.login()
    elif command == '2':
        bnk.create_account()
    elif command == '3' :
        bnk.display_info()
    elif command =='4':
        bnk.add_bank_card()
    elif command == '5':
        bnk.balance_show()
    elif command == '6':
        bnk.logout()
    else:
        print('Thank you for using our BANK !!')
        break