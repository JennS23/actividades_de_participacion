def encontrar_max_min(lista):

  if not lista:
    return None, None

  maximo = lista[0]
  minimo = lista[0]

  for numero in lista:
    if numero > maximo:
      maximo = numero
    if numero < minimo:
      minimo = numero

  return maximo, minimo

mi_lista = [3, 7, 2, 9, 5]
num_max, num_min = encontrar_max_min(mi_lista)

print("El número más grande es:", num_max)
print("El número más pequeño es:", num_min)
