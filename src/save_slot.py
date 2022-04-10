import json
import os


class SaveSlot:
    def __init__(self):
        self.save_slots = [None, None]
        self.load_savings()

    def load_savings(self):
        directory = os.fsencode(os.getcwd())
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            with open(filename) as json_file:
                data = json.load(json_file)
            if filename == "save_slot1.json":
                self.save_slots[0] = data
            elif filename == "save_slot2.json":
                self.save_slots[1] = data
