# pylint: disable=missing-docstring

from classes.conversion_item import ConversionItem
from classes.conversion_history import ConversionHistory

# This function is testing the write json file to save conversion
def test_save_conversion():
    """
    Tests saving and loading a conversion item using ConversionHistory.

    Ensures that a conversion item is saved to the history, the history is 
    cleared before the test, and the saved item matches the original.
    """
    conversion_item = ConversionItem("AUD", "USD", 200, 0.5000, "Testing")
    # Using test json file
    conversion_history = ConversionHistory("tests/test_conversion_history.json")

    # clears the json file
    conversion_history.clear()

    # Save the conversion item
    conversion_history.save_conversion(conversion_item)

    # Load and verify the saved items
    saved_items = conversion_history.load_history()
    assert len(saved_items) == 1

    saved_item = saved_items[0]
    assert saved_item.description == conversion_item.description
