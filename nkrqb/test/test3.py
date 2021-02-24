class Foo:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
class Bar(Foo):
    def __init__(self, **kwagrs):
        super().__init__(kwagrs['c'],kwagrs['d'])
        self.c = kwagrs['a']
        self.d = kwagrs['b']
        
    def show(self):
        print(self.a, self.b, self.c, self.d)
        

Bar(a=3,b=4,c=1,d=2).show()
