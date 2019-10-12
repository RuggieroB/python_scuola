'''

	# python_scuola

	Python3 5Finf. - AS 2019/2020

'''

import math

scelta=0

while scelta<=0 or scelta>2:
	scelta=input("Effettua una scelta:\n1) Calcolo del quadrato;\n2) Calcolo della radice quadrata.\n\t\t")
	scelta=int(scelta)
	if scelta<=0 or scelta>2:
		print("ERRORE! Scelta non valida! Valori accettabili 1 o 2.\n\n")

if scelta==1:
	num=input("\nInserisci un numero intero:\t")
	num=int(num)
	num2=math.pow(num,2)
	print("\nIl quadrato del numero",num,"è:\t",num2)
else:
	num=input("\nInserisci un numero intero:\t")
	num=int(num)
	rad=math.sqrt(num)
	print("La radice quadrata di",num,"è:\t",rad)
