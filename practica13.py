n=int(input('Ingrese un numero : '))
i=2
while(n%i!=0):
	i=i+1
if i==n:
	print(str(n), 'es primo')
else:
	print(str(n), 'no es primo')