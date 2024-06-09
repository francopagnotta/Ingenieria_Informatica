# 3. Se representa un ticket de supermercado como una lista de diccionarios, donde cada diccionario tiene
# la siguiente información:
	# ● Nombre del producto
	# ● Precio por unidad
	# ● Cantidad
# Se pide hacer una función que reciba el ticket y devuelva el monto total a pagar.

supermarket_ticket = [
    {"product": "Apples", "price": 2.50, "quantity": 3},
    {"product": "Milk", "price": 3.80, "quantity": 1},
    {"product": "Bread", "price": 4.10, "quantity": 2},
    {"product": "Eggs", "price": 2.00, "quantity": 12},
    {"product": "Lettuce", "price": 1.75, "quantity": 1},
]

def getTotalAmountToPay(ticket):
    total_amount = 0
    
    for item in ticket:
        total_amount += item["price"]
        
    return round(total_amount, 2)

print(f"The total amount to pay is: ${getTotalAmountToPay(supermarket_ticket)}")