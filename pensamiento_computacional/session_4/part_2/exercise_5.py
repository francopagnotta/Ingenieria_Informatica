# 5. 
# Agustina está jugando a las cartas con sus amigos. A ella le gusta tener las cartas de su mano bien
# ordenadas. Esto significa que cada vez que tiene que agarrar una nueva carta, la quiere agregar a su
# mano en el lugar indicado para no romper el orden.
# Si se tiene una lista de enteros ordenadas de mayor a menor. Hacer una función que según esta lista
# inserte un nuevo entero, manteniendo el orden.

# Podemos pensar la lista de cartas como números enteros.
# Ejemplo:
# cartas: [1, 4, 6, 8]
# carta nueva: 5
# La lista de cartas debería quedar: [1, 4, 5, 6, 8]
# Tratar de pensar una solución sin usar el método sort. (no es obligatorio).

list = [1, 4, 5, 6, 8]

def addIntegerToList():
	user_input = input("Insert an integer value to add it to the list: ")
	
	if user_input in list:
		print(f"The integer value {user_input} is already in the list {list}")
	else:
		list.append(int(user_input))
		print(sortIntegerList(list))
    
def sortIntegerList(list):
	for i in range(len(list)):
		for j in range(len(list) - 1):
			if list[i] < list[j]:
				current = list[i]
				list[i] = list[j]
				list[j] = current
    
	return list

addIntegerToList()

