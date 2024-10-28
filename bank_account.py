"""
Class name BankAccount that holds bank attributes and methods
"""
class BankAccount:
    def __init__(self, full_name, account_number, balance=0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
  
    """
    Helps add money to balance then updates balance. 
    It will return the amount deposited and show the new balance with the new deposit.
    """
    def deposit(self, amount):
        new_balance = self.balance + amount
        self.balance = new_balance
        print(f"Amount deposited: ${amount:.2f} new balance: ${self.balance:.2f}")

    """
    Checks to see if there's anough money in the balance. 
    If there is not enouph money there will be a overdraft fee of 10, this will be subtracted from the balance and an insufficient funds message will show.
    If there is enouph money, it will subtract the amount from the balance and update the new balance. It will show amount withdrawn and new balance. 
    """
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance = self.balance - 10
            print("Insufficient funds. Overdraft fee charged")
        else:
            new_balance = self.balance - amount
            self.balance = new_balance 
            print(f"Amount withdraw: ${amount:.2f} new balance ${self.balance:.2f}")

    """
    Show a account balance with a friendly message. Then shows current balance of the account. 
    """
    def get_balance(self):
        balance = self.balance
        print(f"Thank you for being our bank user. Your current account balance is ${balance:.2f}")
        return balance
    
    """
    Adding interest to the users balance.
    """
    def add_interest(self):
        self.balance = self.balance + (self.balance * 0.00083)
        return self.balance
    
    """
    Shows users name, account number and balance. 
    """
    def print_statement(self):
        print(f"{self.full_name}\nAccount No.: {self.account_number}\nBalance: ${self.balance:.2f}")
