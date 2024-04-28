# 9. Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior. Ahora se
# necesita una funcionalidad que permita a los niños aprender las tablas. Crear una función que reciba un
# número entero e imprima por pantalla la tabla de ese número del 1 al 10.

# shows te math table from start index to end index of the number 
# passed as param
def getMathTableOfNumberFromRange(number, start_index, end_index):
	end_index = end_index + 1

	for index in range(start_index, end_index):
		print(f"{number} * {index} = {number * index}")

getMathTableOfNumberFromRange(5, 1, 10)


