class User:
    def __init__(self, email, password, balance):
        self.email = email
        self.password = password
        self.balance = balance

class Bank:
    user_list = []
    deposit_history = []
    email = ''
    password = 0
    total_loan = 0
    bank_balance = 0
    loan_history = []
    withdraw_history = []
    

    def show(self):
        for user in self.user_list:
            print(f"Email: {user.email}, Balance: {user.balance}")

class Customer(User):
    def __init__(self):
        pass
    def create_account(self):
        email = input("Enter your Email: ")
        password = input("Enter Your Password: ")
        balance = 0
        new_user = User(email, password, balance)
        Bank.user_list.append(new_user)
        print("\nCreate Account Successful\n")

    def deposit(self, email, password, money):
        for user in Bank.user_list:
            if user.email == email and user.password == password:
                user.balance += money
                Bank.bank_balance += money
                new_dict = {'email': email, 'deposit': money}
                f = 0
                for u in Bank.deposit_history:
                    if u.email == email:
                        Bank.deposit_history['deposit'] == money
                        f =1
                    else:
                        Bank.deposit_history.append(new_dict)
                        f = 1
                if f == 0:
                    Bank.deposit_history.append(new_dict)
                      

                print(10*'*',"  Deposit Successful")
               
                return
        print("\nUser not found")

    def withdraw(self, email, password, money):
        for user in Bank.user_list:
            if user.email == email and user.password == password:
                if money <= user.balance:
                    user.balance -= money
                    Bank.bank_balance -= money
                    new_dict = {'email': email, 'withdraw': money}
                    f = 0
                    for u in Bank.withdraw_history:
                        if u.email == email:
                            Bank.withdraw_history['withdraw'] == money
                            f =1
                        else:
                            Bank.withdraw_history.append(new_dict)
                            f = 1
                    if f == 0:
                        Bank.withdraw_history.append(new_dict)
                        print(10*'*',"  Withdrawal Successful")
                else:
                    print("Not enough money in your account")
                return
        print("User not found")

    def loan(self, money):
     
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            loan = money * 2
            for user in Bank.user_list:
                if user.email == email and user.password == password:
                    if loan <= user.balance and loan <= Bank.bank_balance:
                        user.balance += money
                        Bank.total_loan += money
                        Bank.bank_balance -= money
                        new_dict = {'email': email, 'lone': money}
                        f = 0
                        for u in Bank.loan_history:
                            if u.email == email:
                                Bank.loan_history['lone'] == money
                                f =1
                            else:
                                Bank.loan_history.append(new_dict)
                                f = 1
                        if f == 0:
                            Bank.loan_history.append(new_dict)
                        print(10*'*',"  Loan Successful")
                    else:
                        print("Sorry, loan cannot be processed")
                    return
            print("User not found")
        
        
    def transaction_history():
        pass

class Admin(User):
    def __init__(self):
        pass
    def create_account(self):
        email = input("Enter Your email: ")
        password = int(input("Enter Your Password: "))
        Bank.email = email
        Bank.password = password
        print("\nCreate Account Successful\n")
    

    def available_money(self):
        print("\nBank Name: Kalu Bank")
        print(f"Available balance of Kalu Bank: {Bank.bank_balance}")
        print()

    def total_loan(self):
        print("\nTotal loan of Kalu Bank:", Bank.total_loan)
        print()
    flag = 0   
    def myOpenion(a):
        if a == 1:
            Admin.flag = 1
        else:
            Admin.flag = 0
        
        

bank = Bank()
customer = Customer()
admin = Admin()

while True:
    print()
    print("====================** Welcome to Taka Khor Bank **======================\n")
    print("1. Create an Account\n2. Log in to an Account\n3. Exit\n")
    choice = int(input("Enter your choice: "))

    if choice == 3:
        break

    elif choice == 1:
        while True:
            print("\n1. Create an account as admin\n2. Create an account as user\n")
            create_choice = int(input("Enter your choice: "))

            if create_choice == 1:
                admin.create_account()
                break

            elif create_choice == 2:
                customer.create_account()
                break

    elif choice == 2:
        while True:
            print()
            print("1. Log in to an account as admin\n2. Log in to an account as user\n3. Back to previws page")
            print()
            login_choice = int(input("Enter your choice: "))

            if login_choice == 3:
                break

            elif login_choice == 1:
                email = input("Enter your email: ")
                password = int(input("Enter your password: "))

                if email == Bank.email and password == Bank.password:
                    while True:
                        print(f"{10*'>'} Hello Admin Welcome to Taka Khro Bank  {10*'<'}")
                        print()
                        print("1. Check the total available balance of the bank")
                        print("2. Check the total loan amount")
                        print("3. Can on or off the loan feature of the bank")
                        print("4. Back to previews page")
                        print()
                        admin_choice = int(input("Enter your choice: "))

                        if admin_choice == 4:
                            break

                        elif admin_choice == 1:
                            admin.available_money()

                        elif admin_choice == 2:
                            admin.total_loan()
                        elif admin_choice==3:
                             print()
                             print("You can turn the feature on and off ")
                             print()
                             print('1. On')
                             print('2. Off')
                             print()
                          
                             o  = int(input("Enter Your Choice: "))
                             
                             if o == 1:
                               Admin.myOpenion(1)
                               print("Trun on loan feature")
                                
                             elif o == 2:
                                 Admin.myOpenion(2) 
                                 print("Trun off loan feature")
                else:
                    print("Create an account frist")                
                                 
                        

            elif login_choice == 2:
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                print()

                for user in Bank.user_list:
                    if email == user.email and password == user.password:
                        while True:
                            print(f"\n{10*'>'} Hello {user.email} Welcome to Taka Khor Bank {10*'<'}")
                            print()
                            print("1. Deposit")
                            print("2. Withdraw")
                            print("3. Loan")
                            print("4. Lest Transaction history")
                            print("5. Back to previews page")
                            print()
                            user_choice = int(input("Enter your choice: "))

                            if user_choice == 5:
                                break

                            elif user_choice == 1:
                                money = int(input("Enter your amount: "))
                                customer.deposit(email, password, money)

                            elif user_choice == 2:
                                money = int(input("Enter your amount: "))
                                customer.withdraw(email, password, money)

                            elif user_choice == 3:
                                if Admin.flag==1:
                                    
                                    money = int(input("Enter the loan amount: "))
                                    customer.loan(money)
                                else:
                                    print("\nAdmin off the feature\n")
                                    break
                            elif user_choice == 4:
                                print("\n     Hello User Here Your Lest Transaction History    \n")
                                for i in Bank.deposit_history:
                                     if i['email'] == email:
                                        print(f"Deposit: {i['deposit']}")
                                        
                                for i in Bank.withdraw_history:
                                     if i['email'] == email:
                                         print(f"Withdraw: {i['withdraw']}")
                                         
                                for i in Bank.loan_history:
                                     if i['email'] == email:
                                         print(f"Loan : {i['loan']}\n")
                                    