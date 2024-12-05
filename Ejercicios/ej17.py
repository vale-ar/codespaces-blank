# Escribe un programa que pida al usuario un número y use una sentencia if-else
# para determinar si el número es positivo, negativo o cero.
# Entrada: -3
# Salida: El número es negativo.

num = float(input("Ingresa un numero: "))

if num == 0:
    print("El numero es 0.")
elif num < 0:
    print("El numero es negativo.")
else:
    print("El numero es positivo.")

