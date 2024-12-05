# Escribe un programa que genere un número aleatorio entre 1 y 20 y permita al usuario adivinarlo. El programa debe darle pistas si el número es mayor o menor al número a adivinar,
# utilizando un bucle while.
# Entrada: 10
# Pista: El número es menor.

print("¡Adivina el número!")
print("Estoy pensando en un número entre 1 y 20...")
print("¿En qué número estoy pensando?")

import random

random_num = random.randint(1, 20)

while True:
    intento = int(input("Adivina el numero: "))
    if intento == numero_aleatorio:
        print("¡Te felicito! Adivinaste el número.")
        break
    elif intento < numero_aleatorio:
        print("El numero es mayor.")
    else:
        print("El numero es menor.")

