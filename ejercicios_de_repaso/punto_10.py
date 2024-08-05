def factorial(numero):

  if numero < 0:
    return None 
  elif numero == 0:
    return 1
  else:
    factorial = 1
    for i in range(1, numero + 1):
      factorial *= i
    return factorial

num = 5
resultado = factorial(num)
if resultado is not None:
  print("El factorial de", num, "es", resultado)
else:
  print("El número ingresado no es válido.")
