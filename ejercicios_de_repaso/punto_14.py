def calcular_media(lista_numeros):

  if len(lista_numeros) == 0:
    return None  # Si la lista está vacía, no hay media
  
  suma = sum(lista_numeros)
  media = suma / len(lista_numeros)
  return media

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5]
resultado = calcular_media(mi_lista)
print("La media es:", resultado)
