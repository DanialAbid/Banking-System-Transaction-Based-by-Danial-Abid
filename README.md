﻿# Banking-System-Transaction-Based-by-Danial-Abid
# Banking System (Transaction Validation)

This project is a dynamic Banking System model that leverages **formal methods** and the **Z3 theorem prover** to ensure system correctness. It includes features for adding and removing transactions, validating system constraints, and maintaining transaction history while preventing invalid states.

---

## **Project Overview**

The Banking System validates transactions while adhering to the following constraints:
- **No Overdraft**: The account balance must never be negative.
- **Unique Transaction IDs**: All transactions must have unique identifiers.
- **Positive Transaction Amounts**: Only positive transaction amounts are allowed.
- **Dynamic Constraints**: The system dynamically updates and verifies constraints after each modification.

This implementation is designed to demonstrate the importance of **formal verification** in preventing errors and ensuring system reliability.

---

## **Features**

- Add transactions dynamically.
- Remove transactions by ID.
- Validate constraints in real-time using Z3.
- Prevent invalid states, such as:
  - Duplicate transaction IDs.
  - Negative transaction amounts.
  - Overdrafts.

---

## **System Requirements**

- Python 3.7 or above
- Z3 Theorem Prover (`z3-solver` package)

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/banking-system-z3.git
   cd banking-system-z3
