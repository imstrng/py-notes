class Vervoermiddel(object):
    # logger: administreert alle constructies van alle objecten
    # van Vervoermiddel en subklassen
    log = []
    @classmethod
    def history(cls):
        for c in cls.log:
            print(c[0], c[1])
    # constructor
    def __init__(self, merknaam, eigenaar):
        # self staat voor het object (instantie) conform de klasse
        self.merknaam = merknaam
        self.eigenaar = eigenaar
        # ADD LOGGING
        self.log.append(('Constructed: ', self.__class__.__name__))

        
tram = Vervoermiddel('Lijn 5','Pietje')
fiets = Vervoermiddel('Batavus','Harrie')
print(tram.history())
print(fiets.history())