# 5. Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”. Cada elemento va
# a ser representado con una letra: R para piedra, P para papel y T para tijera.

# a. Hacer una función que le haga al usuario ingresar alguna de esas letras, e imprima por pantalla
# la jugada para ganarle. Por ejemplo:
# > ¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T)
# > P
# > Tijera. ¡Te gané!

# ATENCIÓN: Observar cómo se usa una frase inicial para darle a entender al usuario lo que tiene
# que hacer (en este caso ingresar alguna de las tres letras).

# b. Mostrar por pantalla el mensaje “NO vale” cuando el usuario ingresa una letra no válida
# (distinta de R, P o T).


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

# maneja la logica de inicio, evaluacion de opciones, reinicio y finalizacion del juego
def playRockPapperOrScissor():
  play = True

  while play:
    user_choice = getUserChoce()

    if user_choice == 0:
      showFeedback(user_choice, 1)
    elif user_choice == 1:
      showFeedback(user_choice, 2)
    elif user_choice == 2:
      showFeedback(user_choice, 0)
    else:
      print("Please enter a valid option")
      continue

    play = restart()
  else:
    print("Bye!")
    
playRockPapperOrScissor()