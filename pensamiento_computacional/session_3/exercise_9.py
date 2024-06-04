# c

# shows te math table from start index to end index of the number 
# passed as param
def getMathTableOfNumberFromRange(number, start_index, end_index):
	end_index = end_index + 1

	for index in range(start_index, end_index):
		print(f"{number} * {index} = {number * index}")

getMathTableOfNumberFromRange(5, 1, 10)


