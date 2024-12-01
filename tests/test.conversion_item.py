# pylint: disable=missing-docstring
# pylint: disable=line-too-long

from colored import Fore, Style
from classes.conversion_item import ConversionItem

# This function is testing the conversion_item JSON dictionary
def test_conversion_item_json():
    """
    Tests the json_dict() method of the ConversionItem class.

    Ensures that the method correctly converts a ConversionItem instance 
    into a dictionary with the expected keys and values.
    """
    conversion_item = ConversionItem("AUD", "USD", 200, 0.5000, "Testing")
    diction = conversion_item.json_dict()
    assert diction["from_currency"] == "AUD"
    assert diction["to_currency"] == "USD"
    assert diction["amount"] == 200
    assert diction["rate"] == 0.5000
    assert diction["description"] == "Testing"

#This function is testing the conversion_item string message is as working
def test_conversion_item_str():
    """
    Tests the string representation (__str__) of the ConversionItem class.

    Ensures that the __str__ method returns the correct formatted string
    for a given ConversionItem instance.
    """
    conversion_item = ConversionItem("AUD", "USD", 200, 0.5000, "Testing")
    input_str = f"{conversion_item}"
    assert input_str == f"{Fore.white}Converting{Style.reset} {Fore.blue}200.00 AUD{Style.reset} {Fore.white}at the rate of{Style.reset} {Fore.cyan}0.5{Style.reset} {Fore.white}is equivalent to{Style.reset} {Fore.blue}100.00 USD{Style.reset} {Fore.white}-{Style.reset} {Fore.green}Testing{Style.reset}"
