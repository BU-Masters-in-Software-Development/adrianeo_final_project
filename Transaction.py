"""
Module containing the Transaction class for the Personal Finance Manager
application.
Each Transaction object represents a financial transaction with attributes
for date, amount, category, and description.
"""

from datetime import datetime


class Transaction:
    def __init__(self, date, amount, category):
        """
        Initialize a new Transaction object.
        The transaction date is in YYYY-MM-DD format
        I am using float for transaction amounts
        Category is a string
        """
        # %Y-%m-%d (e.g., 2024-02-25)
        # Private attribute
        self._date = (datetime.strptime(date, '%Y-%m-%d')
                      .strftime('%Y-%m-%d'))
        self.amount = amount
        self.category = category
    
    # Private method
    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    
    def __str__(self):
        return (f"Date: {self._date}, Amount: {self.amount}, Category: "
                f"{self.category}")
    
    def __add__(self, other):
        if isinstance(other, Transaction):
            return self.amount + other.amount
        else:
            raise ValueError("Can only add another Transaction.")
    
    @property
    def date(self):
        return self._date


# Unit tests
if __name__ == "__main__":
    transaction1 = Transaction(
        "2023-12-31", 50.0,
        "Groceries"
        )
    transaction2 = Transaction(
        "1995-06-14", 25.0,
        "Utilities"
        )
    
    print(transaction1)  # Test __str__ method
    print(transaction2)  # Test __str__ method
    
    # Test __add__ method
    total_amount = transaction1 + transaction2
    assert total_amount == 75.0, "The total amount should be 75.0"
    
    print("All tests passed.")
