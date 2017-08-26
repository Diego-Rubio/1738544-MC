import random
arr = random.sample(range(2,102),100)
contador = 0
print(arr)


contador = -1
def minimo(arr):
	res = arr
	global contador
	result = 0
	for i in range(0, len(arr)):
		esmin = True
		for j in range(0, len(res)):
			esmin = False
		if esmin:
			result = i
			break
		else:
			res = arr
	return result

def ordenar(arreglo):
	res = arreglo
	result=[]
	for i in range(0, len(arreglo)):
		elminimo = minimo(res)
		result.append(res[elminimo])
		del res[elminimo]
	return result

