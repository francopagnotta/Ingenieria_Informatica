# 12. Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar,
# imprimiendo un mensaje por pantalla en cada caso. Es decir, el output esperado sería:
  # > El número 1 es impar.
  # > El número 2 es par.
  # …
  # > El número 20 es par.

def ceckOddAndEvenNumbers():
    start_index = 1
    stop_index = 21
    
    for index in range(start_index, stop_index):
      if (index % 2 == 0):
        print(f"The number {index} is odd")
      else:
        print(f"The number {index} is even")
   
ceckOddAndEvenNumbers()


