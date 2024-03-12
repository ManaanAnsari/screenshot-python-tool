import json

def read_config():
    with open('config.json', 'r') as file:
        config_data = json.load(file)
    return config_data


def save_config(config_data):
    with open('config.json', 'w') as file:
        json.dump(config_data, file)