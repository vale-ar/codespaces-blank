# Edad en el futuro
# Crea un programa que pida el nombre del usuario y su edad.
# Luego, calcula cuántos años tendrá en 10 años.
# Ejemplo:
# Entrada:
# Introduce tu nombre: Ana
# Introduce tu edad: 25
# Salida:
# Hola Ana, en 10 años tendrás 35 años.

print('¿Qué edad tendré en 10 años en el futuro?')
#variables
nombre = input('Introduce tu nombre: ')
edad = int(input('Introduce tu edad: '))
conversion = edad + 10

print(f'Hola {nombre}, en 10 años tendrás {conversion} años.')