# 11. Se tiene la siguiente lista de palabras: [“entender”, “pueden”, “humanos”, “los”, “que”, “código”,
# “escriben”, ”programadores”, “buenos”, “Los”, “entiende.”, “computadora”, “una”, “que”, “código”,
# “escribe”, “tonto”, “Cualquier”]. Hacer una función que reciba una lista, y devuelva un string uniendo
# las palabras desde el final de la lista hasta el principio con un “ ” (espacio) entre cada una, para formar
# la frase. (ver funciones de listas y strings).

list_of_words =  [
	"entender",
	"pueden",
	"humanos",
	"los",
	"que",
	"código",
	"escriben",
	"programadores",
	"buenos",
	"Los",
	"entiende.",
	"computadora",
	"una",
	"que",
	"codigo",
	"escribe",
	"tonto",
	"Cualquier",
]

def makeAPraseByWords(list_of_words):
	list_of_words_copy = list(list_of_words)
	list_of_words_copy.reverse()
	return " ".join(list_of_words_copy)

print(makeAPraseByWords(list_of_words))


