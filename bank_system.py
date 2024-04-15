from user import User
from file_handler import FileHandler

class BankSystem:
    # Manages operations related to users and their accounts
    def __init__(self):
        # Initialize user dictionary and file handler
        self.users = {}
        self.file_handler = FileHandler()

    def create_new_customer(self, username, pin, initial_deposit):
        # Create a new customer with the given username, PIN, and initial deposit
        if username in self.users:
            return "Username already exists. Please choose another username."
        new_user = User(username, pin, initial_deposit)
        self.users[username] = new_user
        # Add user details to files and create user folders and files
        self.file_handler.add_user_to_file(username)
        self.file_handler.add_pin_to_file(pin)
        self.file_handler.add_balance_to_file(username, initial_deposit)
        self.file_handler.create_folder(username)
        self.file_handler.create_user_file(username, pin, initial_deposit)
        self.file_handler.create_excel_sheet(username)
        return "New customer created successfully."


    def login(self, username, pin):
        # Log in a user with the given username and PIN
        if username in self.users:
            user = self.users[username]
            if user.pin == pin:
                return user
            else:
                return "Invalid PIN."
        else:
            return "User not Exist."
        

    def transfer(self, sender_username, receiver_username, amount):
        # Transfer funds from one user to another
        sender = self.users.get(sender_username)
        receiver = self.users.get(receiver_username)

        if sender and receiver:
            if sender.account_balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                # Update balances and transaction history
                self.file_handler.update_balance_in_file(sender_username, sender.account_balance)
                self.file_handler.update_balance_in_file(receiver_username, receiver.account_balance)
                self.file_handler.update_transaction_history(sender_username, ["Transfer to " + receiver_username, -amount, sender.account_balance])
                self.file_handler.update_transaction_history(receiver_username, ["Receive from " + sender_username, amount, receiver.account_balance])
                return "Transfer successful"
            else:
                return "Insufficient funds for transfer"
        else:
            return "Receiver not found"

        

    def deposit(self, username, amount):
        # Deposit funds into a user's account
        user = self.users.get(username)
        if user:
            user.deposit(amount)
            # Update balance and transaction history
            file_handler = FileHandler()
            file_handler.update_balance_in_file(username, user.account_balance)
            file_handler.update_transaction_history(username, ["deposit " , amount, user.account_balance])
            return f"Deposit of {amount} successfully processed. New balance: {user.account_balance}"
        else:
            return "User not Exist."
        


    def withdraw(self, username, amount):
        # Withdraw funds from a user's account
        user = self.users.get(username)
        if user:
            user.withdraw(amount)
            # Update balance and transaction history
            file_handler = FileHandler()
            file_handler.update_balance_in_file(username, user.account_balance)
            file_handler.update_transaction_history(username, ["withdraw " , -amount, user.account_balance])
            return f"Withdrawal of {amount} successfully processed. New balance: {user.account_balance}"
        else:
            return "User not Exist."
        
    

    def displayNumOfCustomer(self):
        # Display the number of customers
        return f"Number of customers: {len(self.users)}"
    

    def load_users_from_file(self):
        # Load user data from files
        usernames = self.file_handler.get_usernames_from_file()
        pins = self.file_handler.get_pins_from_file()
        balances = self.file_handler.get_balances_from_file()
        for username, pin in zip(usernames, pins):
            balance = balances.get(username, 0)
            self.users[username] = User(username, pin, balance)



    