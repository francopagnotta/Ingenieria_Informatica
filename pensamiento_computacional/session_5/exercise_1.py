# 1. En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener
# mejor organizado sus datos.

	# a. Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las
	# características que se consideren más relevantes para identificar a una persona (su nombre,
	# DNI, edad, etc).
	# b. Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso
	# del estudiante y sus características (año, división, orientación, etc).
	# c. Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad
	# e imprimirla por pantalla.

students = [
	{
		"name": "Olivia",
		"last_name": "Benson",
		"age": 40,
		"dni": 123456,
		"course": {
			"year": 2024,
			"commission": 1,
			"orientation": "science"
		}
	},
	{
		"name": "Nick",
		"last_name": "Amaro",
		"age": 42,
		"dni": 142458,
		"course": {
			"year": 2024,
			"commission": 2,
			"orientation": "politics"
		}
	},
	{
		"name": "Amanda",
		"last_name": "Rollins",
		"age": 41,
		"dni": 145932,
		"course": {
			"year": 2024,
			"commission": 3,
			"orientation": "informatic"
		}
	}
]


def addStudent(name, lastName, age, dni, year, commission, orientation):
	students.append({
		"name": name,
		"last_name": lastName,
		"age": age,
		"dni":	dni,
		"course": {
			"year": year,
			"commission": commission,
			"orientation": orientation
		}
	})
 

def getOldestStudent():
	age = 0
	student_index = 0
	for i in range(len(students)):
		if (students[i]["age"] > age):
			age = students[i]["age"]
			student_index = i
	return students[student_index]
	# return max(students, key = lambda student : student["age"])


 
addStudent("Fran", "Pagnotta", 28, 39557500, 2024, 4, "engineering")
print(getOldestStudent())


def manageDictonary():
    dictionary = {
		1: "Olivia",
		2: "Nick"
	}
    print(dictionary.get(1))
    print(dictionary.items())
    print(dictionary.get(2))
    print(dictionary.keys())
    print(dictionary.pop(2))
    print(dictionary.values())
    print(dictionary.update({ 3: "Ice T"}))
    print(dictionary.values())
    
manageDictonary()