"""This class module converts the currencies using a given exchange rate"""

class CurrencyConverter:
    """
    Purpose:
        This class is used to convert a given amount of currency based on
        the exchange rate.

    Attributes:
        rate: The exchange rate used for conversion.

    Methods:
        __init__(rate):
            Initialises the CurrencyConverter with the given exchange rate.

        convert(amount):
            Converts the given amount using the exchange rate.
    
    Example:
        converter = CurrencyConverter(rate=0.85)  # Initialise with an exchange rate of 0.85
        result = converter.convert(100)  # Convert value of 100  
        print(result)  # Output: 85.0
    """

    def __init__(self, rate):
        """
        Initialises with the given exchange rate.

        Args:
            rate: The exchange rate for the conversion.
        
        Example:
            converter = CurrencyConverter(rate=0.85)
            print(converter.rate)  # Output: 0.85
        """
        self.rate = rate

    def convert(self, amount):
        """
        Converts the given amount using the exchange rate.

        Args:
            amount: Amount to convert.

        Returns:
            Converted amount.

        Examples:
            converter = CurrencyConverter(rate=0.85)
            result = converter.convert(100)
            print(result)  # Output: 85.0
        """
        return self.rate * amount
