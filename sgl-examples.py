# https://www.informatik-aktuell.de/betrieb/datenbanken
#    /datenbanken-mit-python-und-sqlite.html#thanksForYour Comment

import os, sys, sqlite3

# Existenz feststellen
if os.path.exists("firma.db"):
    print("Datei bereits vorhanden")
    sys.exit(0)

# Verbindung zur Datenbank erzeugen + Datensatz-Cursor erzeugen
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# Datenbanktabelle erzeugen
sql = "CREATE TABLE personen(" \
      "name TEXT, " \
      "vorname TEXT, " \
      "personalnummer INTEGER PRIMARY KEY, " \
      "gehalt REAL, " \
      "geburtstag TEXT)"
cursor.execute(sql)

# Datensatz erzeugen
sql = "INSERT INTO personen VALUES('Maier', " \
      "'Hans', 6714, 3500, '15.03.1962')"
cursor.execute(sql)
connection.commit()
sql = "INSERT INTO personen VALUES('Schmitz', " \
      "'Peter', 81343, 3750, '12.04.1958')"
cursor.execute(sql)
connection.commit()
sql = "INSERT INTO personen VALUES('Mertens', " \
      "'Julia', 2297, 3621.5, '30.12.1959')"
cursor.execute(sql)
connection.commit()

# Verbindung beenden
connection.close()

#---------------------- Listing 2: Datei sqlite_anzeigen.py

import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# SQL-Abfrage
sql = "SELECT * FROM personen"

# Kontrollausgabe der SQL-Abfrage
# print(sql)

# Absenden der SQL-Abfrage
# Empfang des Ergebnisses
cursor.execute(sql)

# Ausgabe des Ergebnisses
for dsatz in cursor:
    print(dsatz[0], dsatz[1], dsatz[2],
          dsatz[3], dsatz[4])

# Verbindung beenden
connection.close()

#--------------- Listing 3: Datei sqlite_auswaehlen.py

import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# SQL-Abfragen
# Einzelne Felder
sql = "SELECT name, vorname FROM personen"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# Auswahl mit WHERE-Klausel und Vergleichsoperator
sql = "SELECT * FROM personen " \
      "WHERE gehalt > 3600"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[3])
print()

# Auswahl mit Zeichenkette
sql = "SELECT * FROM personen " \
      "WHERE name = 'Schmitz'"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# Auswahl mit logischen Operatoren
sql = "SELECT * FROM personen " \
      "WHERE gehalt >= 3600 AND gehalt <= 3650"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[3])

# Verbindung beenden
connection.close()

#--------------- Listing 4: Datei sqlite_like.py

import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# SQL-Abfragen

# Beliebig viele beliebige Zeichen
sql = "SELECT * FROM personen WHERE name LIKE 'm%'"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# Beinhaltet ...
sql = "SELECT * FROM personen WHERE name LIKE '%i%'"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# Einzelne beliebige Zeichen
sql = "SELECT * FROM personen WHERE name LIKE 'M__er'"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])

# Verbindung beenden
connection.close()

#--------------- Listing 5: Datei sqlite_sortieren.py

import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# Sortierung absteigend
sql = "SELECT * FROM personen ORDER BY gehalt DESC"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1], dsatz[3])
print()

# Sortierung nach mehreren Feldern
sql = "SELECT * FROM personen ORDER BY name, vorname"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])

connection.close()

#-------------------- Listing 6: Datei sqlite_eingabe.py

import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# Eingabe Name
eingabe = input("Bitte den gesuchten Namen eingeben: ")
sql = "SELECT * FROM personen WHERE name LIKE ?"
cursor.execute(sql, (eingabe,))
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# Eingabe Teil des Namens
eingabe = input("Bitte den gesuchten Namensteil eingeben: ")
sql = "SELECT * FROM personen WHERE name LIKE ?"
eingabe = '%' + eingabe + '%'
cursor.execute(sql, (eingabe,))
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

connection.close()

#--------------- Listing 7: Datei sqlite_aendern.py

import sqlite3

def ausgabe():
    # SQL-Abfrage, senden, Ausgabe
    sql = "SELECT * FROM personen"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])
    print()

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# Vorher
ausgabe()

# Datensatz aktualisieren
sql = "UPDATE personen SET gehalt = 3780 " \
      "WHERE personalnummer = 81343"
cursor.execute(sql)
connection.commit()

# Nachher
ausgabe()

connection.close()

#----------------- Listing 8: Datei sqlite_loeschen.py

import sqlite3

def ausgabe():
    # SQL-Abfrage, senden, Ausgabe
    sql = "SELECT * FROM personen"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])
    print()

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# Vorher
ausgabe()

# Datensatz entfernen
sql = "DELETE FROM personen " \
      "WHERE personalnummer = 8339"
cursor.execute(sql)
connection.commit()

# Nachher
ausgabe()

connection.close()
