def get_valid_amount():
    while True:
        try:
            amount = int(input("Enter the amount: "))
            if amount <= 0:
                print("Error: Amount must be positive.")
                continue
            return amount
        except ValueError:
            print("Error: Please enter a valid number!")


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Current balance: {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: {self.balance}.")

    def display_balance(self):
        print(f"The balance of your account is {self.balance}.")


def main():
    account = BankAccount(112, 10000)
    print("Welcome to the Bank!")

    while True:
        operation = input("Choose the operation (deposit, withdraw, display_balance or exit): ").lower()

        if operation == "exit":
            print("Goodbye!")
            break
        elif operation == "deposit":
            amount = get_valid_amount()
            account.deposit(amount)
        elif operation == "withdraw":
            amount = get_valid_amount()
            account.withdraw(amount)
        elif operation == "display_balance":
            account.display_balance()
        else:
            print("Error: Invalid operation. Please choose again.")


main()
