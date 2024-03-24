"""
Module containing the FinanceManager class for the Personal Finance Manager
application.
FinanceManager handles the management of financial transactions including
adding, listing, saving, and loading transactions.
"""

import csv
import os
from datetime import datetime


class FinanceManager:
    def __init__(self, file_name):
        """
        Initialize a new FinanceManager object with an empty list of
        transactions.
        """
        # Use os.path.join to construct the file path in an OS-agnostic way
        self._file_path = os.path.join(os.getcwd(), file_name)
        self.transactions = self._load_transactions()
    
    def _load_transactions(self):
        """
        Load transactions to the list.
        The user input will be appended.
        """
        try:
            with open(self._file_path, mode = 'r', newline = '') as file:
                reader = csv.DictReader(file)
                return [row for row in reader if row]  # Ensures non-empty rows
        except FileNotFoundError:
            return []
    
    def add_transaction(self, transaction):
        """
        Add a transaction to the list.
        The user input will be appended.
        :rtype: object
        """
        if self._validate_date(transaction['Date']):
            self.transactions.append(transaction)
            self._save_transactions()
        else:
            raise ValueError(
                'Transaction date is in the future. Please enter a valid date.'
                )
    
    def _save_transactions(self):
        """
        Save transactions to a CSV file.
        filename is a parameter for the name of the file to save/update the
        transactions.
        """
        with open(self._file_path, mode = 'w', newline = '') as file:
            # Updated to exclude 'Description'
            fieldnames = ['Date', 'Amount', 'Category']
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            for transaction in self.transactions:
                writer.writerow(transaction)
    
    def _validate_date(self, date_str):
        """
        Validate that the day is not in the future.
        """
        transaction_date = datetime.strptime(date_str, '%Y-%m-%d')
        return transaction_date <= datetime.now()
    
    def list_transactions(self):
        """
        List all transactions.
        """
        return self.transactions
    
    def __repr__(self):
        """
        The __repr__ method in the FinanceManager class provides an official
        string representation of the object, making it more informative and
        useful for debugging. It returns a string indicating the class name
        and the current number of transactions it is managing.
        """
        return (f'FinanceManager managing {len(self.transactions)} '
                f'transactions.')
    
    def __len__(self):
        """
        The __len__ method allows the object to respond to the len()
        function call. In this context, it returns the total number of
        transactions managed by the FinanceManager, making it act like a
        collection or a container of transactions.
        """
        return len(self.transactions)


# Unit Tests

if __name__ == "__main__":
    fm = FinanceManager(
        'MOCK_DATA.csv'
        )  # Points to the actual CSV file with pre-existing data
    initial_len = len(
        fm
        )  # Capture the initial length before adding a new transaction
    
    # Add a new transaction
    fm.add_transaction(
        {
            'Date': '2024-01-01', 'Amount': '100', 'Category': 'Groceries'
            }
        )
    
    # Assert that the length has increased by 1
    assert len(
        fm
        ) == initial_len + 1, ("The length of transactions should have "
                               "increased by 1.")
    
    # Assert that the last transaction added matches the expected category
    assert fm.transactions[-1][
               'Category'] == 'Groceries', ("The category of the last added "
                                            "transaction should be "
                                            "'Groceries'.")
    
    print("All tests passed.")
