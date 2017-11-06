from heapq import heappop, heappush
from copy import deepcopy
import random

import time
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst] 
    l = [] 
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l

class Fila:
    def __init__(self):
        self.fila= []
    def obtener(self):
        return self.fila.pop()
    def meter(self,e):
        self.fila.insert(0,e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)

class Pila:
    def __init__(self):
        self.pila= []
    def obtener(self):
        return self.pila.pop()
    def meter(self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longitud(self):
        return len(self.pila)


def flatten(L):
    while len(L) > 0:
        yield L[0]
        L = L[1]

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

    def BFS(self,ni):
        visitados =[]
        f=Fila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def DFS(self,ni):
        visitados =[]
        f=Pila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def shortest(self, v): 
        q = [(0, v, ())] 
        dist = dict() 
        visited = set() 
        while len(q) > 0: 
            (l, u, p) = heappop(q) 
            if u not in visited: 
                visited.add(u) 
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])    
            p = (u, p) 
            for n in self.vecinos[u]: 
                if n not in visited: 
                    el = self.E[(u,n)] 
                    heappush(q, (l + el, n, p)) 
        return dist 

    def kruskal(self):
        e = deepcopy(self.E)
        arbol = Grafo()
        peso = 0
        comp = dict()
        t = sorted(e.keys(), key = lambda k: e[k], reverse=True)
        nuevo = set()
        while len(t) > 0 and len(nuevo) < len(self.V):
            #print(len(t)) 
            arista = t.pop()
            w = e[arista]    
            del e[arista]
            (u,v) = arista
            c = comp.get(v, {v})
            if u not in c:
                
                arbol.conecta(u,v,w)
                peso += w
                nuevo = c.union(comp.get(u,{u}))
                for i in nuevo:
                    comp[i]= nuevo
        print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
        return arbol

    def vecinoMasCercano(self):
        ni = random.choice(list(self.V))
        result=[ni]
        while len(result) < len(self.V):
            ln = set(self.vecinos[ni])
            le = dict()
            res =(ln-set(result))
            for nv in res:
                le[nv]=self.E[(ni,nv)]
            menor = min(le, key=le.get)
            result.append(menor)
            ni=menor
        return result
        
        

    
            
g= Grafo()

g.conecta('Mex','Bra',6.52)
g.conecta('Mex','Can',3.32)
g.conecta('Mex','Peru',4.62)
g.conecta('Mex','Arg',7)
g.conecta('Mex','Fran',9.1)
g.conecta('Mex','Nor',8.65)
g.conecta('Mex','Groen',6.32)
g.conecta('Mex','Nig',11.96)
g.conecta('Mex','Sud',14.86)
g.conecta('Bra','Can',6.61)
g.conecta('Bra','Peru',2.56)
g.conecta('Bra','Arg',1.93)
g.conecta('Bra','Fran',8.41)
g.conecta('Bra','Nor',9.74)
g.conecta('Bra','Groen',9.13)
g.conecta('Bra','Nig',7.4)
g.conecta('Bra','Sud',8.4)
g.conecta('Can','Peru',6.03)
g.conecta('Can','Arg',8)
g.conecta('Can','Fran',5.78)
g.conecta('Can','Nor',5.43)
g.conecta('Can','Groen',3.33)
g.conecta('Can','Nig',9.16)
g.conecta('Can','Sud',13.06)
g.conecta('Peru','Arg',2.38)
g.conecta('Peru','Fran',9.9)
g.conecta('Peru','Nor',10.7)
g.conecta('Peru','Groen',9.23)
g.conecta('Peru','Nig',9.88)
g.conecta('Peru','Sud',10.75)
g.conecta('Arg','Fran',10.33)
g.conecta('Arg','Nor',11.66)
g.conecta('Arg','Groen',10.87)
g.conecta('Arg','Nig',8.75)
g.conecta('Arg','Sud',8.56)
g.conecta('Fran','Nor',1.85)
g.conecta('Fran','Groen',3.67)
g.conecta('Fran','Nig',4.41)
g.conecta('Fran','Sud',8.63)
g.conecta('Nor','Groen',2.43)
g.conecta('Nor','Nig',6.13)
g.conecta('Nor','Sud',10.19)
g.conecta('Groen','Nig',8.03)
g.conecta('Groen','Sud',12.29)
g.conecta('Nig','Sud',4.27)
print(g.kruskal())



print(g)
k = g.kruskal()
print([print(x, k.E[x]) for x in k.E])

for r in range(10):
    ni = random.choice(list(k.V))
    dfs =  k.DFS(ni)
    c = 0
    
    
    for f in range(len(dfs) -1):
            c += g.E[(dfs[f],dfs[f+1])]
            print(dfs[f], dfs[f+1], g.E[(dfs[f],dfs[f+1])] )
            
    c += g.E[(dfs[-1],dfs[0])]
    print(dfs[-1], dfs[0], g.E[(dfs[-1],dfs[0])])
    print('costo',c)

dfs = g.vecinoMasCercano()
print(dfs)
c=0
for f in range(len(dfs) -1):
    c += g.E[(dfs[f],dfs[f+1])]
    print(dfs[f], dfs[f+1], g.E[(dfs[f],dfs[f+1])] )
    
c += g.E[(dfs[-1],dfs[0])]
print(dfs[-1], dfs[0], g.E[(dfs[-1],dfs[0])])
print('costo',c)



data = ['Peru', 'Arg', 'Fran', 'Nor', 'Nig', 'Mex', 'Bra', 'Can', 'Sud', 'Groen']
tim=time.clock()
per = permutation(data)
print(time.clock()-tim)


