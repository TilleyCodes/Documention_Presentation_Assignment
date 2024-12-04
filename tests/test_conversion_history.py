"""This module tests ConversionItem and ConversionHistory classes to:
- ensure the converted item is saved, cleared and loaded in JSON file.
"""

# Importing the ConversionItem class
# Source: Local module - classes/conversion_item.py
# Purpose: To capture currency conversion item currencies, amount, rate, and description
from classes.conversion_item import ConversionItem
# Importing the ConversionHistory class
# Source: Local module - classes/conversion_history.py
# Purpose: Saving, retrieving, and clearing currency conversion history in a JSON file
from classes.conversion_history import ConversionHistory

def test_save_conversion():
    """
    Tests saving and loading a conversion item using ConversionHistory.

    Ensures a conversion item is saved to the history, the history is 
    cleared before the test, and the saved item matches the original.

    Example:
        conversion_item = ConversionItem("AUD", "USD", 200, 0.5000, "Testing")
        conversion_history = ConversionHistory("tests/test_conversion_history.json")
        conversion_history.clear()
        conversion_history.save_conversion(conversion_item)
        saved_items = conversion_history.load_history()
        assert len(saved_items) == 1
        assert saved_items[0].description == "Testing"
    """
    conversion_item = ConversionItem("AUD", "USD", 200, 0.5000, "Testing")
    conversion_history = ConversionHistory("tests/test_conversion_history.json")

    # Clear the json file and save the conversion item
    conversion_history.clear()
    conversion_history.save_conversion(conversion_item)

    # Load and verify the saved items
    saved_items = conversion_history.load_history()
    assert len(saved_items) == 1

    saved_item = saved_items[0]
    assert saved_item.description == conversion_item.description
