# 2. En un vivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si
# necesita luz solar o no, y el precio. 
# (OBSERVACIÓN: ¿Qué tipo de dato nos permitía guardar si algo es verdad o no?). 
# Ahora se necesita un sistema que guarde las plantas a medida que van llegando. 
# Se pide hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue
# esa planta a la lista de diccionarios.

plants = []

def addPlant():

	user_input = input("Do you want to add a plant? Enter to  continue, x to quit: ")
 
	while user_input != 'x':
		specie = input("specie: ")
		sunlight = input("sunlight is needed? Yes or No: ")
		price = input("price: ")
  
		plants.append({
			"specie": specie,
			"sunlight": True if sunlight.lower() == "yes" else False,
			"price": price
		})
		
		user_input = input("Do you want to add another plant? Enter to  continue, x to quit: ")
	else:
		print(f"The plant list is: {plants}")

addPlant()
