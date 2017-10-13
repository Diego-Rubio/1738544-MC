cnt=0
def primo(num):
	global cnt
	n=num
	a=0
	b='No es primo'
	c='Si es primo'
	if n<2:
		print("Intente con un numero mayor o igual a 2")
	for i in range(1,n+1):
		cnt+=1
		if n%i==0:
			a=a+1
	if a!=2:
		return b
	else:
		return c
	cnt=0

print("Lo siguiente representa:\n1er Columna: Numero Primo \n2da Columna: ¿Es o no es?  \n3er Columna: Total de operaciones")
for	w in range(2,104):
	cnt=0
	print(w, primo(w), cnt)