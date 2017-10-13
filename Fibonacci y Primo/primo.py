cnt=0
def primo(num):
	global cnt
	n=num
	a=0
	if n<2:
		print("Intente con un numero mayor o igual a 2")
	for i in range(1,n+1):
		cnt+=1
		if n%i==0:
			a=a+1
	if a!=2:
		print("No es primo")
	else:
		print("Es primo")
	print("El numero de operaciones fue:",cnt)
	cnt=0
