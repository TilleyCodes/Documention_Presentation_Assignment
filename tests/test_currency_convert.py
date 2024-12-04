"""This module tests CurrencyConverter class to:
- ensure the converted amount is calculated corretly based on the exchange rate
"""

# Importing the CurrencyConverter class
# Source: Local module - classes/currency_converter.py
# Purpose: Performs currency conversion using a fixed exchange rate
from classes.currency_converter import CurrencyConverter

def test_convert():
    """
    Tests the convert method of the CurrencyConverter class.

    Ensures the convert method correctly calculates the converted amount 
    based on the provided exchange rate.

    Asserts:
        The converted amount matches the expected value.

    Example:
        conversion_rate = CurrencyConverter(0.5000)
        result = conversion_rate.convert(200)
        assert result == 100.0
    """
    conversion_rate = CurrencyConverter(0.5000)
    converting_amount = conversion_rate.convert(200)
    assert converting_amount == 200 * 0.5000
