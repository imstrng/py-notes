import sqlite3

dbname = '/tmp/survey.db'

def persoon_tabel_maken():
    '''Maak persoon tabel in de database'''
    try:
        # Verbind naar sqlite database bestand en maak een cursor
        conn = sqlite3.connect(dbname)
        curs = conn.cursor()
    
        # Verwijder eventuele betaande tabellen
        curs.execute('''DROP TABLE IF EXISTS persoon''')

        # Maak een nieuwe tabel
        curs.execute('''CREATE TABLE IF NOT EXISTS persoon (
                        achternaam TEXT, 
                        leeftijd INTEGER,
                        voornamen TEXT)''')
    except:
        print('Kon tabellen niet aanmaken.')
    finally:
        try:
            # Sluit de cursor en verbinding
            curs.close()
            conn.close()
        except:
            pass

        
        
def persoon_toevoegen(achternaam,leeftijd,voornamen):
        '''Voegt een persoon toe aan de persoon tabel'''
        try:
            # Verbind naar sqlite database bestand en maak een cursor
            conn = sqlite3.connect(dbname)
            curs = conn.cursor()

            # Voeg de data toe in de tabel
            query = '''INSERT INTO persoon (achternaam, leeftijd, voornamen) VALUES (?,?,?)'''
            curs.execute(query, (achternaam, leeftijd, voornamen))
            conn.commit()
        except():
            print('Kon persoon niet in tabel toevoegen.')
        finally:
            try:
                # Sluit de cursor en verbinding
                curs.close()
                conn.close()
            except:
                pass

            
def persoon_afdrukken(achternaam):
        '''Drukt alle personen af van de persoon tabel en print deze uit op het scherm waarvan de
        achternaam gelijk is aan de invoer'''
        try:
            # Verbind naar sqlite database bestand en maak een cursor
            conn = sqlite3.connect(dbname)
            curs = conn.cursor()

            # Query de tabel en print deze af
            query = '''SELECT achternaam, leeftijd, voornamen FROM persoon where achternaam = ?'''
            data = curs.execute(query, (achternaam,)).fetchall()
            for achternaam, leeftijd, voornamen in data:
                print(voornamen,achternaam+':',leeftijd,'jaar')
            
        except():
            print('Kon data niet afdrukken')
        finally:
            try:
                # Sluit de cursor en verbinding
                curs.close()
                conn.close()
            except:
                pass

# Maak een tabel
persoon_tabel_maken()
# Voeg een persoon persoon toe
persoon_toevoegen('Beumer',45,'Chris')
# Druk persoon af
persoon_afdrukken('Beumer')
