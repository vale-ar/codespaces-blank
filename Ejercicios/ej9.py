# Sumar elementos de una lista
# Crea un programa que use un bucle for para sumar todos los números de una lista proporcionada por el usuario.
# Ejemplo:
# Entrada: [3, 5, 7, 2]
# Salida: La suma de los elementos es: 17
# El for es para recorrer elementos

entrada = input("Proporciona una lista de numeros separados por comas: ")
lista_de_numeros = entrada.split(",")

suma = 0

for n in lista_de_numeros:
    suma = suma + int(n)

print(f"La suma de los numeros es: {suma}")



