# Tiempo en segundos
# Pide al usuario una cantidad de horas, minutos y segundos, y calcula el tiempo total en segundos.
# Ejemplo:
# Entrada:
# Horas: 1
# Minutos: 15
# Segundos: 30
# Salida:
# El tiempo total es: 4530 segundos

print('Tiempo en segundos.')
print('Proporciona los siguientes datos: ')
#variables
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))
tiempo_total_segundos = (horas * 3600) + (minutos * 60) + segundos

print(f'El tiempo total es: {tiempo_total_segundos}')