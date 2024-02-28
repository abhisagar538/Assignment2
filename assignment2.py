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
    ('Rakshitha', '8073889241','ragp21ec@cmrir.ac.in'),
    ('Chirag','8073889241', 'chirag@gmail.com'),
    ('Sanyog','8073889241', 'sanyog@gmail.com'),
    ('Reyansh','8073889241 ','reyansh@gmail.com'),
    ('Mamtha','8073889241 ','mamtha@gmail.com')
]

cursor.executemany('''INSERT INTO users (name, cell, email) VALUES (?, ?, ?)''', user_data)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
