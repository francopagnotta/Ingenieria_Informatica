# 10. Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos
# números elevados al cuadrado.

integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
integer_list_copy = []

for integer in integer_list:
	integer_list_copy.append(integer ** 2)

print(integer_list_copy)

