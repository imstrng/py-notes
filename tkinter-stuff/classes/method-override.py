class Vervoermiddel(object):
    # constructor
    def __init__(self, merknaam, eigenaar):
        # self staat voor het object (instantie) conform de klasse
        self.merknaam = merknaam
        self.eigenaar = eigenaar
    
    # wisselen van eigenaar
    def wissel(self, nieuwe_eigenaar):
        self.eigenaar = nieuwe_eigenaar
        # lever de nieuwe eigenaar op
        return self.eigenaar
    
    # Hier uw show-methode
    def show(self):
        print(self.eigenaar,'heeft een',self.merknaam)

        
class Voertuig(Vervoermiddel):
    # Overerving: een Voertuig is een Vervoermiddel   
    pass



class Motorvoertuig(Voertuig):
    # Overerving: een Motorvoertuig is een voertuig.
    def __init__(self, merknaam, eigenaar, kenteken = None):
        self.merknaam = merknaam
        self.eigenaar = eigenaar
       
        if kenteken:
            self.kenteken = kenteken
        else:
            self.kenteken = 'geen'
            
class Auto(Motorvoertuig):
    # Overerving: een Auto is een Motorvoertuig
    pass


mijn_auto = Auto('Chris','Mercedes','ASDF')
print(mijn_auto.kenteken)