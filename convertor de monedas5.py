menu="""
Bienvenidos al convertor de monedas馃槑馃
1. PESOS COLOMBIANOS 馃挍馃挋馃А
2. PESOS ARGENTINOS 馃挋馃馃挋
3. PESOS MEXICANOS 
4. NUEVOS SOLES
Elige una opci贸n 
"""
opci贸n= int(input(menu)) 
if opci贸n==1:
	valor=str(input('Ingresa un valor en d贸lares:'))
	valor_d贸lar=(3681.20)
	valor_d贸lar=float(valor_d贸lar)
	valor_pesos=int(valor)*valor_d贸lar
	valor_pesos=round(valor_pesos, 2)
	valor_pesos=str(valor_pesos)
	print('El valor en pesos colombianos es: $',valor_pesos,'馃嚚馃嚧')
if opci贸n==2:
	valor=str(input('Ingresa un valor en d贸lares:'))
	valor_d贸lar=(71.84)
	valor_d贸lar=float(valor_d贸lar)
	valor_pesosarg=int(valor)*valor_d贸lar
	valor_pesosarg=round(valor_pesosarg, 2)
	valor_pesosarg=str(valor_pesosarg)
	print('El valor en pesos argentinos es: $',valor_pesosarg,'馃嚘馃嚪')	
if opci贸n==3:
	valor=str(input('Ingresa un valor en d贸lares:'))
	valor_d贸lar=(22.28)
	valor_d贸lar=float(valor_d贸lar)
	valor_pesosmex=int(valor)*valor_d贸lar
	valor_pesosmex=round(valor_pesosmex, 2)
	valor_pesosmex=str(valor_pesosmex)
	print('El valor en pesos mexicanos es: $',valor_pesosmex,'馃嚥馃嚱')
if opci贸n==4:
	valor=str(input('Ingresa un valor en d贸lares:'))
	valor_d贸lar=(3.62)
	valor_d贸lar=float(valor_d贸lar)
	valor_soles=int(valor)*valor_d贸lar
	valor_soles=round(valor_soles, 2)
	valor_soles=str(valor_soles)
	print('El valor en nuevos soles es: S/',valor_soles,'馃嚨馃嚜')