import sqlite3
from sqlite3 import Error

def create_conn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print('aus def: ',e)

def main():
    database = r"konten"
    db_file = "BKonten.db"
    print(db_file, database)
    sql_create_table = """CREATE TABLE IF NOT EXISTS konten (
                          id integer PRIMARY KEY,
                          name text VARCHAR(30) NOT NULL,
                          verfüger text VARCHAR (50) NOT NULL,
                          rahmen REAL (10),
                          saldo REAL (10),
                          datum DATE NOT NULL
                          );"""

    conn = create_conn(database)       # create a database connection
    if conn is not None:
        # create konten table
        create_table(conn, sql_create_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
