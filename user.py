
class User:
    # Represents a user in the banking system
    def __init__(self, username, pin, initial_deposit=0):
        # Initialize user with username, PIN, and initial deposit
        self.username = username
        self.pin = pin
        self.account_balance = initial_deposit
    
    def deposit(self, amount):
        # Deposit an amount into the user's account
        self.account_balance += amount
        return f"Deposit of {amount} successfully processed. New balance: {self.account_balance}"
        
    def withdraw(self, amount):
        # Withdraw an amount from the user's account if funds are sufficient
        if amount <= self.account_balance:
            self.account_balance -= amount
            return f"Withdrawal of {amount} successfully processed. New balance: {self.account_balance}"
        else:
            return "Insufficient funds"
        
    def get_info(self):
        # Return user's account information
        return f"Username: {self.username}\nAccount Balance: {self.account_balance}"
    
    
        