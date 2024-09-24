import json

# Function to retrieve the bank data from a file
def get_bank_data():
    try:
        with open("Bank.txt", "r") as file:
            data = file.read()
            if data:
                return json.loads(data)  # Parse JSON data
            else:
                return []  # Return an empty list if the file is empty
    except FileNotFoundError:
        return []  # If file doesn't exist, return an empty list

# Function to save data back to the file
def save_bank_data(data):
    with open("Bank.txt", "w") as file:
        json.dump(data, file, indent=4)  # Write data as JSON

# Bank class to represent an account
class Bank:
    def __init__(self, user, balance=0):
        self.user = user
        self._account_balance = balance
    
    def deposit(self, amount):
        self._account_balance += amount
        
    def withdraw(self, amount):
        self._account_balance -= amount
        
    def get_balance(self):
        return self._account_balance

# Create a new bank account and save it to the file
def create_bank_acc(user, initial_balance=0):
    data = get_bank_data()
    for account in data:
        if account['user'] == user:
            print(f"Account for {user} already exists.")
            return
    # Create a new account and add it to the data list
    new_account = {
        'user': user,
        'balance': initial_balance
    }
    data.append(new_account)
    save_bank_data(data)
    print(f"Account created for {user}.")

# Delete an existing bank account
def delete_bank_acc(user):
    data = get_bank_data()
    updated_data = [account for account in data if account['user'] != user]
    
    if len(updated_data) == len(data):
        print(f"No account found for {user}.")
    else:
        save_bank_data(updated_data)
        print(f"Account for {user} deleted.")

# Update an existing bank account balance and save it to the file
def update_bank_acc(user, amount, action="deposit"):
    data = get_bank_data()
    account_found = False
    
    for account in data:
        if account['user'] == user:
            account_found = True
            if action == "deposit":
                account['balance'] += amount
            elif action == "withdraw":
                if account['balance'] >= amount:
                    account['balance'] -= amount
                else:
                    print(f"Insufficient balance for {user}.")
                    return
            break
    
    if account_found:
        save_bank_data(data)
        print(f"Account for {user} updated.")
    else:
        print(f"No account found for {user}.")

# Display the account balance
def display_balance(user):
    data = get_bank_data()
    for account in data:
        if account['user'] == user:
            print(f"Balance for {account['user']}: {account['balance']}")
            return
    print(f"No account found for {user}.")

# Main program with menu options
def main():
    while True:
        print("\nBanking System Menu:")
        print("1. Create Bank Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Balance")
        print("5. Delete Bank Account")
        print("6. Exit")

        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        match option:
            case 1:
                user = input("Enter the name for the account: ")
                initial_balance = int(input("Enter initial deposit amount: "))
                create_bank_acc(user, initial_balance)

            case 2:
                user = input("Enter the account name to deposit to: ")
                amount = int(input("Enter the amount to deposit: "))
                update_bank_acc(user, amount, action="deposit")

            case 3:
                user = input("Enter the account name to withdraw from: ")
                amount = int(input("Enter the amount to withdraw: "))
                update_bank_acc(user, amount, action="withdraw")

            case 4:
                user = input("Enter the account name to display balance: ")
                display_balance(user)

            case 5:
                user = input("Enter the account name to delete: ")
                delete_bank_acc(user)

            case 6:
                print("Exiting the banking system. Goodbye!")
                break

            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
