"""
Class name BankAccount that holds bank attributes and methods
"""
class BankAccount:
    def __init__(self, full_name, account_number, balance=0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
  
    """
    Helps add money to balance then updates balance. It will return the amount deposited and show the new balance with the new deposit.
    """
    def deposit(self, amount):
        new_balance = self.balance + amount
        self.balance = new_balance
        print(f"Amount deposited: ${amount} new balance: ${self.balance}")

