
class BankAccount:
    """Class name BankAccount that holds bank attributes and methods"""

    def __init__(self, full_name, account_number, balance=0):
        """Initialize bank account intance and setting up attributes"""
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
  
    def deposit(self, amount):
        """Helps add money to balance then updates balance. It will return the amount deposited and show the new balance with the new deposit."""
        self.balance += amount 
        print(f"Amount deposited: ${amount:,.2f}, new balance: ${self.balance:,.2f}")


    def withdraw(self, amount):
        """Checks to see if there's enough money in the balance. If there is not enough money there will be an overdraft fee of 10, this will be subtracted from the balance and an insufficient funds message will show. If there is enough money, it will subtract the amount from the balance and update the new balance. It will show amount withdrawn and new balance."""
        if amount > self.balance:
            self.balance -= 10 #overdraft fee
            print("Insufficient funds.")
        else:
            self.balance -= amount  
            print(f"Amount withdraw: ${amount:,.2f}, new balance ${self.balance:,.2f}")

    def get_balance(self):
        """Shows the account balance with a friendly message. Then shows the current balance of the account."""
        print(f"Thank you for being a valuable client. Your current account balance is ${self.balance:,.2f}")
        return self.balance

    def add_interest(self):
        """Adding interest to the user's balance."""
        self.balance = self.balance + (self.balance * 0.00083)
        return self.balance
    
    def print_statement(self):
        """Shows user's name, account number, and balance."""
        print(f"{self.full_name}\nAccount No.: {self.account_number}\nBalance: ${self.balance:,.2f}")

   

#different object instances
lucila_account = BankAccount("Lucila Hernandez", 12345678)
adi_account = BankAccount("Adi Armendariz", 10101010)
marceline_account = BankAccount("Marceline Hernandez", 20202020)

#depositing money, then withdrawing, and showing bank statement
adi_account.deposit(30000)
adi_account.withdraw(33000)
adi_account.get_balance()


# example code #1
# created new bank account intance
mitchell_account = BankAccount("Mitchell", "03141592")
#deposited $400,000 into "Mitchell's" account
mitchell_account.deposit(400000)
# printed statement
mitchell_account.print_statement()
# added interest
mitchell_account.add_interest()
# added interest to the account
mitchell_account.withdraw(150)
#printed statement
mitchell_account.print_statement()


#example code #2
# created new bank account account intance
maria_account = BankAccount("Maria", "02587109")
#deposited $700,000 into "Maria's" account
maria_account.deposit(700000)
# printed statement
maria_account.print_statement()
# added interest
maria_account.add_interest()
# added interest to the account
maria_account.withdraw(300)
#printed statement
maria_account.print_statement()
