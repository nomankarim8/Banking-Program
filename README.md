![logo](https://github.com/nomankarim8/nomankarim8/blob/main/image.png?raw=true)
# Python Banking Program

This Python Banking Program allows users to perform basic banking operations such as checking the balance, depositing money, and withdrawing money. It runs in a console environment, prompting the user for input and displaying the current balance.

## Features

- **Show Balance:** Displays the current balance.
- **Deposit:** Allows the user to deposit money into their account.
- **Withdraw:** Allows the user to withdraw money from their account, ensuring they have sufficient funds.
- **Exit:** Exits the program.

## Requirements

- Python 3.x

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/python-banking-program.git
    cd python-banking-program
    ```

2. **Run the program:**

    ```bash
    python banking_program.py
    ```

3. **Follow the on-screen instructions:**

    - **Show Balance:** Press `1` to display your current balance.
    - **Deposit:** Press `2` to deposit money. Enter the amount when prompted.
    - **Withdraw:** Press `3` to withdraw money. Enter the amount when prompted.
    - **Exit:** Press `4` to exit the program.

## Code Overview

### Functions

- `show_balance(balance)`: Displays the current balance.
- `deposit()`: Prompts the user for a deposit amount and returns the amount if valid.
- `withdraw(balance)`: Prompts the user for a withdrawal amount and returns the amount if valid.
- `main()`: Main function that runs the banking program, handling user input and calling the appropriate functions.

### Program Flow

1. The program starts with a balance of 0.
2. It displays a menu with options to show balance, deposit, withdraw, or exit.
3. Based on the user's choice, it performs the corresponding operation.
4. The program continues to run until the user chooses to exit.

## Example

```plaintext
*********************
   Banking Program   
*********************
1.Show Balance
2.Deposit
3.Withdraw
4.Exit
*********************
Enter your choice (1-4): 2
*********************
Enter an amount to be deposited: 100
*********************
*********************
Your balance is $100.00
*********************
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features.

## Author

- [nomankarim8](https://github.com/nomankarim8)

```

