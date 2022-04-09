import sqlite3
import csv

conn = sqlite3.connect('att.db')
cur = conn.cursor()
cur.execute('''create table if not exists wcards('date','time','cardid')''')
with open('sample.txt') as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        cur.execute("insert into wcards(date, time, cardid) values (?, ?, ?)",
        (row['Date'], row['Time'], row['CardID']))

data=cur.execute("SELECT * FROM wcards")
for row in data:
    print (row)
    
conn.commit() # you need to commit changes

#alternatively:

import sqlite3
import csv
conn = sqlite3.connect('att2.db')
with open('sample.txt') as f:
    rdr = csv.DictReader(f)
    data = [(row['Date'], row['Time'], row['CardID']) for row in rdr]
with conn: # using with context manager commit() is executed automaticaly
    conn.execute('''create table wcards('date','time','cardid')''')
    conn.executemany("insert into wcards (date, time, cardid) values (?, ?, ?)", data)

data=cur.execute("SELECT * FROM wcards")
for row in data:
    print (row)

    
conn.commit()    
