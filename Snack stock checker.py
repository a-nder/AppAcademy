stock = {
    "Chips": 8,
    "Biscuits": 6,
    "Chocolate": 10,
    "Popcorn": 5
}

stock_item = input("Enter item to check: ").title()

if stock_item in stock:
    number = stock[stock_item]
    print(f"Found! {stock_item} has {number} in stock.")
else:
    print("Not found.")