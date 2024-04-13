def calcDiffBetweenSumResultAndLimit():
	limit = int(input("Insert the limit: "))
	
	num_1 = int(input("Insert the first integer to sum: "))
	num_2 = int(input("Insert the second integer to sum: "))

	sum_result = num_1 + num_2
	difference = limit - sum_result

	is_less_than_limit = sum_result < limit

	if (is_less_than_limit):
		print(f"The result of sum {num_1} and {num_2} is {sum_result} and to get to {limit} it needs {difference}")
	elif (sum_result == limit):
		print(f"The result of sum {num_1} and {num_2} is {sum_result} and is equals to the limit {limit}")
	else:
		print(f"The result of sum {num_1} and {num_2} is {sum_result} and It's over te limit {limit}")
		

calcDiffBetweenSumResultAndLimit()


