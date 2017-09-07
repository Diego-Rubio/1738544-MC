def selection(arr):
	for i in range(0,len(arr)-1):
		valor=i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[valor]:
				valor=j
			if valor !=i:
				aux=arr[i]
				arr[i]=arr[valor]
				arr[valor]=aux
	return arr				