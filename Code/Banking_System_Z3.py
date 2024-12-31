from z3 import *

class BankingSystemZ3:
    def __init__(self, initial_balance):
        self.initial_balance = initial_balance
        self.transactions = {}  # Dictionary to store transactions {id: amount}
        self.solver = Solver()

    def add_transaction(self, txn_id, amount):
        """Add a transaction with a unique ID."""
        if txn_id in self.transactions:
            print(f"Transaction ID {txn_id} already exists. Try again with a unique ID.")
            return
        
        self.transactions[txn_id] = amount
        print(f"Transaction {txn_id} added: Amount = {amount}")
        self._update_constraints()

    def remove_transaction(self, txn_id):
        """Remove a transaction by ID."""
        if txn_id not in self.transactions:
            print(f"Transaction ID {txn_id} does not exist.")
            return
        
        del self.transactions[txn_id]
        print(f"Transaction {txn_id} removed.")
        self._update_constraints()

    def check_constraints(self):
        """Check if the current system satisfies all constraints."""
        if self.solver.check() == sat:
            print("All constraints satisfied. Final state:")
            model = self.solver.model()
            print(f"Final Balance: {model[self.balance]}")
        else:
            print("Constraints not satisfied. Possible issues with transactions.")

    def _update_constraints(self):
        """Rebuild the Z3 model and update constraints based on current transactions."""
        self.solver.reset()  # Clear the previous constraints

        # Create Z3 variables
        self.balance = Int('balance')
        self.solver.add(self.balance >= 0)  # Balance must not be negative

        # Add constraints for all transactions
        balance_expr = self.initial_balance
        for txn_id, amount in self.transactions.items():
            txn_var = Int(f'txn_{txn_id}')
            self.solver.add(txn_var == amount)  # Set transaction amount
            self.solver.add(txn_var > 0)  # Transactions must have positive amounts
            balance_expr += amount  # Update balance expression
        
        # Set final balance constraint
        self.solver.add(self.balance == balance_expr)

# Example Usage
if __name__ == "__main__":
    # Initialize system with an initial balance of 1000
    banking_system = BankingSystemZ3(initial_balance=1000)

    # Dynamic interaction
    while True:
        print("\nMenu:")
        print("1. Add Transaction")
        print("2. Remove Transaction")
        print("3. Check Constraints")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            txn_id = input("Enter transaction ID: ")
            amount = int(input("Enter transaction amount: "))
            banking_system.add_transaction(txn_id, amount)
        elif choice == "2":
            txn_id = input("Enter transaction ID to remove: ")
            banking_system.remove_transaction(txn_id)
        elif choice == "3":
            banking_system.check_constraints()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
