from copy import deepcopy
import random
import math
import time


class Pila(object):
    def __init__(self):
        self.a=[]
    def obtener(self):
        return self.a.pop()
    def meter(self,e):
        self.a.append(e)
        return len(self.a)
    @property
    def longitud(self):
        return len(self.a)


class DSU(object):
    def __init__(self,nodos):
        self.padre={}
        for w in nodos:
            self.padre[w]=w
    def get(self, n):
        x=n 
        while x!=self.padre[x]:
            x=self.padre[x]
        while x!=n:
            n,self.padre[n]=self.padre[n],x
        return n
    def union(self, a, b):
        a,b=self.get(a),self.get(b)
        if a!=b:
            self.padre[a]=b
            return True
        else: return False

def permutaciones(arr):
    if len(arr)==0: return [[]]
    perm=[]
    for i in range(len(arr)):
        wot=permutaciones(arr[:i]+arr[i+1:])
        for w in wot:
            perm.append([arr[i]]+w)
    return perm

class Grafo(object):
    def __init__(self):
        self.vertices=set()
        self.aristas=dict()
        self.vecinos=dict()
    def agrega(self,v):
        self.vertices.add(v)
        if not v in self.vecinos:
            self.vecinos[v]=set()
    def conecta(self,u,v,peso=1):
        self.agrega(u)
        self.agrega(v)
        self.aristas[(u,v)]=self.aristas[(v,u)]=peso
        self.vecinos[u].add(v)
        self.vecinos[v].add(u)
    def __str__(self):
        nodos="Vertices:\n"
        for w in self.vertices:
            nodos+=" "+str(w)+" "
        vis=set()
        edges="Aristas:\n"
        for w in self.aristas:
            (x,y)=w
            if w in vis:
                continue
            if (y,x) in vis:
                continue
            vis.add(w)
            edges+=" "+str(w)+":\t"+str(self.aristas[w])+"\n"
        return nodos+"\n"+edges
    def DFS(self, ini):
        vis=[]
        bsq=Pila()
        bsq.meter(ini)
        while bsq.longitud>0:
            act=bsq.obtener()
            if act in vis:
                continue
            vis.append(act)
            vecino=self.vecinos[act]
            for w in vecino:
                if w not in vis:
                    bsq.meter(w)
        return vis

    def kruskal(self):
        aristas_ordenadasw=deepcopy(self.aristas)
        aristas_ordenadas=sorted(aristas_ordenadasw.keys(), key= lambda k: aristas_ordenadasw[k], reverse=True)
        
        peso,arbol,n=0,Grafo(),len(self.vertices)
        dsu=DSU(self.vertices)

        while len(aristas_ordenadas)>0 and len(arbol.aristas)<2*(n-1):
            (x,y)=aristas_ordenadas.pop()
            if dsu.union(x,y):
                arbol.conecta(x,y,self.aristas[(x,y)])
                peso+=self.aristas[(x,y)]
        print("Arbol de expansion minima: ",peso)
        return arbol
    def heuristica(self,ini):
        vis=[ini]
        act=ini
        for k in range(len(self.vertices)-1):
            sig=0
            peso=1000000000
            for w in self.vecinos[act]:
                if w not in vis and self.aristas[(w,act)]<peso:
                    peso=self.aristas[(w,act)]
                    sig=w
            act=sig
            vis.append(act)
        return vis
    
    def PAV(self):
        perm=permutaciones(list(self.vertices))
        mejor=-1
        camino=[]
        for w in perm:
            peso=0
            for i in range(len(w)-1):
                peso+=self.aristas[(w[i],w[i+1])]
            peso+=self.aristas[(w[-1],w[0])]
            if peso<mejor or mejor==-1:
                mejor=peso
                camino=w
        return camino



def distancia(p,q):
    (x,y),(a,b)=p,q
    return math.sqrt((x-a)**2+(y-b)**2)



#INTERPRETACION DEL GRAFO

