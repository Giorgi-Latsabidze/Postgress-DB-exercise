# models/database.py

import psycopg2
from config import DB_SETTINGS

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(**DB_SETTINGS)
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    def execute_query(self, query, data=None):
        try:
            self.connect()
            self.cursor.execute(query, data)
            self.connection.commit()
            self.disconnect()
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
