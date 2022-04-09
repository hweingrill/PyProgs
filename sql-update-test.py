import sqlite3
import random

conn = sqlite3.connect('testing.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS testing(Name TEXT, Telephone TEXT, ID REAL)")

column = input("Column to update: ")
update_user = input("Value to update: ")
field_name = input("Where field name equal to: ")
value = input("Value: ")

c.execute("INSERT INTO testing (name, Telephone, ID) VALUES (?,?,?)", (update_user, field_name, value))
conn.commit()
data = c.execute('''SELECT * FROM testing''')

for row in data:
    print(row)


#c.execute("UPDATE testing SET {3} = ? WHERE {3} = ?".format(column, update_user, field_name, value))
#c.execute("UPDATE testing SET {2} = ? WHERE ? = ?".format(column, update_user, field_name, value))
c.execute("UPDATE testing (name, Telephone, ID) VALUES (?,?,?)", (update_user, field_name, value))

conn.commit()
conn.close()

