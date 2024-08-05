import math

def area_circulo(radio):
  area = math.pi * radio**2
  return area

radio = int(input("ingrese el radio:"))
area_calculada = area_circulo(radio)
print("El área de un círculo con radio", radio, "es:", area_calculada)