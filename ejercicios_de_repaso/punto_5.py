def fahrenheit_a_celsius(fahrenheit):

  celsius = (fahrenheit - 32) * 5/9
  return celsius

temperatura_fahrenheit = 72
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
print(temperatura_fahrenheit, "grados Fahrenheit son igual a", temperatura_celsius, "grados Celsius.")