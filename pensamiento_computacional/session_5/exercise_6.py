# 6. En una fábrica, se hace un chequeo de calidad a los productos antes de cada entrega. El resultado del
# chequeo de la entrega se guarda en una lista de diccionarios, donde cada diccionario tiene la siguiente
# información de cada producto:
	# ● Código del producto
	# ● Fecha de vencimiento
	# ● Si pasó el chequeo de calidad o no
# Se pide hacer una función que reciba esta lista de diccionarios y elimine todos los productos que no
# pasaron el chequeo de calidad. Devolver en una tupla el diccionario con los elementos eliminados y la
# cantidad de elementos que quedaron en el diccionario.
# Dado que la tupla es inmutable y nosotros no podemos ir agregando elementos a una tupla, ¿En qué
# momento deberíamos crear la tupla?

products = [
    {
        "product_code": "PROD-1234",
        "expiration_date": "2024-12-31",
        "quality_check": True
    },
    {
        "product_code": "PROD-5678",
        "expiration_date": "2024-11-15",
        "quality_check": False
    },
    {
        "product_code": "PROD-9012",
        "expiration_date": "2025-03-01",
        "quality_check": True
    },
    {
        "product_code": "PROD-3456",
        "expiration_date": "2024-08-20",
        "quality_check": False
    },
]

# def deleteProductsWithNoQualityCheckFromDictList(dict_list):
#     filtered_list = list(
# 		filter(lambda product : product["quality_check"] == False, dict_list)
# 	)
    
#     return (filtered_list, len(filtered_list))

# Alternative code using an external function with filter instead lambda function.
# Python Lambda Functions are anonymous functions means that the function is without a name.
# As we already know the def keyword is used to define a normal function in Python. Similarly, 
# the lambda keyword is used to define an anonymous function in Python. 
# The lambda functions are syntactically restricted to a single expression.
# Inside the filter method, we can use a lambda function or 
# wue can use an external function like the example below:

def filterByQualityCheck(product):
    return product["quality_check"] == False

def deleteProductsWithNoQualityCheckFromDictList(dict_list):
    filtered_list = list(
		filter(filterByQualityCheck, dict_list)
	)
    
    return (filtered_list, len(filtered_list))

# In the above example, we could have used a lambda function perfectly, we used an external function to learn an alternative way.
# In other cases where we need to apply more logic to each item of the iterable within the filter method, whe need to use an external function.

print(deleteProductsWithNoQualityCheckFromDictList(products))