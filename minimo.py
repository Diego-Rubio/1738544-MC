contador=0
def minimo(arr):
    m = arr[0]
    global contador
    for i in arr:
        contador+=1
        if i < m:
            m=i
    return m
        
def ordenar(arreglo):
    aux = arreglo
    result=[]
    for i in range(0,len(arreglo)):
        m = minimo(aux)
        result.append(aux[m])
        del aux[m]
    return result

import random
p=random.sample(range(1,100),50)
print(p)
ord=ordenar(p)
print(contador)
print(ord)
print(minimo(p))
