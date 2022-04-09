import sqlite3

conn = sqlite3.connect('animelist2.sqlite')
cur = conn.cursor()



cur.execute('''CREATE TABLE IF NOT EXISTS Production
            (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, p_name TEXT)''')

i_production = input('Insert production: ')
cur.execute('''INSERT INTO Production (p_name) VALUES (?)''', (i_production))
f_production = cur.execute("SELECT id From Production WHERE p_name = ?", [i_production]).fetchone()[0]

i_title='Graz'
f_genre='oldies'
f_production='long'
f_year=1940
cur.execute('''INSERT INTO Title (t_name, genre_id, production_id, year_id )
            VALUES (?,?,?)''', (i_title, f_genre, f_production, f_year ))
