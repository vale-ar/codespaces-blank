#hola mundo
print("Hola mundo!")
print('Me está gustando Python')

#variables 1
nombre = input('Dime como te llamas: ')
apellido = input('Ingresa tu apellido: ')

print(f'Hola {nombre} {apellido}. ¡Bienvenido a la plataforma!')

#variables 2
edad = input('Ingresa tu edad: ')
ciudad = input('Cuéntanos, ¿De dónde eres?: ')

print('¡Gracias por registrarte en la plataforma!')
print(f'Usar:{nombre} {apellido}, edad {edad}, nos visita desde: {ciudad}. ¡Ya puedes ingresar!')
print('¿Qué deseas sumar?')

#Función para realizar la suma
def sumar(x, y):
    return x + y 

#Solicitar al usuario que ingrese los datos
numero1 = float(input('Introduce el primer número: '))
numero2 = float(input('Introduce el segundo número: '))

#Calcular la suma
resultado = sumar(numero1, numero2)
#Mostrar el resultado
print('Este es tu resultado: {resultado}')