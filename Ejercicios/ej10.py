#Filtrar números pares
#Solicita una lista de números al usuario y usa un bucle for para agregar solo los números pares a una nueva lista.
#Ejemplo:
#Entrada: [1, 2, 3, 4, 5, 6]
#Salida: [2, 4, 6]

entrada = input("Proporciona una lista de numeros separados por comas: ")
lista_de_numeros = entrada.split(",")

lista_numero_par = []

for n in lista_de_numeros:
    if int(n) % 2 == 0:
        lista_numero_par.append(n)
print(lista_numero_par)
