# 6. Santiago armó una lista con el pedido de empanadas de su familia pero ahora quiere saber la cantidad
# de gustos diferentes que tiene que pedir.
# Podemos pensar la lista de empanadas como una lista de strings, entonces deberíamos devolver la
# cantidad de strings diferentes que hay en una lista.

empanadas = [
	'meat',
	'vegetables',
	'cheese and ham',
	'cheese and onion',
	'meat',
	'vegetables',
	'humita'
 ]

def differentTastes():
	result = []
	
	for i in range(len(empanadas)):
		if empanadas[i] not in result:
			result.append(empanadas[i])
   
	return len(result)
  
  
print(differentTastes())

