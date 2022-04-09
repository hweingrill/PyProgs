import sqlite3
                      
conn = sqlite3.connect('geek2.db')           # connection object
                      
cursor = conn.cursor()                       # cursor object

#table = """CREATE TABLE STUDENT
#(NAME VARCHAR(255),
#CLASS VARCHAR(255),
#SECTION VARCHAR(255));"""

#cursor.execute(table)

#cursor.execute('''INSERT INTO STUDENT VALUES ('Joerg', '7th', 'A')''')
#cursor.execute('''INSERT INTO STUDENT VALUES ('Eva', '8th', 'B')''')
#cursor.execute('''INSERT INTO STUDENT VALUES ('Renate', '9th', 'C')''')

print("Data Inserted in the table: ")
data = cursor.execute('''SELECT * FROM STUDENT''')
                       
for row in data:
    print(row)
                          
conn.commit()           # Commit your changes in the database 
conn.close()                      

