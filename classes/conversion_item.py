# pylint: disable=line-too-long

"""This class module captures the from_currency, to_currency, amount, rate, and description of the conversion item"""

# Imported colored for text formating
# Source: https://pypi.org/project/colored/
# Purpose: To style the text terminal output in different colours
from colored import Fore, Style

class ConversionItem:
    """
    This class represents a currency conversion.

    Attributes:
        from_currency: Currency code to convert from.
        to_currency: Currency code to convert to.
        amount: Amount to convert.
        rate: Exchange rate used.
        description: Description of the conversion.
    
        Methods:
        json_dict():
            Returns the conversion data as a JSON dictionary.

        __str__():
            Returns a f-string of the conversion details.

    Examples:
        item = ConversionItem("USD", "EUR", 100, 0.85, "DEC Holiday")
        print(item)
            Converting 100.00 USD at the rate of 0.85 is equivalent to 85.00 EUR - DEC Holiday
            
        item.json_dict()
            {'from_currency': 'USD', 'to_currency': 'EUR', 'amount': 100, 'rate': 0.85, 'description': 'DEC Holiday'}
    """

    def __init__(self, from_currency, to_currency, amount, rate, description):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.rate = rate
        self.description = description

    def json_dict(self):
        """
        This function converts the ConversionItem data to JSON.

        Returns:
        A dictionary containing the conversion details.

        Example:
        item = ConversionItem("USD", "EUR", 100, 0.85, "Travel Expense")
        item.json_dict()
            {'from_currency': 'USD', 'to_currency': 'EUR', 'amount': 100, 'rate': 0.85, 'description': 'Travel Expense'}
        """
        return {
            "from_currency": self.from_currency,
            "to_currency": self.to_currency,
            "amount": self.amount, 
            "rate": self.rate,
            "description": self.description,
        }

    def __str__(self):
        """
        This function creates an f-string of the conversion details.

        Returns:
        A string showing the amount, currencies, rate, and description.

        Example:
            >>> item = ConversionItem("USD", "EUR", 100, 0.85, "Work Trip")
            >>> print(item)
            Converting 100.00 USD at the rate of 0.85 is equivalent to 85.00 EUR - Work Trip
        """
        converted_amount = self.amount * self.rate
        return f"{Fore.white}Converting{Style.reset} {Fore.blue}{self.amount:.2f} {self.from_currency}{Style.reset} {Fore.white}at the rate of{Style.reset} {Fore.cyan}{self.rate}{Style.reset} {Fore.white}is equivalent to{Style.reset} {Fore.blue}{converted_amount:.2f} {self.to_currency}{Style.reset} {Fore.white}-{Style.reset} {Fore.green}{self.description}{Style.reset}"
