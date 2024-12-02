"""This class module converts the currencies using a given exchaneg rate"""

class CurrencyConverter:
    """
    Purpose:
        This class is used to convert a given amount of currency based on
        the exchange rate.

    Attributes:
        rate (float): The exchange rate used for conversion.

    Methods:
        __init__(rate):
            Initialises the CurrencyConverter with the given exchange rate.

        convert(amount):
            Converts the given amount using the exchange rate.
    """

    def __init__(self, rate):
        """
        Initialises with the given exchange rate.

        Args:
                rate (float): The exchange rate for the conversion.
        """
        self.rate = rate

    def convert(self, amount):
        """
        Converts the given amount using the exchange rate.

        Args:
            amount (float): Amount to convert.

        Returns:
            float: Converted amount.
        """
        return self.rate * amount
