# pylint: disable=missing-docstring
# pylint: disable=line-too-long

from colored import Fore, Style
from currency_codes import get_fiat_currencies
from tabulate import tabulate
from classes.conversion_item import ConversionItem
from classes.currency_converter_live_rate import CurrencyConverterLiveRate
from classes.currency_converter import CurrencyConverter

def convert_with_live_rate(conversion_history):
    """
    Performs a currency conversion using live exchange rates.

    This function prompts the user to input the amount, from currency, 
    and to currency for conversion. It uses live FX rates to calculate 
    the converted amount and displays the result. The user can also save 
    the conversion with an optional description to the conversion history.

    Args:
        conversion_history (ConversionHistory): An class that stores and manages
                                                the user's past conversions.
    """

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

    # Save this conversion to the conversion history if the user enters a description
    description = input(f"{Fore.white}Enter a short description to save to history or enter to return to main menu: {Style.reset}")
    if description != "":
        conversion_item = ConversionItem(from_currency, to_currency, amount, rate, description)
        conversion_history.save_conversion(conversion_item)

def convert_with_personal_rate():
    """
    Converts a currency value using a user-provided exchange rate.

    This function prompts the user for an FX rate, a value to convert, and whether to 
    convert to or from the base currency. Displays the converted result.
    """
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
    """
    Calculates and displays the FX rate based on user input values.

    Prompts the user to input the "from" and "to" values. Calculates the 
    exchange rate and displays the result.
    """
    from_value = get_numerical_input(f"{Fore.white}Please enter the from value to calculate the FX rate:{Fore.white} ")
    if from_value is None:
        return

    to_value = get_numerical_input(f"{Fore.white}Please enter the to value to calculate the FX rate:{Fore.white} ")
    if to_value is None:
        return
    fx_rate = 1/(from_value/to_value)
    print(f"\n{Fore.white}The FX rate is{Style.reset} {Fore.cyan}{fx_rate:.5f}{Style.reset} {Fore.white}from value{Style.reset} {Fore.blue}{from_value:.2f}{Style.reset} {Fore.white}to value{Style.reset} {Fore.blue}{to_value:.2f}{Style.reset}{Fore.white}.{Style.reset} \n")

def get_currency_codes():
    """
    Retrieves a list of currency names and codes.

    Returns:
        list: A list of [name, code] pairs for each currency.
    """
    currency_codes = []
    for currency in get_fiat_currencies():
        name = currency.name
        code = currency.code
        currency_codes.append([name, code])
    return currency_codes

def print_currency_codes():
    """
    This function displays a sorted list of currency names and codes in a table format.
    """
    currency_codes = get_currency_codes()
    currency_codes.sort()
    headers = [f"{Fore.blue}Name{Style.reset}", f"{Fore.blue}Code{Style.reset}"]
    print(tabulate(currency_codes, headers, tablefmt="rounded_outline"))

def print_conversion_history(conversion_history):
    """
    Displays the user's conversion history.

    Args:
        conversion_history (ConversionHistory): A class managing saved conversions.
    """
    conversion_items = conversion_history.load_history()
    for item in conversion_items:
        print(item)

# Helper Functions to make code DRY:

def get_numerical_input(message):
    """
    Prompts the user for a valid non-zero numerical input.

    Displays error messages for invalid or zero values and allows up to three attempts.

    Returns:
        float or None: The valid numerical input as a float, or None if the attempts fail.

    Args:
        message (str): The prompt message to display to the user.    
    """
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
    """
    Checks if a given string can be converted to a float.

    Returns:
        bool: True if the string can be converted to a float, False otherwise.

    Args:
        input_str (str): The string to check.
    """
    try:
        float(input_str)
        return True
    except ValueError:
        return False
    