# 8. Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un
# número entero e imprima por pantalla los números del 1 hasta ese número con la estructura de control
# iterativa for.

# shows in console the sequence of numbers between 
# the specified indexes passed as params, both incuded.
def getNumbersFromRange(start_index, end_index):
	end_index = end_index + 1 
	# + 1 porque el stopIndex del metodo range no se incluye, 
 	# entonces si el limite es 10, hacemos que el stopIndex sea 11 para poder mostrar hasta el 10
 
	for number in range(start_index, end_index):
		print(number)

getNumbersFromRange(10)

