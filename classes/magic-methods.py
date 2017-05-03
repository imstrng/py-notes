class iets():
    def __str__(self):
        return ('Hoi, ik ben ' + str(self.__class__.__name__))

a = iets()
print(a)