
# Variable: espacio en la memoria que nos permite almacenar. Lo ideal es que sean lo más descriptivas posibles

name = 'Jose' #Declaramos la variable y le asignamos un valor

student name = 'Jose' #las variables no pueden incluir espacios
student_name = 'Jose' #para separar los conceptos podemos aplicar _ determinado por desarrolladores como "snake_case"
2student_name = 'Jose' #No empezar variable con numeros
student_name1 = 'Jose' #Si podemos terminar una variable con numeros

# Tipos de datos primitivos
# Integers, numeros enteros
integer_1 = 10
integer_2 = 0

# Floating point number (Float): numeros decimales
float_1 = 12.3
float_2 = -5.2

# String: Todo dato de texto que quiera imprimirse y/o guardarse, que este dentro de las comillas, incluidos numeros, simbolos, espacios, etc
string_1 = 'this is a sentence.'
string_2 = 'and this is another.'

# Boolean: Nos prmite definir verdadero o falso, el tipo de dato buleano solo puede tener dos valores posibles. En el caso de python, "True" y "Flase"
# son sintáxis especificas del programa por lo que siempre serán escritas con la primera letra mayúscula

boolean_1 = True
boolean_2 = False

# Otros datos que podremos almacenar dentro de las variables

# List, vectores, arrays
list_1 = []
# Lista de estudiantes
lista_estudiantes = ['Andrés', 'Bastián', 'Benjamín'] #Los corchetes me permiten definir una lista. Para separarlos ocuparemos las ","
#                       0           1           2    Python identifica a los elementos con su propio index para representar los valores dentro de una lista. index=indice
# Para imprimir a un valor especifico de una lista tenemos que definirlo según su indice, por ej:
print(lista_estudiantes[1])

lista_estudiantes.append('Constanza') #.append para agregar otro valor a la lista

carrito_del_super = []

item1 = input('Ingresa un producto: ')
item2 = input('Ingresa un producto: ')

carrito_del_super.append(item1)
carrito_del_super.append(item2)

print(carrito_del_super) #Imprime la ejecucion de los input y crea la lista según los datos

# Dictionaries
# Nos permite estructurar datos complejos con multiples propiedades
dictionary_1 = {
    'Computer Program': 'A series of instructions that can be executed by a computer',
    'Syntax': 'The rules we create for computers and programmers to follow to avoid ambiguity and five strict meanings',
    'Programming Language': 'A formal set of syntax for writing a computer program'
}

student_data = {
    'nombre': 'José',
    'apellido': 'Martínez',
    'edad': 30,
    'dirección': 'calle',
    'graduado': True,
    'materias_cursadas': ['python', 'javascript', 'sql']
}

product_item = {
    'name': 'Zapatilla Nike',
    'price': 100,
    'stock': 10000,
    'description': 'Un texto descriptivo'
}

product_item2 = {
    'name': 'Zapatilla Nike',
    'price': 100,
    'stock': 10000,
    'description': 'Un texto descriptivo'
}

products_list = [product_item, product_item2]

