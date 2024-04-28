# 6. Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de
# ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con
# ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
# Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del
# usuario, y no solo para 100?

def calcDiffBetweenSumResultAndLimit():
	limit = int(input("Insert the limit: "))
	
	num_1 = int(input("Insert the first integer to sum: "))
	num_2 = int(input("Insert the second integer to sum: "))

	sum_result = num_1 + num_2
	difference = limit - sum_result

	is_less_than_limit = sum_result < limit

	if (is_less_than_limit):
		print(f"The result of sum {num_1} and {num_2} is {sum_result} and to become {limit} needs {difference}")
	elif (sum_result == limit):
		print(f"The result of sum {num_1} and {num_2} is {sum_result} and is equals to the limit {limit}")
	else:
		print(f"The result of sum {num_1} and {num_2} is {sum_result} and It's over te limit {limit}")
		

calcDiffBetweenSumResultAndLimit()


