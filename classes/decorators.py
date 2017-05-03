class JustProp():
    # getter
    @property
    def content(self):
        return self.__content  # Hidden property
    
    # setter
    @content.setter
    def content(self,content):
        self.__content = content

jp = JustProp()
jp.content = ['aap','noot','mies']
jp.content

PI = 3.14159265359

class Cirkel():
        
    # constructor
    def __init__ (self, straal):
        self.straal = straal

    # Computed properties
    @property
    def diameter(self):
        return 2 * self.straal

    @property
    def omtrek(self):
        return 2 * PI * self.straal

    @property
    def oppervlakte(self):
        return PI * (self.straal ** 2)

    # Printer
    def __str__(self):
        result=''
        all = dir(self)
        for attr in all:
            # Geen 'magic', geen methods
            if attr[0:2] != '__'  and \
               type(getattr(self, attr)).__name__  != 'method':
                result += "{:<11}: {}\n".format(attr, str(getattr(self, attr)))
        return result

   
class Bol(Cirkel):
    # Computed properties
    @property
    def oppervlakte(self):
        return 4* PI * (self.straal ** 2)
    pass

    @property
    def volume(self):
        return (4/3) * PI * (self.straal ** 3)
    pass


mijn_bol = Bol(10)
print(mijn_bol)