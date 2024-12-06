# APIs: Numbers API

#Agregaremos paquetes que vienn incluidos en python

import json #necesario para convertir los datos que recibimos en la respuesta en un diccionario
import requests # necesario para hacer peticiones HTTP desde python

# Paquete que nos permite traer la info del servidor
# Generamos la peticion con .get (verbo) 
# .get necesita un parametro de tipo string, especificamente una url de donde haremos la peticion
# definimos una variable para guardar la respuesta a la peticion .get


#Creamos una variable input para hacerlo interactivo y luego lo insertamos dentro de la url
num = int(input("Ingrese un numero para consultar: "))

response = requests.get(f"http://numbersapi.com/{num}?json") #realiza la peticion .get a la API

trivia = json.loads(response.content) # Toma el contenido de la respuesta y la convierte en un formato utilizable (python: diccionario)

print(trivia) # Imprime todos los datos encontrados

# print(trivia['text']): Imprime solamente el parametro 'text'

# Obtener los datos en formato JSON
#    data = response.json()

    # Extraer y mostrar la información
#    print(f"Hecho sobre el número {number}: {data['text']}")