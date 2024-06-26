import json
import time
import os


class DataProvider:
    @staticmethod
    def get_data(file_name):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'test_data', file_name)
        file_path = os.path.abspath(file_path)
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data

    @staticmethod
    def get_timestamp():
        return str(time.time())

    @staticmethod
    def set_data(file_name, data):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'test_data', file_name)
        file_path = os.path.abspath(file_path)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
