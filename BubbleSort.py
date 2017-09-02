def burbuja(arreglo):
    aux=arreglo[:]
    for i in range(len(arreglo)):
        for j in range(0,len(arreglo)-i-1):
            if(aux[j]>aux[j+1]):
                temp=aux[j]
                aux[j]=aux[j+1]
                aux[j+1]=temp
    return aux