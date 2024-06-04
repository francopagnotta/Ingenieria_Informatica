# Recursos con Tuplas

# Un matrimonio está organizando una fiesta y tiene que armar una lista de invitados. Cada uno tiene su propia
# tupla y guarda en ella a todos los que quiere invitar.

# 8. Si alguien cancela tienen que sacarlo de la tupla.
# Hacer una función que reciba la tupla y un nombre, y devuelva una nueva tupla sin el nombre pasado
# por parámetro.

# Las tuplas son inmutables, entonces ¿Cómo podemos hacer para “eliminar” un elemento de una tupla?
# Recordemos que las tuplas tienen definido el operador +, pero no el operador -.

# 9. Cuando ya tienen a todos los invitados tienen que juntar sus tuplas, para eso se necesita una función
# que a partir de dos tuplas cree una sola que sea la combinación de ambas tuplas

guest_list_him = ()
guest_list_her = ()

def addGuesToList(guest_list, guest_name):
    result_list = list(guest_list)
    
    if guest_name not in guest_list:
        result_list.append(guest_name)
        
    return tuple(result_list)

def removeGuesFromList(guest_list, guest_name):
    result_list = list(guest_list)
    
    if guest_name in guest_list:
        result_list.remove(guest_name)
        
    return tuple(result_list)

def joinTuples(first_tuple, second_tuple):
    return first_tuple + second_tuple


guest_list_him = addGuesToList(guest_list_him, "Olivia")
guest_list_him = addGuesToList(guest_list_him, "Finn")
guest_list_him = addGuesToList(guest_list_him, "Amanda")

guest_list_her = addGuesToList(guest_list_her, "Elliot")
guest_list_her = addGuesToList(guest_list_her, "Barba")
guest_list_her = addGuesToList(guest_list_her, "Nick")

print("him guest list after add guests", guest_list_him)
print("her guest list after add guests", guest_list_her)

guest_list_him = removeGuesFromList(guest_list_him, "Olivia")
guest_list_her = removeGuesFromList(guest_list_her, "Nick")

print("him guest list after remove a guest", guest_list_him)
print("her guest list after remove a guest", guest_list_her)

print("joned lists", joinTuples(guest_list_him, guest_list_her))