# 1. Hacer una función que reciba un string y que imprima solamente los caracteres que sean vocales.

def printVowelsOnly(string):
	vowels = "aeiou"

	for character in string:
		if character in vowels:
			print(character)

printVowelsOnly("argentina")

