import json
import os

FILE_NAME = "data.json"


def load_data():
    """Load investment data from JSON file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []


def save_data(data):
    """Save investment data to JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)


def add_investment():
    """Add a new investment entry."""
    investment_type = input("Investment type (stock, crypto, etc.): ").strip()
    name = input("Asset name: ").strip()

    while True:
        try:
            quantity = float(input("Quantity: "))
            break
        except ValueError:
            print("Please enter a valid number for quantity.")

    while True:
        try:
            purchase_price = float(input("Purchase price per unit: "))
            break
        except ValueError:
            print("Please enter a valid number for purchase price.")

    investment = {
        "type": investment_type,
        "name": name,
        "quantity": quantity,
        "purchase_price": purchase_price
    }

    data = load_data()
    data.append(investment)
    save_data(data)
    print(f"Investment '{name}' added successfully!")


def view_investments():
    """Display all investment entries."""
    data = load_data()
    if not data:
        print("No investment data found.")
        return

    print("\n=== Investment Portfolio ===")
    for idx, item in enumerate(data, 1):
        total_value = item['quantity'] * item['purchase_price']
        print(
            f"{idx}. {item['name']} ({item['type']} - {item['quantity']} units x ${item['purchase_price']:.2f} = ${total_value:.2f})")


def main():
    """Main menu loop for the CLI app."""
    while True:
        print("\n=== Investment CLI App ===")
        print("1. Add Investment")
        print("2. View Investments")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            add_investment()
        elif choice == "2":
            view_investments()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
