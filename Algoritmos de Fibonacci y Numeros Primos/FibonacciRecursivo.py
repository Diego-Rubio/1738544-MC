cnt=0
def fibonacci(n):
	global cnt
	cnt+=1
	if n==0 or n==1:
		return 1
	return fibonacci(n-2) + fibonacci(n-1)

print("Lo siguiente representa:\n1er Columna: Posicion Fibonacci \n2da Columna: Numero de Fibonacci  \n3er Columna: Total de operaciones")
for i in range(0,51):
	cnt=0
	print(i+1, fibonacci(i), cnt)
