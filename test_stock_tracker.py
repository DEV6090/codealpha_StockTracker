"""Run with: python -m unittest test_stock_tracker.py -v"""
import csv
import os
import tempfile
import unittest

from stock_tracker import (PRICES, parse_quantity, add_holding,
                           calculate_portfolio, format_table, save_csv)


class TestStockTracker(unittest.TestCase):
    def test_parse_quantity_valid(self):
        self.assertEqual(parse_quantity("10"), 10)

    def test_parse_quantity_invalid(self):
        for bad in ("abc", "-5", "0", "2.5", ""):
            self.assertIsNone(parse_quantity(bad))

    def test_duplicate_stock_adds_up(self):
        holdings = {}
        add_holding(holdings, "AAPL", 3)
        add_holding(holdings, "AAPL", 2)
        self.assertEqual(holdings, {"AAPL": 5})

    def test_total(self):
        rows, total = calculate_portfolio({"AAPL": 10, "TSLA": 5}, PRICES)
        self.assertEqual(total, 10 * 180 + 5 * 250)
        self.assertEqual(len(rows), 2)

    def test_table_contains_total(self):
        rows, total = calculate_portfolio({"AAPL": 10}, PRICES)
        self.assertIn("$1,800", format_table(rows, total))

    def test_csv_output(self):
        rows, total = calculate_portfolio({"MSFT": 2}, PRICES)
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "p.csv")
            save_csv(rows, total, path)
            with open(path, newline="") as f:
                data = list(csv.reader(f))
        self.assertEqual(data[0], ["Stock", "Quantity", "Price", "Value"])
        self.assertEqual(data[-1][-1], "660")


if __name__ == "__main__":
    unittest.main()
