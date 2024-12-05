# Escribe un programa que reciba un número del usuario e imprima si el número es par o impar utilizando una sentencia if-else.
# Entrada: 7
# Salida: El número es impar.

number = int(input("Ingresa un numero: "))

if number % 2 == 0:
    print("El numero es par.")
else:
    print("Tu numero es impar.")
