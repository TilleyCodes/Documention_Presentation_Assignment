# pylint: disable=missing-docstring
# pylint: disable=line-too-long
# pylint: disable=invalid-name

from colored import Fore, Back, Style

from classes.conversion_history import ConversionHistory
from functions.currency_converter_functions import print_currency_codes, calculate_fx_rate, convert_with_personal_rate, convert_with_live_rate, print_conversion_history

print(f"\n{Fore.white}{Back.blue}Welcome to the Currency Converter Application!{Style.reset}\n")
print(f"{Fore.white}Please select from the options below.")

def user_menu():
    """
    This function displays the user menu with options for currency conversions and other features.

    Prompts the user to select an option by entering a corresponding number.

    Returns:
        str: The user's menu selection as a string.
    """
    print(f"\n{Fore.white}Enter{Style.reset} {Fore.green}1{Style.reset} {Fore.white}to convert currencies using live FX rate.{Style.reset}")
    print(f"{Fore.white}Enter{Style.reset} {Fore.green}2{Style.reset} {Fore.white}to convert currencies using your personalised FX rate.{Style.reset}")
    print(f"{Fore.white}Enter{Style.reset} {Fore.green}3{Style.reset} {Fore.white}to calculate the FX rate.{Style.reset}")
    print(f"{Fore.white}Enter{Style.reset} {Fore.green}4{Style.reset} {Fore.white}to view the currency code list.{Style.reset}")
    print(f"{Fore.white}Enter{Style.reset} {Fore.green}5{Style.reset} {Fore.white}to view conversion history.{Style.reset}")
    print(f"{Fore.white}Enter {Fore.green}6{Style.reset} {Fore.white}to exit.{Style.reset}\n")

    selection = input(f"{Fore.white}Please enter a number corresponding to your selection: {Style.reset}")
    print("\n")

    return selection

# instance of class ConversionHistory(json file name) to pass through below
conversion_history = ConversionHistory("data/conversion_history.json")

user_selection = ""

while user_selection != "6":
    user_selection = user_menu()

    if  user_selection =="1":
        convert_with_live_rate(conversion_history)
    elif user_selection == "2":
        convert_with_personal_rate()
    elif user_selection == "3":
        calculate_fx_rate()
    elif user_selection == "4":
        print(f"{Fore.white}Here is the list of currency codes.{Style.reset}\n")
        print_currency_codes()
        print("\n")
    elif user_selection == "5":
        print(f"{Fore.white}Here is your conversion history. {Style.reset}\n")
        print_conversion_history(conversion_history)
        print("\n")
    elif user_selection == "6":
        print(f"{Fore.white}Good-bye...{Style.reset}\n")
    else:
        print(f"{Fore.white}Invalid selection{Style.reset}")

print(f"{Fore.blue}Thank you for using the Currency Converter.{Style.reset}\n")
