# pylint: disable=missing-docstring
# pylint: disable=line-too-long


from colored import Fore, Style
from currency_codes import get_fiat_currencies
from tabulate import tabulate
from classes.conversion_item import ConversionItem
from classes.currency_converter_live_rate import CurrencyConverterLiveRate
from classes.currency_converter import CurrencyConverter

# This function takes the user's input to calculate the conversion using the live FX rate
def convert_with_live_rate(conversion_history):
    amount = get_numerical_input(f"{Fore.white}Please enter the amount you wish to convert: {Style.reset}")
    if amount is None:
        return
    from_currency = input(f"{Fore.white}Please enter the 3 letter currency code you wish to convert from: {Style.reset}").upper()
    to_currency = input(f"{Fore.white}Please enter the 3 letter currency code you wish to convert to: {Style.reset}").upper()
    converter = CurrencyConverterLiveRate()

    conversion_result = converter.convert_currency(from_currency, to_currency, amount)
    if conversion_result is None:
        print(f"\n{Fore.white}Unable to convert currency from{Style.reset} {Fore.red}{from_currency}{Style.reset} {Fore.white}to{Style.reset} {Fore.red}{to_currency}{Style.reset}{Fore.white}. Please ensure your{Style.reset} {Fore.red}currency code{Style.reset} {Fore.white}is valid.{Style.reset}\n")
        return

    (converted_amount, rate) = conversion_result
    print(f"\n{Fore.white}Converting{Style.reset} {Fore.blue}{amount:.2f} {from_currency}{Style.reset} {Fore.white}at the rate of{Style.reset} {Fore.cyan}{rate}{Style.reset} {Fore.white}is equivalent to{Style.reset} {Fore.blue}{converted_amount:.2f} {to_currency}{Style.reset}{Fore.white}.{Style.reset}\n")

    description = input(f"{Fore.white}Enter a short description to save to history or enter to return to main menu: {Style.reset}")
    if description != "":
        conversion_item = ConversionItem(from_currency, to_currency, amount, rate, description)
        conversion_history.save_conversion(conversion_item)

# This function uses the FX rate input to calulate the value of the currency depending on the exchange direction
def convert_with_personal_rate():
    personal_rate = get_numerical_input(f"{Fore.white}Please enter the FX rate you received during your exchange: {Style.reset}")
    if personal_rate is None:
        return
    currency_value = get_numerical_input(f"{Fore.white}Please enter the value you wish to convert: {Style.reset}")
    if currency_value is None:
        return
    user_selection = input(f"\n{Fore.white}Do you want this value{Style.reset} {Fore.blue}{float(currency_value):.2f}{Style.reset} {Fore.white}converted to your base currency? Enter{Style.reset} {Fore.green}Y{Style.reset} {Fore.white}or{Style.reset} {Fore.red}N{Style.reset}{Fore.white}:{Style.reset} ").upper()

    if user_selection == "Y":
        converter = CurrencyConverter(rate = 1 / personal_rate)
        converted_amount = converter.convert(currency_value)
        print(f"\n{Fore.white}The value{Style.reset} {Fore.blue}{currency_value:.2f}{Style.reset} {Fore.white}with FX rate{Style.reset} {Fore.cyan}{personal_rate:.5f}{Style.reset} {Fore.white}is{Style.reset} {Fore.blue}{converted_amount:.2f}{Style.reset} {Fore.white}in your base currency.{Style.reset}\n")
    else:
        converter = CurrencyConverter(rate = personal_rate)
        converted_amount = converter.convert(currency_value)
        print(f"\n{Fore.white}The value{Style.reset} {Fore.blue}{currency_value:.2f}{Style.reset} {Fore.white}in your local currency with FX rate{Style.reset} {Fore.cyan}{personal_rate:.5f}{Style.reset} {Fore.white}is{Fore.white} {Fore.blue}{converted_amount:.2f}{Style.reset} {Fore.white}in foreign currency.{Style.reset}\n")

# This function calculates to FX rate by dividing the from_value input by the to_value input
def calculate_fx_rate():
    from_value = get_numerical_input(f"{Fore.white}Please enter the from value to calculate the FX rate:{Fore.white} ")
    if from_value is None:
        return

    to_value = get_numerical_input(f"{Fore.white}Please enter the to value to calculate the FX rate:{Fore.white} ")
    if to_value is None:
        return
    fx_rate = 1/(from_value/to_value)
    print(f"\n{Fore.white}The FX rate is{Style.reset} {Fore.cyan}{fx_rate:.5f}{Style.reset} {Fore.white}from value{Style.reset} {Fore.blue}{from_value:.2f}{Style.reset} {Fore.white}to value{Style.reset} {Fore.blue}{to_value:.2f}{Style.reset}{Fore.white}.{Style.reset} \n")

# This function creates the currency_code list by retreiving the currency name and code from currency_codes import
def get_currency_codes():
    currency_codes = []
    for currency in get_fiat_currencies():
        name = currency.name
        code = currency.code
        currency_codes.append([name, code])
    return currency_codes

# This function will print the currency code in alphabetical order
def print_currency_codes():
    currency_codes = get_currency_codes()
    currency_codes.sort()
    headers = [f"{Fore.blue}Name{Style.reset}", f"{Fore.blue}Code{Style.reset}"]
    print(tabulate(currency_codes, headers, tablefmt="rounded_outline"))

def print_conversion_history(conversion_history):
    conversion_items = conversion_history.load_history()
    for item in conversion_items:
        print(item)

# Helper Functions to make code DRY:

# This functiion asks for a non-zero numerical input and return None after 3 tries if the user doesn't enter a valid number
def get_numerical_input(message):
    error_message_numerical = f"{Fore.white}Please enter a{Style.reset} {Fore.red}numerical{Style.reset} {Fore.white}value: {Style.reset}"
    error_message_zero = f"\n{Fore.white}Please enter a{Style.reset} {Fore.red}non-zero{Style.reset} {Fore.white}value: {Style.reset}"
    tries = 0

    value = input(message)
    while (not is_float(value) or float(value) == 0) and tries < 3:
        message = error_message_numerical if not is_float(value) else error_message_zero
        value = input(message)
        tries += 1
    return float(value) if is_float(value) and float(value) != 0 else None
# This function checks the string to see if it can be converted to a number
def is_float(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False
    