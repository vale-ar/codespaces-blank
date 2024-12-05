# Say Hello
#def: le decimos a python que definiremos una funcion, luego indicamos su nombre como si fuera una variable
# funcion que no recibe parametros
def print_hello_world(): 
    print("Hello world - from function!")

# llamamos/invocamos a la funcion para que el programa la ejecute
# podemos invocar la funcion las veces que queramos y se imprimira en la terminar
# print_hello_world() 
# print_hello_world()

# definimos una funcion con parametros propios; podemos reutilizar estos parametros dentro de la funcion
def suma(num1, num2):
    return num1 + num2 #retorna el resultado de la suma y este queda disponible en el resto del programa

def resta(num1, num2):
    return num1 - num2

operacion = input("Que quieres hacer? sumar o restar?: ")
parametro_1 = float(input("Ingresa primer numero: "))
parametro_2 = float(input("Ingresa segundo numero: "))

# .lower lleva todos los string acoplados a una variable a minusculas
if operacion.lower == "sumar":
    resultado = suma(parametro_1, parametro_2)
elif operacion.lower == "restar":
    resultado = resta(parametro_1, parametro_2)
else:
    resultado = "Hubo un error!"

print(f"El resultado de tu operacion es: {resultado}") #imprime el resultado

# Function to return the phrase "Hello <name>"
def hello_name(name):
    response = f"Hello {name}"
    return response

text_result = hello_name("Luis")

print(text_result)
