import requests
import json
import random

def trivia_fetch(num):
  url = f"http://numbersapi.com/{num}?json"
  respuesta = requests.get(url)
  trivia = json.loads(respuesta.content)
  return trivia

def main():
  print("Hello learners!")
  print("Hagamos un quiz!")

  res_user = input("Ingresa un numero o presiona enter para obtener uno aleatorio: ")

  if res_user == "":
    res_user = "random"

  trivia = trivia_fetch(res_user)

  # Escoge aleatoriamente un dato del diccionario de la respuesta
  dato_aleatorio = random.choice(list(trivia.values()))
  print(dato_aleatorio)

if __name__=="__main__":
  main()