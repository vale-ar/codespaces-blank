
# Este símbolo representa un comentario y el programa no lo ejecuta

#lee la variable, le asigna un valor y lo guarda en la memoria
nombre = input('Ingresa tu nombre:') #imprime un msje al usuario y espera que ingrese un dato
apellido = input('Ingresa tu apellido:')
ciudad = input('Ingresa tu ciudad:')

print(f'Hola, {nombre} {apellido}. Seleccionaste la ciudad: {ciudad}.') #f: format

nombre_completo = f'{nombre} {apellido}'

print(f'Nombre Completo: {nombre_completo}')

#Prueba de cambio para Github