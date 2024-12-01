# pylint: disable=missing-docstring
# pylint: disable=line-too-long

import json
from classes.conversion_item import ConversionItem

# This class is a composition of ConversionItem and is responsible for saving and loading a conversion history to a JSON file
class ConversionHistory():
    def __init__(self, file):
        self.file = file

    def save_conversion(self, conversion_item):
        conversion_history = self.load_history()
        conversion_history.append(conversion_item)

        # Convert ConversionItem list to Dictionary list for saving as JSON
        json_data = []
        for item in conversion_history:
            json_data.append(item.json_dict())

        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4)

    # This function clears the data from the json file
    def clear(self):
        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump([], json_file, indent=4)

    # This function returns a list of ConversionItem
    def load_history(self):
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
        