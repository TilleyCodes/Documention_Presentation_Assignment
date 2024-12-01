# pylint: disable=missing-docstring
# pylint: disable=line-too-long

import json
from classes.conversion_item import ConversionItem

# This class is a composition of ConversionItem and is responsible for saving and loading a conversion history to a JSON file
class ConversionHistory():
    """
    This class manages the currency conversion history stored in JSON file.

    Attributes:
        file (str): Path to the JSON file for storing history.

    Methods:
        __init__(file):
            Initialises with the specified file path.

        save_conversion(conversion_item):
            Saves a ConversionItem to the file.

        clear():
            Clears all data in the file.

        load_history():
            Loads saved conversions as a list of ConversionItem objects.
    """
    def __init__(self, file):
        self.file = file

    def save_conversion(self, conversion_item):
        """
        Saves a conversion item to the history file.

        Args:
            conversion_item (ConversionItem): The conversion to save.
        """
        conversion_history = self.load_history()
        conversion_history.append(conversion_item)

        # Convert ConversionItem list to Dictionary list for saving as JSON
        json_data = []
        for item in conversion_history:
            json_data.append(item.json_dict())

        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4)

    def clear(self):
        """
        Clears all data from the history file.
        """
        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump([], json_file, indent=4)

    # This function returns a list of ConversionItem
    def load_history(self):
        """
        Loads conversion history from the file.

        Returns:
            list[ConversionItem]: List of saved conversions, or an empty list if the file is missing or inaccessible.
        """
        try:
            with open(self.file, "r", encoding="utf-8") as json_file:
                json_to_load = json.load(json_file)

            items = []
            for json_item in json_to_load:
                item = ConversionItem(
                    json_item['from_currency'],
                    json_item['to_currency'],
                    json_item['amount'],
                    json_item['rate'],
                    json_item['description']
                )
                items.append(item)
            return items
        except (FileNotFoundError, PermissionError, OSError):
            return []
        