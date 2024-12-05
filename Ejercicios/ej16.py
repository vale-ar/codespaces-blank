# Pide al usuario un número entero e imprime la tabla de multiplicar de ese número del 1 al 10
# utilizando un bucle for.
# Entrada: 3
# Salida:
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30

num = int(input("¡Hola usuario! Ingresa un número entero: "))

for i in range(1,11):
    print(f"{num} x {i} = {num * i}")
    