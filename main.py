# main.py

from models.database import Database
from utils.file_handler import FileHandler

def insert_data(db, data):
    query = """
    INSERT INTO Books (Title, Authors, Description, Category, Publisher, Publish_Date, Price)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    for _, row in data.iterrows():
        try:
            db.execute_query(query, (
                row['Title'], row['Authors'], row['Description'], 
                row['Category'], row['Publisher'], row['Publish Date'], 
                row['Price']
            ))
            print(f"Inserted row: {row['Title']}")
        except Exception as e:
            print(f"Error inserting row: {row['Title']} - {e}")

if __name__ == "__main__":
    db = Database()
    file_handler = FileHandler('data/Books.csv')
    data = file_handler.read_csv()
    insert_data(db, data)
