'''
247G3 Opgave 4

Methoden toevoegen aan een klasse
In het bestand H6_inzend_04.py vindt u de klassenhiërarchie van de onderste tak van 
wielerwedstrijd (wedstrijd-cross-{veld, ATB}). Een wedstrijd wordt gehouden op een plaats, 
op een bepaalde datum, vanaf een vertrekpunt en op een vertrektijd. Aan een wedstrijd doen 
deelnemers mee. Na afloop van een wedstrijd zijn de winnaars (1ste, 2de en 3de plaats) bekend. 
U bewaart de oplossing van onderstaande opgaven als H6_inzend_04_loi.py.
'''

class Wedstrijd(object):
    '''
    a) Schrijf een constructor die de properties plaats, datum, vertrekpunt en vertrektijd invult.
    De constructor maakt ook de property deelnemers aan in de vorm van een lege lijst.
    Datum en tijd zijn strings volgens de ISO-standaard ('yyyy-mm-dd' en 'hh:mi').
    '''
    # constructor
    def __init__(self, plaats, datum, vertrekpunt, vertrektijd):
        self.plaats = plaats
        self.datum = datum
        self.vertrekpunt = vertrekpunt
        self.vertrektijd = vertrektijd
        self.deelnemers = []
    
    '''
    b) Schrijf een methode inschrijving() die de naam van een wielrenner toevoegt aan deelnemers.
    Voorbeeld: instantie.inschrijving('Jan Jansen')
    '''
    def inschrijving(self,naam):
        self.deelnemers.append(naam)

    '''
    c) Schrijf een methode uitslag() die de namen van winnaars (1ste, 2de en 3de plaats) opslaat in
    de winnaars property (een tuple). Een wedstrijd kan natuurlijk niet worden gewonnen door iemand
    die niet heeft deelgenomen aan de wedstrijd. De methode uitslag() gaat dat na. Komt een winnaar 
    niet voor in de deelnemerslijst, dan faalt de methode en print de melding: 'Niet in deelnemerlijst: <naam>'.
    Print deze melding voor elke 'winnaar' die ontbreekt in 'deelnemers'.
    '''
    def uitslag(self,eerste, tweede, derde):
        for self.__naam in (eerste, tweede, derde):
            if self.__naam not in self.deelnemers:
                print('Niet in deelnemerslijst:',self.__naam)
                self.winnaars = None
            
    '''
    d) Voeg een methode toon() toe die alle property-value-paren van een instantie afdrukt
    (elk paar op een nieuwe regel). Maak in deze methode gebruik van de magic property __dict__.
    '''
    def toon(self):
        print('-'*40)
        print("{:<15}: {}".format('Wedstrijd', self.__class__.__name__))
        for k, v in sorted(self.__dict__.items()):
            if '_' not in k:
                print("{:<15}: {}".format(k, str(v)))
        print('-'*40)
            

class Cross(Wedstrijd):
    pass

class Veldrijden(Cross):
    pass

class ATB(Cross):
     pass

    
if __name__ == '__main__':
    '''
    e) Test uw methoden door een instantie te maken van ATB (u mag de parameters zelf kiezen).
    Voeg een aantal deelnemers toe (minimaal zes, u mag de namen zelf kiezen).
    Vervolgens 'maakt u de uitslag bekend' (u mag de winnaars zelf kiezen).
    Ten slotte drukt u de instantie af met de toon()-methode.
    '''
    race1 = ATB(datum='2016-09-23',plaats='Amstelveen',vertrekpunt='Bakboord 11',vertrektijd='12:00')
    race1.inschrijving('Chris')
    race1.inschrijving('Jan')
    race1.inschrijving('Piet')
    race1.inschrijving('Klaas')
    race1.inschrijving('Kees')
    race1.inschrijving('Harrie')
    race1.inschrijving('Daan')
    race1.uitslag('Jan','Harrie','Chris')

    race2 = Cross(datum='2016-06-12',plaats='Amsterdam',vertrekpunt='Spuistraat',vertrektijd='10:00')
    race2.inschrijving('Chris Hansen')
    race2.inschrijving('Jan Jansen')
    race2.inschrijving('Piet Pietersen')
    race2.inschrijving('Klaas Klaasen')
    race2.uitslag('Klaas Klaasen','Frits Fraudeur','Hans Trol')
    
    race1.toon()   
    race2.toon()   
