'''Cálculo del promedio y evaluación
Escribe un programa que permita al usuario ingresar números (notas) hasta que escriba la palabra "fin". El programa debe calcular el promedio de las notas ingresadas.
Usa un bucle while para obtener las notas y una condicional para determinar si el promedio indica que el usuario aprobó o reprobó.

Condiciones:
Si el promedio es mayor o igual a 4.0, el usuario aprueba.
Si es menor a 4.0, el usuario reprueba.
Ejemplo:

Entrada: 5, 3, 4, fin

Salida:
El promedio es: 4.0
¡Aprobaste!

Entrada: 2, 3, fin

Salida:
El promedio es: 2.5
Reprobaste.'''

lista_notas = []
notas = "" #String vacio
suma = 0
cantidad_notas = 0

while notas != "fin":
    notas = input("Ingresa una nota o escribe 'fin' para salir: ")
    if notas != "fin":
        lista_notas.append(notas)
        cantidad_notas += 1
        suma += float(notas)
    else: 
        break
    
promedio = suma / cantidad_notas

if promedio >= 4:
    print("Aprobaste:)")
else:
    print("Reprobaste:() ")
    
print(f"El promedio es: {promedio}")