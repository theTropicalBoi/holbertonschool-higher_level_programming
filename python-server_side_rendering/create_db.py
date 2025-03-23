import sqlite3

def create_database():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    cursor.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
        (1, 'Mosin', 'Bolt Action', 499.99),
        (2, 'SVT-40', 'Automatic Rifle', 749.99),
        (3, 'Chauchat', 'Machinegun', 1299.99)
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_database()