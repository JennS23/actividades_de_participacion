def es_par(numero):

  if numero % 2 == 0:
    return True
  else:
    return False

numero = int(input("Ingrese un número: "))

if es_par(numero):
  print(numero, "es par.")
else:
  print(numero, "es impar.")