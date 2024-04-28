# 1. Crear una lista con los números del 1 al 10. Acceder con el índice a la posición que contiene el número
# 5, e imprimirlo por pantalla. Recordar que el índice de las listas empiezan con 0.


list = []

for index in range(1, 11):
	list.append(index)

print(list[4])

# 2. Con la lista del punto anterior, usar la función len() para averiguar su longitud, e imprimirla.
print(len(list))


