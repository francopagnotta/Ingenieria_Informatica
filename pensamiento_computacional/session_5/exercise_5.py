# 5. Un profesor guarda las notas del primer parcial de sus alumnos en una lista de diccionarios que guarda
# la siguiente información:
	# ● Nombre
	# ● Apellido
	# ● Intento
	# ● Nota
# Donde ”intento” es la instancia que está rindiendo, 1 si es la primera vez que rinde el parcial, 2 si es el
# primer recuperatorio y 3 si es el segundo recuperatorio.

# Se pide hacer una función que, dado esta lista de diccionarios, devuelva el promedio de las notas en la
# primera oportunidad que rindieron los alumnos.

# ¿Cómo harían para generalizar la función y que el intento sea parametrizable? Es decir, que no
# solamente sirve para el intento 1, sino que también pueda servir para los demás.

student_notes = [
  {
    "name": "Alice",
    "lastname": "Smith",
    "attempt": 1,
    "note": 5,
  },
  {
    "name": "Bob",
    "lastname": "Johnson",
    "attempt": 2,
    "note": 8,
  },
  {
    "name": "Charlie",
    "lastname": "Brown",
    "attempt": 3,
    "note": 9,
  },
  {
    "name": "David",
    "lastname": "Lee",
    "attempt": 1,
    "note": 7,
  },
]

def getAverageByAttempt(attempt):
  notes = []
  average = 0
  
  for i in range(len(student_notes)):
    if (student_notes[i]["attempt"] == attempt):
      notes.append(student_notes[i]["note"])
  
  for note in notes:
    average += note
    
  return average / len(notes)

# alternative with filter and lambda function
  # average = 0
    
  # students = list(
  #   filter(lambda students : students["attempt"] == attempt, student_notes)
  #   )
  
  # for i in range(len(students)):
  #   average += students[i]["note"]
    
  # return average / len(students)
          
print(getAverageByAttempt(2))