# Promedio de tres números
# Solicita tres números al usuario y muestra su promedio.
# Ejemplo:
# Entrada:
# Número 1: 5
# Número 2: 7
# Número 3: 10
# Salida:
# El promedio es: 7.33

print('Promedio de tres números')

num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))
num3 = float(input('Número 3: '))
total = num1 + num2 + num3 
promedio = total / 3

print(f'El promedio es: {promedio}')