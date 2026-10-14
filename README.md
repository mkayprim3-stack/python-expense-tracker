# Expense Tracker 💰

A command-line expense tracker built with Python that helps users record expenses, organize spending by category, and monitor their total spending.

## ✨ Features

- **Add Expenses:** Record an expense with a description, amount, and category.
- **View Expenses:** Display all recorded expenses with amounts formatted in Nigerian naira (₦).
- **Total Spending:** Calculate the total amount spent.
- **Category Summaries:** See spending totals for each category.
- **Custom Categories:** Create your own category when the predefined options don't fit.
- **Delete Expenses:** Remove individual expenses.
- **Clear All Expenses:** Clear all recorded expenses with a confirmation prompt.
- **Persistent Storage:** Save expenses in a JSON file so they remain available between sessions.
- **Input Validation:** Reject empty descriptions, invalid amounts, non-positive amounts, and fractions of a kobo.
- **Data Validation:** Detect corrupted JSON and invalid expense data structures.

## 🛠️ Technologies Used

- **Python** — application logic
- **JSON** — expense data storage
- **`decimal`** — precise monetary input handling
- **`os`** — file and path management

## 🚀 Getting Started

### Requirements

- Python 3 installed on your computer.

### Installation and Usage

1. Clone this repository or download its files.
2. Open the project folder in your terminal or code editor.
3. Run the application:

   ```bash
   expense_tracker.py
   ```

   If your Python file has a different name, replace `expenses.py` with its actual filename.

4. Follow the on-screen menu to manage your expenses.

## 💾 Data Storage

The application stores expenses in `expenses.json`, located in the same folder as the Python script.

- Expense data is saved when an expense is added, deleted, or when all expenses are cleared.
- Saved expenses remain available when the program is restarted.
- If the data file contains invalid JSON or an invalid structure, the application displays an error and stops instead of continuing with potentially damaged data.

**Important:** Back up your `expenses.json` file if you want to preserve your personal expense records.

## 📚 What I Learned

Building this project helped me practise:

- Python conditionals, loops, lists, and dictionaries.
- User input and input validation.
- Working with JSON files.
- Reading and writing persistent data.
- File paths using `os.path`.
- Handling invalid JSON and validating stored data.
- Using `Decimal` for monetary input and converting naira amounts into integer kobo.
- Debugging indentation, file-path, and control-flow errors.

## 🔮 Future Improvements

Potential future additions include:

- Recording the date of each expense.
- Filtering expenses by date or category.
- Exporting summaries to CSV.
- Adding a graphical user interface.

---

**Version:** 1.0  
**Language:** Python  
**Application Type:** Command-line expense tracker
