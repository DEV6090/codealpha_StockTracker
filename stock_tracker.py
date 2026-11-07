#CodeAlpha Python Internship - Task 2: Stock Portfolio Tracker.
import csv
from datetime import datetime

# Hardcoded prices (USD per share), as allowed by the task brief.
PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def show_prices(prices: dict) -> None:
    """Print the available stocks and their prices."""
    print("\nAvailable stocks:")
    for symbol, price in prices.items():
        print(f"  {symbol:<6} ${price:,}")
    print()


def parse_quantity(text: str):
    """Return a positive int, or None if the text is not valid."""
    try:
        qty = int(text)
    except ValueError:
        return None
    return qty if qty > 0 else None


def add_holding(holdings: dict, symbol: str, qty: int) -> None:
    holdings[symbol] = holdings.get(symbol, 0) + qty


def calculate_portfolio(holdings: dict, prices: dict):
    rows = []
    total = 0
    for symbol, qty in holdings.items():
        price = prices[symbol]
        value = price * qty
        rows.append((symbol, qty, price, value))
        total += value
    return rows, total


def format_table(rows: list, total: int) -> str:
    width = 40
    lines = [f"{'Stock':<8}{'Qty':>6}{'Price':>11}{'Value':>15}", "-" * width]
    for symbol, qty, price, value in rows:
        lines.append(f"{symbol:<8}{qty:>6}{'$' + format(price, ','):>11}"
                     f"{'$' + format(value, ','):>15}")
    lines.append("-" * width)
    lines.append(f"{'Total investment:':<25}{'$' + format(total, ','):>15}")
    return "\n".join(lines)


def save_txt(table: str, filename: str = "portfolio.txt") -> None:
    stamp = datetime.now().strftime("%d %b %Y, %I:%M %p")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Stock Portfolio Report - {stamp}\n\n{table}\n")


def save_csv(rows: list, total: int, filename: str = "portfolio.csv") -> None:
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(rows)
        writer.writerow(["TOTAL", "", "", total])


def collect_holdings(prices: dict) -> dict:
    holdings = {}
    print("Enter a stock symbol and quantity.")
    print("Commands: 'list' shows prices, 'done' finishes.\n")

    while True:
        try:
            symbol = input("Stock symbol: ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if symbol == "DONE":
            break
        if symbol == "LIST":
            show_prices(prices)
            continue
        if symbol not in prices:
            print(f"  '{symbol}' not found. Type 'list' to see available stocks.")
            continue

        qty = parse_quantity(input("Quantity: ").strip())
        if qty is None:
            print("  Quantity must be a whole number greater than 0.")
            continue

        add_holding(holdings, symbol, qty)
        print(f"  Added {qty} x {symbol}")

    return holdings


def main() -> None:
    print("=== Stock Portfolio Tracker ===")
    show_prices(PRICES)

    holdings = collect_holdings(PRICES)
    if not holdings:
        print("No stocks entered. Nothing to calculate.")
        return

    rows, total = calculate_portfolio(holdings, PRICES)
    table = format_table(rows, total)
    print("\n" + table + "\n")

    choice = input("Save report? (txt / csv / both / no): ").strip().lower()
    if choice in ("txt", "both"):
        save_txt(table)
        print("Saved portfolio.txt")
    if choice in ("csv", "both"):
        save_csv(rows, total)
        print("Saved portfolio.csv")


if __name__ == "__main__":
    main()
