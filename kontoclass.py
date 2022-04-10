def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_database():
    database = r"BKonten.db"
    sql_create_konten = """ CREATE TABLE IF NOT EXISTS konten (
                          id INTEGER NOT NULL,
                          name TEXT VARCHAR(30) NOT NULL,
                          verfueger TEXT VARCHAR (50) NOT NULL,
                          rahmen REAL (10),
                          saldo REAL (10),
                          datum DATE NOT NULL
                          );"""
    sql_create_ktobeweg = """CREATE TABLE IF NOT EXISTS ktobeweg (
                          id INTEGER NOT NULL,
                          bewdat DATE not NULL,
                          einbet REAL (10),
                          ausbet REAL (10),
                          kz REAL (1),
                          saldo REAL (10) NOT NULL
                          );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_konten)
        create_table(conn, sql_create_ktobeweg)
    else:
        print("Error! cannot create the database connection.")

class Ktobeweg(object):

    def __init__(self, kontoid:int, bewdat:str, einbet=float, ausbet=float,kz=int,saldo=float):
        self.ktobewid=kontoid
        self.ktobewdat=bewdat
        self.ktobewein=einbet
        self.ktobewaus=ausbet
        self.ktobewkz=kz
        self.ktobewbet=saldo

    def _writebew(self):
        datenbank = "Bkonten.db"
        connection = None
        try:
            strSQL = f"INSERT INTO ktobeweg SET VALUES," \
                      f"id={self.ktobewid}"\
                      f"bewdat={self.ktobewdat}," \
                      f"einbet={self.ktobewein}" \
                      f"ausbet={self.ktobewaus}" \
                      f"kz={self.ktobewaus}"\
                      f"saldo={self.ktobewbet}"\
                      f" WHERE id ={self.Kontonummer}"
            with sqlite3.connect(datenbank) as connection:
                cursor = connection.cursor()
                cursor.execute(strSQL)
                connection.commit()
        except sqlite3.Error as e:
            return(e)

class Konto(object):

    def __init__(self, ktonr:int, inhaber:str, autorisiert=["Verfueger"],rahmen:float, startkap:float, kontostand:float, kontodatum:str):
        self.Kontonummer=ktonr
        self.Inhaber=inhaber
        self.Autorisiert=autorisiert
        self.Kontorahmen = rahmen
        self.Kontostand=startkap
        self.Kontodatum = kontodatum
        Konto.angelegteKonten+=1

        print(ktonr, inhaber, autorisiert, startkap)
        print(self.kontonr)

        # überprüfen, ob Konto schon vorhanden
        # wenn nicht, datenbank anlegen
        create_database()
        # konto anlegen


    def ueberweisen(self, ziel, betrag):
        if self.Kontostand - betrag < -self.Kontorahmen:
            # Deckung nicht genuegend
            return False
        else:
            self.Kontostand -= betrag
            ziel.Kontostand += betrag
            return True
        self._update()
        ziel._update()

    def einzahlen(self, betrag):
       self._read()
       self.Kontostand += betrag
       self._update()

    def auszahlen(self, betrag):
       self.Kontostand -= betrag
       self._update()

    def kontostand(self):
        return self.Kontostand

# Kontostand = public, __kontostand = privat
    def _update(self):
        datenbank = "Bkonten.db"
        connection = None
        try:
            strSQL = f"UPDATE konten SET saldo={self.Kontostand}," \
                      f"rahmen={self.Inhaber}," \
                      f"rahmen={self.Kontokorrent}" \
                      f" WHERE id ={self.Kontonummer}"
            with sqlite3.connect(datenbank) as connection:
                cursor = connection.cursor()
                cursor.execute(strSQL)
                connection.commit()
        except sqlite3.Error as e:
            return(e)

    def _read(self):
        datenbank = "Bkonten.db"
        connection = None
        try:
            strSQL = f"SELECT ktonum, ktouse, ktobere, ktorahm, ktosal, ktodat"\
                      " FROM Konto"\
                      f" WHERE id ={self.Kontonummer}"
            with sqlite3.connect(datenbank) as connection:
                cursor = connection.cursor()
                cursor.execute(strSQL)
                # (ktonum, ktouse, ktobere, ktorahm, ktosal, ktodat)
                data = cursor.fetchone()
                self.Kontonummer, self.Inhaber, self.Autorisiert, self.Kontorahmen,
                      self.Kontostand, self.Kontodatum = data

        except sqlite3.Error as e:
            return(e)
