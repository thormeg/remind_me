"""Class used for parsing and returning JSON data."""
from datetime import datetime
import json
import pdb

class JsonParser():
    def read(self):
        with open("remind_me/data/data.json", "r") as f:
            data = json.load(f)
        return data

    def write(self, data):
        output = json.dumps(data, indent=4)
        with open("data/data.json", "w") as f:
            f.write(output)

        
        
if __name__ == '__main__':
    jp = JsonParser()
    data = jp.read()
    jp.write(data)