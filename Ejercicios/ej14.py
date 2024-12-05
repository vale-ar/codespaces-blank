# Usa un bucle for para calcular la suma de todos los números pares entre 1 y 50 e imprime el resultado.
# La suma de los números pares entre 1 y 50 es: 650

suma = 0

for num in range(1,51):
    if num % 2 == 0:
        suma += num

print(f"La suma de los numeros pares entre 1 y 50 es: {suma}")

