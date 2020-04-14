import json
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'configs/config.dev.json')

def config():
    with open(my_file) as json_file:
        config = json.load(json_file)
        return config