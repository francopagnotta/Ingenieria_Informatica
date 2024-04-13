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

# le consulta al usuario si quiere volver a jugar o abandonar el juego
def restart():
  restart = True

  while True:
    print("\n" + "Do you want to play again?" + "\n" + "1: YES" + "\n" + "2: NO" + "\n")

    user_choice_restart = int(input())

    if user_choice_restart == 1:
      break
    elif user_choice_restart == 2:
      restart = False
      break
    else:
      print("Please enter a valid option")
      continue

  return restart