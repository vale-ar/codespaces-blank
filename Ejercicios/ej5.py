# Cálculo del IVA
# Pide al usuario el precio de un producto y calcula el precio final con un IVA del 19%.
# Ejemplo:
# Entrada:
# Introduce el precio del producto: 100
# Salida:
# El precio final con IVA es: $119

print('Cálcula el IVA')

#variables
precio_producto = float(input('Introduce el precio del producto: '))
iva = precio_producto * 0.19
precio_final = precio_producto + iva

print(f'El precio final con IVA es: ${precio_final}')