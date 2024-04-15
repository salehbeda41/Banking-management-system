# Banking Management System

This is a Python-based banking management system that allows users to create accounts, perform transactions, and manage their finances.

## Features

- **User Management**: Create new customer accounts and log in securely.
- **Transaction Handling**: Deposit, withdraw, and transfer funds between accounts.
- **Data Persistence**: Store user data, PINs, and transaction history in text and Excel files.
- **Menu Interface**: Intuitive console menu for easy navigation.

## Installation

1. Clone the repository to your local machine:

    git clone https://github.com/salehbeda41/banking-management-system.git

2. Install the required dependencies:

    pip install openpyxl

## Usage

1. Navigate to the project directory:

    cd banking-management-system

2. Run the main script:

    python main.py

3. Follow the on-screen prompts to create new customers, log in, perform transactions, and display customer information.

## Configuration

No specific configuration is required. However, you may customize the file paths or other settings in the source code if needed.

## File Structure

- `bank_system.py`: Contains the main logic for the banking system.
- `file_handler.py`: Handles file operations for storing user data and transaction history.
- `main.py`: Entry point for running the application and interacting with the user.
- `user.py`: Defines the User class for managing user accounts.
- `balances.txt`, `pins.txt`, `users.txt`: Files for storing user data.

## Troubleshooting

- If you encounter any issues during installation or usage, please check the project's [GitHub Issues](https://github.com/salehbeda41/banking-management-system/issues) page for known problems or open a new issue if necessary.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, feel free to reach out to [Your Name](mailto:salehbeda41@gmail.com).
