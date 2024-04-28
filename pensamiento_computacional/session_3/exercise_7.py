# 7. Se tienen letras para representar las estaciones del año:
# - V para verano
# - O para otoño
# - I para invierno
# - P para primavera

# Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es
# decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a
# ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O,
# B, V e I

def getYearSessionByInitial(initial_letters):
	sessions_of_year = ["summer", "spring", "winter", "fall"]

	if isinstance(initial_letters, str) and len(initial_letters) == 2:
		for session in sessions_of_year:
			if session.lower().startswith(initial_letters):
				print(f"The session of the year with the first two initial lettersfa '{initial_letters}' is: {session}")
				return
			
		print(f"No session of the year was founded with the inital letter: {initial_letters}") 
	else:
		print("You should enter the first two initial letters to get the full session of the year")


getYearSessionByInitial("su")


