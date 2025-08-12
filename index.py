class BankAccount:
    def __init__(self,acc_num,acc_holder):
        self.__acc_num=acc_num
        self.__acc_holder=acc_holder
        self.__balance=0.0
        self.__acc_transactions=[]



    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            self.__acc_transactions.append(f"Deposited ₹{amount}")
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount. Deposit failed.")


    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__acc_transactions.append(f"Withdrew ₹{amount}")
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.__balance}")

    def view_statement(self):
        print("=== Transaction Statement ===")
        if not self.__acc_transactions:
            print("No transactions yet.")
        else:
            for t in self.__acc_transactions:
                print(t)
        print("-----------------------------")
    

    def display_info(self):
        print("=== Account Info ===")
        print(f"Account Holder: {self.__acc_holder}")
        print(f"Account Number: {self.__acc_num}")
        print(f"Balance: ₹{self.__balance}")
        print("-----------------------------")


accounts={}
 

while True:
    print("\n=== Bank Account System ===")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View Statement")
    print("6. Show Account Info")
    print("7. Exit")

    option=input("select your option (1-7): ")
    if option=="1":
        acc_no = input("Enter new account number: ")
        name = input("Enter account holder name: ")
        if acc_no in accounts:
            print("Account already exists.")
        else:
            accounts[acc_no] = BankAccount(acc_no, name)
            print("Account created successfully.")
    elif option in ['2', '3', '4', '5', '6']:
        acc_no = input("Enter your account number: ")
        account = accounts.get(acc_no)
        if not account:
            print("Account not found")
        elif option == '2':
            amount= float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif option == '3':
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)

        elif option == '4':
            account.check_balance()

        elif option == '5':
            account.view_statement()

        elif option == '6':
            account.display_info()
    elif option=="7":
        print("Thank you for using the Bank Account System.")
        break
    else:
        print("Invalid choice. Try again.")
