memo={}
cnt=0
def fibonacci(n):
	global memo, cnt
	if n==0 or n==1:
		return 1
	if n in memo:
		return memo[n]
	else:
		cnt+=1
		val=fibonacci(n-2) + fibonacci(n-1)
		memo[n]=val
		return val

print("Lo siguiente representa:\n1er Columna: Posicion Fibonacci \n2da Columna: Numero de Fibonacci  \n3er Columna: Total de operaciones")
for j in range(0,50):
	cnt=0
	print(j+1, fibonacci(j), cnt)