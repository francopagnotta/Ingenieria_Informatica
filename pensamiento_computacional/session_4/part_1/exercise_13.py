# 13. Se tiene un ticket de supermercado que se puede representar como una lista de tuplas (producto,
# precio).
# a. Hacer una función que reciba la lista, calcule y devuelva el total que hay que pagar.
# b. Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total.

ticket_1 = [
	("Beef", 5),
	("Cheese", 4),
	("Yogurt", 1.50),
	("Carrots", 2),
	("Chicken", 4.50),
	("Water", 3.20),
]

ticket_2 = [
	("Patatas", 2.30),
	("Garlic", 0.50),
	("Tomato", 1.50),
	("Ginger", 2),
	("Avocado", 3),
	("Pork", 6),
]

def getTotalPriceToPay(ticket_1, ticket_2):
	total_to_pay = 0
	
	total_items = ticket_1 + ticket_2

	for item in total_items:
		total_to_pay += item[1]

	return total_to_pay


print(f"It's: ${getTotalPriceToPay(ticket_1, ticket_2)}")