suma=0
for var in range(1,6):
	num=int(input('Ingrese un numero: '))
	if  num %2==0:
		suma=suma+num
print('La suma de numeros pares es: ',suma)