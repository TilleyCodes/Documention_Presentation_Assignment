# pylint: disable=missing-docstring
# pylint: disable=line-too-long

import os
import requests
from dotenv import load_dotenv
from colored import Fore, Style
from classes.currency_converter import CurrencyConverter

# Load the API key from the environment
load_dotenv()
API_KEY = os.getenv("EXCHANGERATES_API_KEY")

# This class inherits from CurrencyConverter to calculate conversion using the live FX rate
class CurrencyConverterLiveRate(CurrencyConverter):
    def __init__(self):
        super().__init__(rate=1)
        return
    def convert_currency(self, from_currency, to_currency, amount):
        if not API_KEY:
            print(f"{Fore.white}Exchange rates API key not found. Make sure it's in the .env file.{Style.reset}")
            return

        rate = self.get_live_rate(from_currency, to_currency, API_KEY)
        if rate is None:
            return
        return (rate * amount, rate)
    # This Function gets the live exchange rate from exchangeratesapi using the currency code if valid
    def get_live_rate(self, base_currency, currency, api_key):
        try:
            response = requests.get(f'https://api.exchangeratesapi.io/v1/latest?access_key={api_key}&base={base_currency}', timeout=10)
            if response.status_code != 200:
                return None
            rates = response.json().get('rates')
            return rates.get(currency)
        except requests.exceptions.RequestException:
            return None
        