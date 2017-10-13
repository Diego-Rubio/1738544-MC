cnt=0
def fibonacci(n):
	r=0
	r1=1
	r2=1
	global cnt
	if n==0 or n==1:
		return 1
	for i in range(2,n+1):
		cnt+=1
		r=r1+r2
		r2=r1
		r1=r
	return r
	cnt=0

print("Lo siguiente representa:\n1er Columna: Posicion Fibonacci \n2da Columna: Numero de Fibonacci  \n3er Columna: Total de operaciones")
for w in range (0,50):
	cnt=0
	print(w+1, fibonacci(w), cnt)	
