def insercion(array):
	for indice in range(1,len(array)):
		valor=array[indice]
		i=indice-1
		while i>=0:
			if valor<array[i]:
				array[i+1]=array[i]
				array[i]=valor
				i-=1
			else:
				break								