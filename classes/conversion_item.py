# pylint: disable=missing-docstring
# pylint: disable=line-too-long

from colored import Fore, Style

# This class stores information on the conversion
class ConversionItem:
    def __init__(self, from_currency, to_currency, amount, rate, description):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.rate = rate
        self.description = description

    # This function returns a dictionary with the conversion item data for JSON
    def json_dict(self):
        return {
            "from_currency": self.from_currency,
            "to_currency": self.to_currency,
            "amount": self.amount, 
            "rate": self.rate,
            "description": self.description,
        }

    # This function returns a formated string from item data
    def __str__(self):
        converted_amount = self.amount * self.rate
        return f"{Fore.white}Converting{Style.reset} {Fore.blue}{self.amount:.2f} {self.from_currency}{Style.reset} {Fore.white}at the rate of{Style.reset} {Fore.cyan}{self.rate}{Style.reset} {Fore.white}is equivalent to{Style.reset} {Fore.blue}{converted_amount:.2f} {self.to_currency}{Style.reset} {Fore.white}-{Style.reset} {Fore.green}{self.description}{Style.reset}"
