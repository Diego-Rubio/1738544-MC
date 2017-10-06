class Cola:
    def __init__(self):
        self.cola=[]
    def obtener(self):
        return self.cola.pop(0)
    def meter(self,e):
        self.cola.append(e)
        return len(self.cola)
    @property
    def longitud(self):
        return len(self.cola)


c=Cola()
c.meter(1)
c.meter(2)
c.meter('x')
c.meter("y")
print(c.longitud)
print(c.obtener())
print(c.obtener())
print(c.obtener())
print(c.obtener())
print(c.longitud)