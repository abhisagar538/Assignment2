import sqlite3

# Connect to SQLite database (will create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    cell TEXT NOT NULL,
                    email TEXT NOT NULL
                )''')

# Insert values into the table
user_data = [
    ('John Doe', '9876541320','john@example.com'),
    ('Jane Smith','9842154644', 'jane@example.com'),
    ('Bob Johnson','9854652132', 'bob@example.com'),
    ('Adam Leach','8754213265','adam@example.com'),
    ('Jack Paul','9854876532','jackp@example.com')
]

cursor.executemany('''INSERT INTO users (name, cell, email) VALUES (?, ?, ?)''', user_data)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
