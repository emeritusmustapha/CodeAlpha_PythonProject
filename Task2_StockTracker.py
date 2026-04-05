prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

print("Stock Tracker")
print("Stocks available:", list(prices.keys()))

portfolio = []

while True:
    name = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if name == "DONE":
        break
    
    if name not in prices:
        print("Stock not found. Try AAPL, TSLA, GOOGL, MSFT, or AMZN")
        continue
    
    try:
        qty = int(input("How many shares: "))
        if qty <= 0:
            print("Enter a positive number")
            continue
    except ValueError:
        print("Enter a valid number")
        continue
    
    portfolio.append([name, qty])

if len(portfolio) == 0:
    print("No stocks added")
else:
    total = 0
    print("\n--- Your Portfolio ---")
    for stock in portfolio:
        name = stock[0]
        qty = stock[1]
        cost = prices[name] * qty
        total += cost
        print(name, "-", qty, "shares @ $", prices[name], "= $", cost)
    
    print("\nTotal investment: $", total)
    
    save = input("\nSave to file? (yes/no): ").lower()
    if save == "yes" or save == "y":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Tracker Report\n")
            f.write("-------------------\n")
            for stock in portfolio:
                f.write(stock[0] + "," + str(stock[1]) + "," + str(prices[stock[0]] * stock[1]) + "\n")
            f.write("Total," + str(total))
        print("Saved to portfolio.txt")
