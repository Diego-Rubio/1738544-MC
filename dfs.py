class Pila:
    def __init__(self):
        self.pila=[]
    def obtener(self):
        return self.pila.pop()
    def meter(self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longitud(self):
        return len(self.pila)


class Grafo:
 
    def __init__(self):
        self.V = set() 
        self.E = dict() 
        self.vecinos = dict() 
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: 
            self.vecinos[v] = set() 
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso 
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp        
 
 
def dfs(grafo,inicio):
    visitados=[]
    pila=Pila()
    pila.meter(inicio)
    while pila.longitud>0:
        actual=pila.obtener()
        if actual in visitados:
            continue
            
        visitados.append(actual)
        vecinos=grafo.vecinos[actual]
        for i in vecinos:
            if i not in visitados:
                pila.meter(i)
    return visitados


grafo=Grafo()
grafo.conecta(1,2)
grafo.conecta(1,3)
grafo.conecta(2,4)
grafo.conecta(2,5)
grafo.conecta(3,6)
grafo.conecta(4,7)
grafo.conecta(5,7)
grafo.conecta(6,8)
grafo.conecta(6,9)
print(dfs(grafo,1))    