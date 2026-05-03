# Abdul Soda Shop | Inventory Management Logic

A Python-based CLI application inspired by the "Deli" exercise in *Python Crash Course* and themed around the popular Indian sitcom *TMKOC*. This project demonstrates the practical application of user input handling, list manipulation, and dictionary-based data mapping.

---

### 🛡️ Core Features
- **Dynamic Inventory:** Allows the operator to remove items from the "Available" list and track "Out of Stock" status in real-time.
- **Order Processing:** Iterates through a customer database (Dictionary) to verify if orders can be fulfilled.
- **Error Handling:** Implements `try-except` blocks to manage invalid user inputs and prevent program crashes.
- **State Management:** Uses `.pop()`, `.append()`, and membership testing (`in` / `not in`) to manage the shop's state.

---

### 🏗️ Technical Logic
The program operates on a three-tier check system:
1. **Invalid Items:** Checks if the requested item was ever part of the shop's menu.
2. **Stock Check:** Cross-references the customer's order against the `empty_stock` list.
3. **Fulfillment:** Triggers a success message if both logic gates are passed.

---

### 🛠️ How to Run
Ensure you have Python installed.
1. Clone the repository:
   ```bash
   git clone [https://github.com/rrbhanderi05/abdul-soda-shop.git](https://github.com/rrbhanderi05/abdul-soda-shop.git)
