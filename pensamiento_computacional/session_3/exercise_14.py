# 14. Crear una función que reciba un número entero e imprima los números primos entre 0 y el número
# ingresado.
# AYUDA: un número es primo cuando solamente es divisible por sí mismo y por 1, es decir que para ver
# si es primo hay que ver que el módulo (%) de ese número con los anteriores hasta el 1 (sin incluirlo) sea
# distinto de 0, o sea que no sea divisible.

def getPrimeNumbers(number_to_check):
	start_index = 2
	stop_index = number_to_check

	for index in range(start_index, stop_index):
		if (number_to_check % index == 0):
			print(f"The number {number_to_check} is not prime")
			return

	print(f"The number {number_to_check} is prime")

getPrimeNumbers(6)


 