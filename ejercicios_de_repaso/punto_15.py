def es_palindromo(texto):

  texto = texto.lower()
  texto = texto.replace(" ", "") 

  
  texto_invertido = texto[::-1]

  return texto == texto_invertido

# Ejemplos de prueba
texto1 = "rotor"
texto2 = "OrO"
texto3 = "Salas"

print(es_palindromo(texto1))
print(es_palindromo(texto2))
print(es_palindromo(texto3))
