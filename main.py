from bank_system import BankSystem

def display_menu():
    # Display the main menu options
    print("Welcome, How to help you?")
    print("1. Create new customer")
    print("2. Login")
    print("3. Display number of customers")
    print("4. Exit")

def main():
    # Initialize the bank system
    bank_system = BankSystem()
    while True:
        # Load user data from files
        bank_system.load_users_from_file()
        # Display the main menu
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Create a new customer
            username = input("Enter username: ")
            pin = input("Enter PIN: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            print(bank_system.create_new_customer(username, pin, initial_deposit))
        elif choice == '2':
            # Login with username and PIN
            username = input("Enter username: ")
            pin = input("Enter PIN: ")
            user = bank_system.login(username, pin)
            if isinstance(user, str):
                print(user)
            else:
                while True:
                    # Provide options for logged-in user
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. Check Info")
                    print("5. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        amount = float(input("Enter deposit amount: "))
                        print(bank_system.deposit(username, amount))
                    elif user_choice == '2':
                        amount = float(input("Enter withdrawal amount: "))
                        print(bank_system.withdraw(username, amount))
                    elif user_choice == '3':
                        receiver = input("Enter the receiver username: ")
                        amount = float(input("Enter the amount: "))
                        print(bank_system.transfer(username, receiver, amount))
                    elif user_choice == '4':
                        print(user.get_info())
                    elif user_choice == '5':
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            # Display the number of customers
            print(bank_system.displayNumOfCustomer())
        elif choice == '4':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        

if __name__ == "__main__":
    main()