"""
Main script for the Personal Finance Manager application.
Provides a user interface to add, list, and save financial transactions.
"""

import os
from FinanceManager import FinanceManager
from Transaction import Transaction


def get_transaction_from_user():
    """
    Get transaction details from the user.
    Then return the transaction object based on the user's input.
    """
    date = input("Enter the transaction date (YYYY-MM-DD): ")
    amount = float(input("Enter the transaction amount: "))
    category = input("Enter the transaction category: ")
    return Transaction(date, amount, category)


def main():
    """
    Main function to run the application.
    """
    file_path = os.path.join(os.getcwd(), 'MOCK_DATA.csv')
    manager = FinanceManager(file_path)
    
    while True:
        print("\n1. Add Transaction\n2. List Transactions\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            try:
                transaction = get_transaction_from_user()
                manager.add_transaction(
                    {
                        'Date': transaction.date, 'Amount': transaction.amount,
                        'Category': transaction.category
                        }
                    )
                print("Transaction added successfully.")
            except ValueError as error:
                print(error)
        elif choice == "2":
            transactions = manager.list_transactions()
            for trans in transactions:
                print(
                    f"{trans['Date']}, {trans['Amount']}, {trans['Category']}"
                    )
        elif choice == "3":
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
    
    # Adjusted unit tests to reflect new structure without 'Description'
    test_manager = FinanceManager('test_transactions.csv')
    test_transaction = {
        'Date': '2024-01-01', 'Amount': '100', 'Category': 'Groceries',
        }
    test_manager.add_transaction(test_transaction)
    assert test_manager.transactions[-1][
               'Category'] == 'Groceries', "Category should be 'Groceries'"
    assert float(
        test_manager.transactions[-1]['Amount']
        ) == 100.0, "Amount should be 100.0"
    print("Unit tests passed.")
