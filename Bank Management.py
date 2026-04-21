class Account():

    def __init__(self,account_number, name, balance=0):

        self.account_number = account_number

        self.name = name

        self.balance = balance

   

    def deposit(self,amount, show=True):

        if amount<=0:

            print("invalid amount")

            return

        self.balance = self.balance + amount

        if show:

            print( f"{self.balance} amount deposited successfully")

       

    def withdraw(self,amount, show=True):

        if amount > self.balance :

            raise Exception("insufficient balance")

            return

        self.balance = self.balance - amount

        if show:

            print( f" {amount} withdrawn successfully")

 

    def transfer (self, newac_number,amount):

        try:

            self.withdraw(amount, show=False)

            newac_number.deposit(amount, show=False)

            print("transaction successful")

        except Exception as e:

            print("transfer failed:", e)

 

       

    def display(self):

        print("Balance amount:", self.balance)

 
accounts = {}   

def create_account():
    acc_no = input("Enter account number: ")
    name = input("Enter name: ")
    balance = float(input("Enter initial balance: "))

    acc = Account(acc_no, name, balance)

    accounts[acc_no] = acc

    print("Account created successfully")
 

def find_account(acc_no):

    for acc in accounts:

        if acc.account_number == acc_no:

            return acc

    return None


while True:

    print("\n1. Create Account")

    print("2. Deposit")

    print("3. Withdraw")

    print("4. Transfer")

    print("5. Display Accounts")

    print("6. Exit")


    choice = input("Enter choice: ")


    if choice == "1":

        create_account()


    elif choice == "2":

        acc_no = input("Enter account number: ")

        acc = find_account(acc_no)

        if acc:

            amount = float(input("Enter amount: "))

            acc.deposit(amount)

        else:

            print("Account not found")


    elif choice == "3":

        acc_no = input("Enter account number: ")

        acc = find_account(acc_no)

        if acc:

            try:

                amount = float(input("Enter amount: "))

                acc.withdraw(amount)

            except Exception as e:

                print(e)

        else:

            print("Account not found")


    elif choice == "4":

        from_acc_no = input("From account: ")

        to_acc_no = input("To account: ")


        from_acc = find_account(from_acc_no)

        to_acc = find_account(to_acc_no)


        if from_acc and to_acc:

            amount = float(input("Enter amount: "))

            from_acc.transfer(to_acc, amount)

        else:

            print("One or both accounts not found")


    elif choice == "5":

        for acc in accounts:

            acc.display()


    elif choice == "6":

        break


    else:

        print("Invalid choice")
