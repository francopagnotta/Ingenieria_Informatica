# 10. Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa
# cantidad de veces.

def happyBirthdayGreetings(number_of_greetings):
	index = 0

	# index less than number of greetings because
	# inedx is initialized with zero.
	while index < number_of_greetings:
		print("Happy Birthday!")
		index += 1


happyBirthdayGreetings(10)

