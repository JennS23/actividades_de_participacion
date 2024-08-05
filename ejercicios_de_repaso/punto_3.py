import random

cantidad_numeros = 10

numeros_aleatorios = []

for _ in range(cantidad_numeros):
    numero_aleatorio = random.randint(1, 100)  # Números entre 1 y 100
    numeros_aleatorios.append(numero_aleatorio)

print(numeros_aleatorios)