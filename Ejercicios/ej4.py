# Calculadora simple
# Pide al usuario dos números y muestra la suma, resta, multiplicación y división de esos números.
# Ejemplo:
#Entrada:
# Primer número: 8
# Segundo número: 4
# Salida:
# Suma: 12
# Resta: 4
# Multiplicación: 32
# División: 2

print('Calculadora simple.')
print('¡Dame 2 números y te mostraré el resultado de suma, resta, multiplicación y división!')
#variables
num1 = float(input('Primer número: '))
num2 = float(input('Segundo número: '))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print('Estos son los resultados:')
print(f'Suma: {suma}')
print(f'Resta: {resta}')
print(f'Multiplicación {multiplicacion}')
print(f'División: {division}')

