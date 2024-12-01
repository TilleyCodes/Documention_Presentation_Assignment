# pylint: disable=missing-docstring

from classes.currency_converter import CurrencyConverter

#This function is testing the conversion
def test_convert():
    conversion_rate = CurrencyConverter(0.5000)
    converting_amount = conversion_rate.convert(200)
    assert converting_amount == 200 * 0.5000
