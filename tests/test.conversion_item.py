# pylint: disable=line-too-long

""" This module tests the ConversionItem class to:
- convert user input to JSON dictionary
- the return f-string output the conversion item
"""

# Importing colored for text formating
# Source: https://pypi.org/project/colored/
# Purpose: To style the text terminal output in different colours and background
from colored import Fore, Style
# Importing ConventionItem class
# Source: local module - classes/conversion_item.py
# Purpose: To capture the from_currency, to_currency, amount, rate, and description of the conversion item
from classes.conversion_item import ConversionItem

def test_conversion_item_json():
    """
    Tests the json_dict() method of the ConversionItem class.

    Ensures the method correctly converts a ConversionItem instance 
    into a dictionary with the expected keys and values.

    Examples:
        conversion_item = ConversionItem("AUD", "USD", 200, 0.5000, "Testing")
        result = conversion_item.json_dict()
        assert result["from_currency"] == "AUD"
        assert result["to_currency"] == "USD"
        assert result["amount"] == 200
        assert result["rate"] == 0.5000
        assert result["description"] == "Testing"
    """
    conversion_item = ConversionItem("AUD", "USD", 200, 0.5000, "Testing")
    diction = conversion_item.json_dict()
    assert diction["from_currency"] == "AUD"
    assert diction["to_currency"] == "USD"
    assert diction["amount"] == 200
    assert diction["rate"] == 0.5000
    assert diction["description"] == "Testing"

def test_conversion_item_str():
    """
    Tests the string representation (__str__) of the ConversionItem class.

    Ensures the __str__ method returns the correct formatted string
    for a given ConversionItem instance.

    Example:
        conversion_item = ConversionItem("AUD", "USD", 200, 0.5000, "Testing")
        result = str(conversion_item)
        expected = f"{Fore.white}Converting{Style.reset} {Fore.blue}200.00 AUD{Style.reset} {Fore.white}at the rate of{Style.reset} {Fore.cyan}0.5{Style.reset} {Fore.white}is equivalent to{Style.reset} {Fore.blue}100.00 USD{Style.reset} {Fore.white}-{Style.reset} {Fore.green}Testing{Style.reset}"
        assert result == expected
    """
    conversion_item = ConversionItem("AUD", "USD", 200, 0.5000, "Testing")
    input_str = f"{conversion_item}"
    assert input_str == f"{Fore.white}Converting{Style.reset} {Fore.blue}200.00 AUD{Style.reset} {Fore.white}at the rate of{Style.reset} {Fore.cyan}0.5{Style.reset} {Fore.white}is equivalent to{Style.reset} {Fore.blue}100.00 USD{Style.reset} {Fore.white}-{Style.reset} {Fore.green}Testing{Style.reset}"
