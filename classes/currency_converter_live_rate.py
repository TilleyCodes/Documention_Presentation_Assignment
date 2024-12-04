# pylint: disable=line-too-long

"""This class module converts the currencies using live exchange rates from exchangerates API"""

# Importing os for operating system interactions
# Source: Python Standard Library
# Purpose: To access the API key from .env file
import os
# Importing requests to make HTTP request
# Source: https://pypi.org/project/requests/
# Purpose: To send request to https://api.exchangeratesapi for the exchange rate
import requests
# Importing load_dotenv to create .env file to save API password
# Source: https://pypi.org/project/python-dotenv/
# Purpose: Loads API key from .env file OS
from dotenv import load_dotenv
# Imported colored for text formating
# Source: https://pypi.org/project/colored/
# Purpose: To style the text terminal output in different colours
from colored import Fore, Style
# Importing the CurrencyConverter class
# Source: Local module - classes/currency_converter.py
# Purpose: Converts currencies using a given exchange rate
from classes.currency_converter import CurrencyConverter

# Load the API key from the environment
load_dotenv()
API_KEY = os.getenv("EXCHANGERATES_API_KEY")

class CurrencyConverterLiveRate(CurrencyConverter):
    """
    This class Inherits from CurrencyConverter.

    Purpose:
        This class performs currency conversions using live exchange rates retrieved from an API.

    Methods:
        __init__():
            Initialises the converter with a default exchange rate of 1.

        convert_currency(from_currency, to_currency, amount):
            Converts an amount using live exchange rates.

        get_live_rate(base_currency, currency, api_key):
            Gets the live exchange rate for from and to currencies.

    Examples:
        converter = CurrencyConverterLiveRate()
        converted, rate = converter.convert_currency("USD", "EUR", 100)
        print(f"Converted: {converted}, Rate: {rate}")
    """

    def __init__(self):
        """
        Initialises the CurrencyConverterLiveRate class with a default rate of 1.
    
        Example:
            converter = CurrencyConverterLiveRate()
            print(converter.rate)  # Output: 1
        """
        super().__init__(rate=1)
        return

    def convert_currency(self, from_currency, to_currency, amount):
        """
        Converts an amount using live exchange rates.

        Args:
            from_currency: The currency code to convert from (e.g., "USD").
            to_currency: The currency code to convert to (e.g., "AUD").
            amount: The amount to be converted.

        Returns:
            Converted amount and rate, or None if the API key is missing or the rate can not retrieved.

        Example:
        converter = CurrencyConverterLiveRate()
        converted, rate = converter.convert_currency("USD", "EUR", 100)
        print(f"Converted: {converted}, Rate: {rate}")
            Converted: 85.0, Rate: 0.85
        """
        if not API_KEY:
            print(f"{Fore.white}Exchange rates API key not found. Make sure it's in the .env file.{Style.reset}")
            return

        rate = self.get_live_rate(from_currency, to_currency, API_KEY)
        if rate is None:
            return
        return (rate * amount, rate)

    def get_live_rate(self, base_currency, currency, api_key):
        """
        Gets the live exchange rate from the API.

        Args:
            base_currency: Base currency code.
            currency: Target currency code.
            api_key: API key for authentication.

        Returns:
            Exchange rate or None if the rate can not be retrieved.

        Example:
            converter = CurrencyConverterLiveRate()
            rate = converter.get_live_rate("USD", "EUR", "api_key_here")
            print(rate)  # Output: 0.85
        """
        try:
            response = requests.get(f'https://api.exchangeratesapi.io/v1/latest?access_key={api_key}&base={base_currency}', timeout=10)
            if response.status_code != 200:
                return None
            rates = response.json().get('rates')
            return rates.get(currency)
        except requests.exceptions.RequestException:
            return None
        