

import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='phone_book', 
    user='postgres', 
    password='6146asem'
    )

# Create a cursor to work with the database
cur = conn.cursor()

# Delete table
cur.execute('DROP TABLE phone_book;')

conn.commit()

# Create a new table
cur.execute("""CREATE TABLE phone_book (
            name VARCHAR(255),
            phone_number VARCHAR(20)
);
""")

conn.commit()

import csv

filename = 'phone_book.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, phone_number = row
        
        # Create new students
        cur.execute(f"""INSERT INTO phone_book (name, phone_number) VALUES 
                    ('{name}', '{phone_number}');
        """)

        conn.commit()
