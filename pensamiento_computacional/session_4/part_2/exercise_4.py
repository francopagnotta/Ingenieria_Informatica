# 4. 
# Un chef está armando una lista de supermercado con todos los ingredientes que hay que comprar. Sólo
# quiere agregar un ingrediente a la lista si no lo escribió antes, así no tiene repetidos.
# Hacer un programa que inserte un nuevo elemento en una lista de strings, solamente si el elemento
# que se desea insertar no se encuentra en la lista. La lista de ingredientes la podemos pensar como una
# lista de strings.

# Ejemplo:
# ingredientes: [“tomate”, “queso”, “cebolla”, “huevo”]
# ingrediente a agregar: “orégano”
# La lista de ingredientes debería quedar [“tomate”, “queso”, “cebolla”, “huevo”, “orégano”]
# En cambio, si el ingrediente a agregar es “queso” la lista debería quedar igual.

ingredients = ["tomato", "cheese", "onion", "egg", "oregano"]


def addIngredient():
	user_input_ingredient = input("add an ingredient by name: ")

	if (user_input_ingredient in ingredients):
		print(f"The ingredient {user_input_ingredient} has already exist in the list {ingredients}")

	else:
		ingredients.append(user_input_ingredient)
		print(f"The ingredient {user_input_ingredient} has been added successfully!")
		print(f"The list was updated: {ingredients}")


addIngredient()


# def addIngredient():
# 	ask = True
# 	retry = True

# 	while ask:
# 		user_input_ingredient = input("add ingredient by name: ")
  
# 		if (user_input_ingredient in ingredients):
# 			print(f"The ingredient {user_input_ingredient} has already exist in the list")
   
# 			while retry:
# 				restart = input("Do you want to retry? Y or N: ")
    
# 				if (restart == 'Y'):
# 					break
# 				elif (restart == 'N'):
# 					retry = False
# 					ask = False
# 		else:
# 			ingredients.append(user_input_ingredient)
# 			print(f"The ingredient {user_input_ingredient} has been added successfully!")

# 			restart = input("continue? Y or N: ")

# 			if (restart == 'N'):
# 				ask = False
# 	else:
# 		print("Bye!")