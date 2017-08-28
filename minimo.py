contador=0
def minimo(arreglo):
    aux=arreglo
    global contador
    result=-1
    for i in range(0,len(arreglo)):
        ismin=True
        for j in range(0,len(aux)):
            contador+=1
            if arreglo[i] > arreglo[j]:
                ismin = False
                break
        if ismin:
            result=i
            break
        else:
            aux=arreglo     
    return result
        
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
