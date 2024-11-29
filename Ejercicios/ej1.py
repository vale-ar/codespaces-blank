# Conversión de metros a centímetros Escribe un programa que pida al usuario un número en metros y lo convierta a centímetros.
# Ejemplo:
# Entrada: Introduce la longitud en metros: 2
# Salida: La longitud en centímetros es: 200 cm


print('Conversor de metros a centímetros.')
#Variables
metro = int(input('Introduce la longitud en metros: ')) #float (números decimales/flotantes) int (números enteros)
conversion = metro * 100

print(f'La longitud en centímetros es: {conversion}cm.')