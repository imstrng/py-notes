class Geheel(object):
    def __init__(self, naam, onderdelen):
        self.naam = naam
        self.onderdelen = onderdelen

class Onderdeel(object):
    def __init__(self, nummer, omschrijving):
        self.nummer = nummer
        self.omschrijving = omschrijving
    

raam = Onderdeel(123,'Voorraam')
deur = Onderdeel(322,'Linker voor deur')

auto = Geheel('Volvo',[raam,deur])
for o in auto.onderdelen:
    print(o.nummer, o.omschrijving)