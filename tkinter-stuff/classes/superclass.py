class A():
    def __init__(self):
        print('first')
        
class B():
    def __init__(self):
        print('second')

class C(A):
    def __init__(self):
        super().__init__()
        print('third')
        
a = C()