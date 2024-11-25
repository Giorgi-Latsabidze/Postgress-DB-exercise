# utils/file_handler.py

import pandas as pd

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        data = pd.read_csv(self.file_path)
        # Check for correct data types and clean data
        data['Publish Date'] = pd.to_datetime(data['Publish Date'], errors='coerce')
        data['Price'] = pd.to_numeric(data['Price'], errors='coerce')
        return data
