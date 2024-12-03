#hola mundo
print("Hola mundo!")
print("Me está gustando Python")

#variables 1
nombre = input("Dime como te llamas: ")
apellido = input("Ingresa tu apellido: ")

print(f"Hola {nombre} {apellido}. ¡Bienvenido a la plataforma!")

#variables 2
edad = input("Ingresa tu edad: ")
ciudad = input("Cuéntanos, ¿De dónde eres?: ")

print("¡Gracias por registrarte en la plataforma!")
print(f"Usar:{nombre} {apellido}, edad {edad}, nos visita desde: {ciudad}. ¡Ya puedes ingresar!")
print("¿Qué deseas sumar?")

#Función para realizar la suma
def sumar(x, y, z):
    return x + y + z

#Función para realizar la resta
def restar(x, y, z):
    return x - y - z

#Solicitar al usuario que ingrese los datos
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

#Calcular la suma
resultado = sumar(numero1, numero2, numero3)
resultado2 = restar(numero1, numero2, numero3)
#Mostrar el resultado
print(f"Este es tu resultado de sumar: {resultado}")
print(f"Este es tu resultado de restar: {resultado2}")

