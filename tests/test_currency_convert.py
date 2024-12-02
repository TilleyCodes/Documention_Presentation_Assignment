# pylint: disable=missing-docstring

from classes.currency_converter import CurrencyConverter

def test_convert():
    """
    Tests the convert method of the CurrencyConverter class.

    Ensures that the convert method correctly calculates the converted amount 
    based on the provided exchange rate.

    Asserts:
        The converted amount matches the expected value.
    """
    conversion_rate = CurrencyConverter(0.5000)
    converting_amount = conversion_rate.convert(200)
    assert converting_amount == 200 * 0.5000
