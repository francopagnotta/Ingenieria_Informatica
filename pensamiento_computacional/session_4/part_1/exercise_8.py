# 8. Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.

# a. Crear una tupla para cada país que contenga su nombre, su capital y el continente donde se
# encuentra.
# b. Guardar las tuplas en una lista.
# c. Hacer una función que reciba por parámetros la lista, e imprima la información de cada país
# con el siguiente formato:

# País: <nombre>
# Capital: <capital>
# Continente: <continente>

# Por ejemplo:
	# País: Japón
	# Capital: Tokio
	# Continente: Asia


argentina = ("Argentina", "Buenos Aires", "South America")
france = ("France", "Paris", "Europe")
japan = ("Japan", "Tokio", "East Asia")
germany = ("Germany", "Berlin", "Europe")
peru = ("Peru", "Lima", "South America")

countries = [argentina, france, japan, germany, peru]

def showCountriesInformation(countries):

	for country in countries:
		print(
			f"country: {country[0]}" + "\n"
			f"capital: {country[1]}" + "\n"
			f"continent: {country[2]}" + "\n"
		)

showCountriesInformation(countries)

