import random
import datetime
"""Financial Tracker Application."""

transactions = []
income: float = 0.0
filename = f"financial_report_{random.randint(1000,9999)}.txt"  # only random number


def add_transaction(transactions: list) -> None:
    """Add expense transactions."""
    while True:
        try:
            money: float = float(input("💸 Enter amount spend: ₹"))
            category: str = input("📂 Enter category (e.g., Food, Rent, Salary): ")
            transactions.append({'amount': money, 'category': category})
            print("✅ Transaction added.")
        except ValueError:
            print("❌ Invalid input. Please enter a number for amount.")
            continue

        more = input("➕ Do you want to add more transactions? (yes/no): ").strip().lower()
        if more != 'yes':
            break


def view_reports(transactions: list) -> None:
    """View all transactions."""
    if not transactions:
        print("⚠️ No transactions to display.")
        iff = input("➕ Do you want to add transactions? (yes/no): ").strip().lower()
        if iff == 'yes':
            add_transaction(transactions)
        return

    print("\n📒 Transactions:")
    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}. 💰 Amount: ₹{transaction['amount']} | 🏷️ Category: {transaction['category']}")


def generate_report(transactions: list) -> None:
    """Generate financial summary report."""
    if not transactions:
        print("⚠️ No transactions to generate report.")
        iff = input("➕ Do you want to add transactions? (yes/no): ").strip().lower()
        if iff == 'yes':
            add_transaction(transactions)
        return

    date = datetime.datetime.now()
    total_expense = sum(t['amount'] for t in transactions)
    net_savings = income - total_expense
    print(f"\n📊 Financial Report - Generated on {date}")
    print(f"💵 Total Income: ₹{income}")
    print(f"💸 Total Expenses: ₹{total_expense}")
    print(f"💰 Net Savings: ₹{income - total_expense}")
    print("\n📂 Categories you spent on:")

    categories = set(t['category'] for t in transactions)
    for category in categories:
        category_expense = sum(t['amount'] for t in transactions if t['category'] == category)
        print(f"   • {category}: ₹{category_expense}")
    print()
    print()
    if net_savings < 0:
        print("⚠️ Warning: You are spending more than your income!")
    print("\n📝 File name for saved report will be:", filename)
    show = input("💾 Do you want to save the report to a file? (yes/no): ").strip().lower()
    if show == 'yes':
        save_reports(transactions)


def save_reports(transactions: list) -> None:
    """Save report to a text file."""
    if not transactions:
        print("⚠️ No transactions to save.")
        iff = input("➕ Do you want to add transactions? (yes/no): ").strip().lower()
        if iff == 'yes':
            add_transaction(transactions)
        return

    with open(filename, 'w', encoding="utf-8") as file:
        date = datetime.datetime.now()
        total_expense = sum(t['amount'] for t in transactions)
        net_savings = income - total_expense
        file.write(f"Financial Report - Generated on {date}\n")
        file.write(f"💵 Total Income: ₹{income}\n")
        file.write(f"💸 Total Expenses: ₹{total_expense}\n")
        file.write(f"💰 Net Savings: ₹{income - total_expense}\n\n")
        file.write("📒 Transactions:\n")
        for i, transaction in enumerate(transactions, start=1):
            file.write(f"{i}. 💰 Amount: ₹{transaction['amount']} | 🏷️ Category: {transaction['category']}\n")
        if net_savings < 0:
            file.write("⚠️ Warning: You are spending more than your income!\n")
        file.write("#You are advised to keep this file safe and secure.#\n\n")
    print(f"✅ Report saved to {filename}")


def show_saved_reports() -> None:
    """Show saved financial report from file."""
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            content = file.read()
            print("\n📂 Saved Financial Report:")
            print(content)
            return
    except FileNotFoundError:
        print("❌ No saved report found.")

    save = input("💾 Do you want to save the report? (yes/no): ").strip().lower()
    if save == 'yes':
        save_reports(transactions)


def main() -> None:
    """Main application loop."""
    global income
    print("---- 💼 Welcome to the Financial Tracker App! 💼 ----")
    try:
        income = float(input("💵 Please enter your income: ₹"))
    except ValueError:
        print("❌ Invalid input. Please enter a numeric value for income.")
        return

    while True:
        print("\n📌 Menu:")
        print("1️⃣ Add Expenses")
        print("2️⃣ View Expenses")
        print("3️⃣ Generate Report")
        print("4️⃣ Save All Reports and Expenses")
        print("5️⃣ Show Saved Reports and Expenses")
        print("6️⃣ Exit")
        choice = input("👉 Choose an option (1-6): ")

        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            view_reports(transactions)
        elif choice == '3':
            generate_report(transactions)
        elif choice == '4':
            save_reports(transactions)
        elif choice == '5':
            show_saved_reports()
        elif choice == '6':
            print("🙏 Thank you for using the Financial Tracker App! 👋")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


main()