options = ["rock", "papper", "scissor"]

# le pide al usuario que ingrese una opcion y la devuelve
def getUserChoce():
  print("Let's play! Insert an option")

  for index, option in enumerate(options):
    print(f"{index + 1}: {option}")

  return int(input()) - 1

# Le muestra el feedback al usuario
def showFeedback(user_choice, game_choice):
  print(f"You chose: {options[user_choice]}!")
  print(f"I chose: {options[game_choice]}! I win!")
