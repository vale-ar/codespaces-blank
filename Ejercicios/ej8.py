# Generar una lista de números
# Pide al usuario un número n y usa un bucle while para generar una lista de los números del 1 al n.
# Ejemplo:
# Entrada: n = 5
# Salida: [1, 2, 3, 4, 5]
# While es para situaciones hipoteticas y cuando no se cumple la condicion

n = int(input("Dame un numero: ") )

number_list = []

acumulador = 1

while n >= acumulador:
    number_list.append(acumulador)
    print(acumulador)
    acumulador = acumulador + 1

print(number_list)

