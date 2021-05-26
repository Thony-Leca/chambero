n=int(input('Ingrese un numero: '))
n2=int(input('Ingrese un numero: '))
n3=int(input('Ingrese un numero: '))
if n>n2>n3:
	mayor=n
if n2>n3>n:
	mayor=n2
if n3>n>n2:
	mayor=n3
print('El numero mayor es : ',mayor)