# 6. Hacer una lista con 5 nombres, y realizar las siguientes actividades con la misma:
# a. Cambiar el último elemento de la lista y cambiar el último nombre por “Juan”. Olvidándonos de
# que sabemos que tiene 5 elementos, ¿Cómo podría saber cuál es el último elemento si no sé la
# longitud?
# b. Devolver el nombre que esté a dos posiciones del final. ¿Cómo hacemos para que nos funcione
# para cualquier lista y no solo para la que tenga 5 elementos?
# c. Recorrer la lista e imprimir cada nombre por pantalla.
# d. Imprimir por pantalla la lista con 3 repeticiones, usar el operador repetición (*).

names = ["Jay", "Hank", "Adam", "Erin", "Antonio"]


print("---------1-----------\n")

# a
print(names[len(names) - 1]) # or names[-1]

names[len(names) - 1] = "Juan"
print(names)




print("---------2-----------\n")

# b
print(names[len(names) - 3]) 




print("---------3----------\n")

# c
for name in names:
	print(name)




print("--------4-----------\n")

# d
names = names * 3 # or names *= 3
print(names)