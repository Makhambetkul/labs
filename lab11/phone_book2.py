import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='phone_book2', 
    user='postgres', 
    password='6146asem'
    )
# Create a cursor to work with the database
cur = conn.cursor()

# Delete table
cur.execute('DROP TABLE phone_book2;')

conn.commit()

# Create a new table
cur.execute("""CREATE TABLE phone_book2 (
            id VARCHAR(20),
            name VARCHAR(255),
            phone_number VARCHAR(20)
);
""")

conn.commit()

cur.execute("""INSERT INTO phone_book2 (id, name, phone_number) VALUES
            ('1', 'Assem', '+7759560235'),
            ('2', 'Nurdana', '+7078430295'),
            ('3', 'Samal', '+7783597014');
            """)

conn.commit()

#Task 1
def searching(pattern):
    query="SELECT id, name, phone_number FROM phone_book2 WHERE id LIKE %s OR name LIKE %s OR phone_number LIKE %s;"
    cur.execute(query, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))

    rows=cur.fetchall()

    return rows

pattern=input()
result=searching(pattern)
for row in result:
    print(row)

#Task 5
deleting_name=input()
cur.execute("DELETE FROM phone_book2 WHERE name = %s;", (deleting_name,))
conn.commit()

#Task 2
new_id=input()
new_name=input()
new_phone_number=input()
cur.execute("INSERT INTO phone_book2 (id, name, phone_number) VALUES (%s, %s, %s)", (new_id, new_name, new_phone_number,))
conn.commit()