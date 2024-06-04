# 12. Se quiere hacer un sistema en la facultad para que un alumno pueda ir guardando las materias que va
# haciendo. Para eso, crear una función que le pregunte al usuario la materia que quiere almacenar, e ir
# guardando la información en una lista hasta que ingrese una ‘X’. ¿Qué funciones de listas no permiten
# insertar en una lista?

subjects = []

def saveSubject():
	user_input = input("Insert a subject to save: ")

	while user_input != 'x':
		subjects.append(user_input)
		user_input = input("Insert a subject to save: ")
	else:
		print("Bye!")

	print(subjects)


saveSubject()
