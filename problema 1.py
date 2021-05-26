n=int(input('Ingrese un numero: '))
n2=int(input('Ingrese un numero: '))
n3=int(input('Ingrese un numero: '))
if n<n2<n3:
		menor=n
if n2<n3<n:
		menor=n2
if n3<n<n2:
		menor=n3

print('El numero menor es : ', menor)