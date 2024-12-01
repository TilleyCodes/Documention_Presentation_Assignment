# pylint: disable=missing-docstring

# This class calcutors the conversion using rate and amount
class CurrencyConverter:
    def __init__(self, rate):
        self.rate = rate

    def convert(self, amount):
        return self.rate * amount
