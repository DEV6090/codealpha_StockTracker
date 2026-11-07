# CodeAlpha_StockTracker

A console stock portfolio tracker built for **CodeAlpha Python Programming Internship – Task 2**.

## Features
- Hardcoded price dictionary (AAPL, TSLA, GOOG, MSFT, AMZN)
- Enter stock names and quantities in a loop
- Input validation for unknown symbols and invalid quantities
- Entering the same stock twice adds the quantities together
- Aligned table showing quantity, price, and value per stock, plus the total
- Optional save to `.txt` or `.csv` (or both)
- `list` command to see available stocks

## Concepts Used
| Concept | Where |
|---|---|
| Dictionaries | `PRICES`, `holdings` |
| Input/output | `collect_holdings()`, `main()` |
| Arithmetic | `calculate_portfolio()` |
| File handling | `save_txt()`, `save_csv()` (with the `csv` module) |
| Functions | One function per job |
| Exception handling | `int()` conversion, `try/except` around `input()` |
| String formatting | f-strings and alignment in `format_table()` |

## Project Structure
```
CodeAlpha_StockTracker/
├── stock_tracker.py        # main program
├── test_stock_tracker.py   # unit tests
├── README.md
└── .gitignore
```

## How to Run
Requires Python 3.8+ and no external libraries.

```bash
python stock_tracker.py
```

Run the tests:

```bash
python -m unittest test_stock_tracker.py -v
```

## Sample Run
```
=== Stock Portfolio Tracker ===

Stock symbol: aapl
Quantity: 10
  Added 10 x AAPL
Stock symbol: tsla
Quantity: 5
  Added 5 x TSLA
Stock symbol: done

Stock      Qty      Price          Value
----------------------------------------
AAPL        10       $180         $1,800
TSLA         5       $250         $1,250
----------------------------------------
Total investment:                 $3,050
```

## Author
Devansh Dwivedi– CodeAlpha Python Programming Intern
