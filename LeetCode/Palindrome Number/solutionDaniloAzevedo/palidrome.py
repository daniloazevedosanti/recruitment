 ###### Danilo Azevedo #####
 #Vericacoes e teste do numero 
 #do palindrome com cast e fatias

numero = int(input('Enter number (digits >= 3): '))
aux = str(numero)
if(len(aux) < 3):
	numero = int(input('Enter number (digits >= 3): '))
	aux = str(numero)
	if aux == aux[::-1]:
    		print(True)
	else:
    		print(False)
else:	
	if aux == aux[::-1]:
    		print(True)
	else:
    		print(False)