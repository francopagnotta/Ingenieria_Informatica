# 7. Manuel y su pareja armaron una lista numerada con las actividades de mantenimiento de la casa.
# Decidieron dividirse las tareas, a Manuel le tocó hacer todas las actividades con número par, por eso
# necesitamos hacer una función que reciba una lista de enteros, y devuelva otra lista que solamente
# contenga números pares, que vienen a ser las tareas de Manuel.

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def getEvenNumbers(integers):
    evens = []
    
    for i in range(len(integers)):
        if (integers[i] % 2 == 0):
            evens.append(integers[i])
    return evens

print(getEvenNumbers(integers))