#Crearemos el grafo, representando las coordenadas 
mapa=[]
mapa.append(("Mty",(0,0)))
mapa.append(("Pedro",(-11,5)))
mapa.append(("Cade",(39,0)))
mapa.append(("Ramones",(70,9)))
mapa.append(("Bravo",(140,19)))
mapa.append(("Juarez",(12,3)))
mapa.append(("MN",(11,-132)))
mapa.append(("MC",(68,28)))
mapa.append(("Guada",(5,8)))
mapa.append(("Apo",(6,13)))
mapa.append(("Aná",(18,103)))
mapa.append(("Esco",(-12,14)))
mapa.append(("Agua",(46,42)))
mapa.append(("All",(24,-15)))
mapa.append(("China",(130,-3)))
mapa.append(("DG",(43,17)))
mapa.append(("Zua",(13,19)))
mapa.append(("Marín",(21,17)))
mapa.append(("Hig",(25,28)))
mapa.append(("Nico",(0,10)))
mapa.append(("Cién",(6,23)))
mapa.append(("Terán",(84,-16)))
mapa.append(("Garcia",(-40,15)))
mapa.append(("Carmen",(-10,18)))
mapa.append(("Aldamas",(97,30)))
mapa.append(("Herreras",(83,20)))
mapa.append(("Huala",(61,-38)))
mapa.append(("Naranjo",(-12,85)))
mapa.append(("Santiago",(6,-10)))
mapa.append(("Santa",(-24,2)))
mapa.append(("Linares",(81,-40)))
mapa.append(("Villa",(-10,53)))
mapa.append(("Arr",(-1,100)))
mapa.append(("Pesque",(26,10)))
mapa.append(("Trevi",(79,38)))
mapa.append(("Gale",(-19,-47)))
mapa.append(("Ray",(11,-28)))
mapa.append(("Bust",(-30,57)))
mapa.append(("Parás",(69,59)))
mapa.append(("Coss",(121,25)))
mapa.append(("Zara",(30,-93)))
mapa.append(("Sabinas",(10,58)))
mapa.append(("Hida",(-20,25)))
mapa.append(("Itur",(40,-50)))
mapa.append(("Mina",(-52,43)))
mapa.append(("Cerra",(51,30)))
mapa.append(("Monte",(40,-25)))
mapa.append(("Aba",(-18,21)))
mapa.append(("Aram",(41,-73)))


G=Grafo()
for (u,p) in mapa:#Nodo u, Punto p
    for (v,q) in mapa:#Nodo v, Punto q
        if u==v:
            continue
        G.conecta(u,v,distancia(p,q))
print(G)#Imprime el grafo










#ALGORITMO DE APROXIMACION PARA PAV

#Implementacion de un algoritmo de aproximacion usando el algoritmo de kruskal para obtener un arbol de expansion minima
#y de el, crear una solucion aproximada al problema del agente viajero
print("ALGORITMO DE APROXIMACION PARA PAV\n")
Gk=G.kruskal()
print(Gk)#Imprime el arbol de expansion minima
tim=time.clock()
mejor=-1
camino=[]
for repeat in range(6):
    inicial=random.choice(list(Gk.vertices))
    dfs=Gk.DFS(inicial)
    peso=0
    for i in range(len(dfs)-1):
        peso+=G.aristas[(dfs[i],dfs[i+1])]
    peso+=G.aristas[(dfs[-1],dfs[0])]

    print("Camino iniciando en ",inicial)
    for i in range(len(dfs)-1):
        print("De ",dfs[i],"\ta",dfs[i+1],"\tla distancia es ",G.aristas[(dfs[i],dfs[i+1])])
    print("De ",dfs[-1],"\ta ",dfs[0],"\tla distancia es ",G.aristas[(dfs[-1],dfs[0])])
    
    print("Suma del camino: ",peso,"\n")
    if mejor==-1 or mejor>peso:
        mejor=peso
        camino=dfs
print("El mejor camino fue el siguiente: ")
for k in camino:
    print(k,'->')
print(camino[0])
print("\nCon un costo de ",mejor)
print("Tiempo de ejecucion: ",time.clock()-tim)
print("\n--------------------------------------------------\n\n")








#ALGORITMO HEURISTICA PARA PAV

#Visita el vecino mas cercano que no haya visitado del vertice actual, hasta completar el ciclo.
print("ALGORITMO HEURISTICA PARA PAV\n")
mejor=-1
camino=[]
tim=time.clock()
for repeat in range(6):
    inicial=random.choice(list(G.vertices))
    dfs=G.heuristica(inicial)
    peso=0
    print("Camino iniciando en ",inicial)
    for i in range(len(dfs)-1):
        peso+=G.aristas[(dfs[i],dfs[i+1])]
        print("De ",dfs[i],"\ta",dfs[i+1],"\tla distancia es ",G.aristas[(dfs[i],dfs[i+1])])
    print("De ",dfs[-1],"\ta ",dfs[0],"\tla distancia es ",G.aristas[(dfs[-1],dfs[0])])
    peso+=G.aristas[(dfs[0],dfs[-1])]
    print("Suma del camino: ",peso,"\n")
    if mejor==-1 or mejor>peso:
        mejor=peso
        camino=dfs
print("El mejor camino fue el siguiente: ")
for k in camino:
    print(k,'->')
print(camino[0])
print("\nCon un costo de ",mejor)
print("Tiempo de ejecucion: ",time.clock()-tim)
print("\n--------------------------------------------------\n\n")
