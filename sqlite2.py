import sqlite3


def maak_winkel_in_sqlite():
    '''Creeer een winkel database'''
    
    try:
        # Verbind naar sqlite database bestand en creeer een cursor
        conn = sqlite3.connect('winkel.sqlite')
        curs = conn.cursor()
    
        # Verwijder eventuele betaande tabellen
        curs.execute('''DROP TABLE IF EXISTS artikel''')
        curs.execute('''DROP TABLE IF EXISTS klant''')
        curs.execute('''DROP TABLE IF EXISTS verkoop''')
        curs.execute('''DROP TABLE IF EXISTS verkoop_regel''')


        # Maak nieuwe tabellen 
        curs.execute('''CREATE TABLE IF NOT EXISTS artikel (
                        aid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, omschrijving TEXT NOT NULL,
                        code INTEGER NOT NULL,
                        prijs REAL NOT NULL)''')

        curs.execute('''CREATE TABLE IF NOT EXISTS klant (
                        kid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
                        voornaam TEXT NOT NULL,
                        achternaam TEXT NOT NULL,
                        email TEXT check(typeof(email) = 'text') )''')

        curs.execute('''CREATE TABLE IF NOT EXISTS verkoop (
                        vid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
                        kid INTEGER NOT NULL ,
                        datijd DATETIME NOT NULL )''')

        curs.execute('''CREATE TABLE IF NOT EXISTS verkoop_regel(
                        vrid INTEGER PRIMARY KEY NOT NULL,
                        vid INTEGER NOT NULL,
                        aid INTEGER NOT NULL,
                        aantal INTEGER NOT NULL DEFAULT (1) )''')

        print('Tabellen zijn aangemaakt.')
    except:
        print('Kon een of meerdere tabellen niet aanmaken.')
    finally:
        try:
            # Sluit de cursor en verbinding met de database    
            curs.close()
            conn.close()
        except:
            pass


if __name__ == '__main__':
    # Maak een database met de benodigde tabellen
    maak_winkel_in_sqlite()
    