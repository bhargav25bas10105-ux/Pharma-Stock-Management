## 💊 PHARMA MANAGER

This is a simple console-based inventory and sales management system for a small pharmacy. It allows for tracking stock, managing prices, processing sales, and generating basic reports, including alerts for low stock and expired/soon-to-expire items.

### 📋 Features

  * **Inventory Management:** Add, update, view, and delete items from stock.
  * **Stock/Price Update:** Modify item quantity and price.
  * **Expiry Alerts:** Automatically displays alerts for:
      * **\!\!EXPIRED\!\!**: Item is past its expiry date.
      * **Exp Soon**: Item expires within the next 90 days.
      * **\!\!BAD DATE\!\!**: Expiry date format is invalid.
  * **Low Stock Alert:** Displays "LOW" if an item's quantity falls below the reorder level (default: 10).
  * **Sales Processing:** Process interactive sales, update inventory stock, and generate a simple invoice/log.
  * **Sales Report:** Generate daily and monthly revenue reports.

### 🚀 Getting Started

#### Prerequisites

  * Python 3.x

#### Installation

1.  Save the provided Python code as `project.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.

#### Usage

Run the script from your terminal:

```bash
python project.py
```

The system will start and present a menu of options:

```
PHARMA MANAGER
1: View | 2: Add | 3: Update | 4: Del | 5: Sale | 7: Report | 8: Exit
Choice:
```

### ⚙️ Menu Options

| Choice | Description | Function |
| :---: | :--- | :--- |
| **1** | View Inventory | Displays all items, quantity, price, expiry, and any alerts (LOW, EXPIRED, Exp Soon). |
| **2** | Add Item | Adds a new medicine/item to the inventory. Requires Name, Expiry Date (Y-M-D), Price, and Quantity. |
| **3** | Update Item | Modifies the price and/or quantity of an existing item. |
| **4** | Delete Item | Removes an item from the inventory by name. |
| **5** | Process Sale | Starts an interactive sales session to add items to a cart, deducts stock, and generates an invoice. |
| **7** | Sales Report | Displays total revenue for the current day and the current month. |
| **8** | Exit | Closes the program. |

### 🛠 Implementation Details

  * **Data Structures:**
      * `INV`: A list of dictionaries to store inventory items. Each dictionary contains `name`, `expiryDate`, `price`, and `quantity`.
      * `SALES`: A list of dictionaries to log sales transactions.
  * **Dependencies:** Uses the built-in `datetime` module for date calculations (expiry alerts, sales reports).
  * **Reorder Level:** The `REORDER` constant is set to `10`.
  * **Currency:** The `CUR` constant is set to `₹`.
  * **Initial Data:** The `main()` function pre-loads a few items into `INV` and a sample sale into `SALES` for testing.
