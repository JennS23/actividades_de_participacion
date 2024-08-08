import math

class Rectangulo:
    def __init__(self, esquina_superior_izquierda, esquina_inferior_derecha):
        
        self.esquina_superior_izquierda = esquina_superior_izquierda
        self.esquina_inferior_derecha = esquina_inferior_derecha

    def calcular_perimetro(self):
        
        x1, y1 = self.esquina_superior_izquierda
        x2, y2 = self.esquina_inferior_derecha
        base = abs(x2 - x1)
        altura = abs(y2 - y1)
        return 2 * (base + altura)

    def calcular_area(self):
        x1, y1 = self.esquina_superior_izquierda
        x2, y2 = self.esquina_inferior_derecha
        base = abs(x2 - x1)
        altura = abs(y2 - y1)
        return base * altura

    def es_cuadrado(self):
        x1, y1 = self.esquina_superior_izquierda
        x2, y2 = self.esquina_inferior_derecha
        base = abs(x2 - x1)
        altura = abs(y2 - y1)
        return base == altura

# Ejemplo de uso
rectangulo1 = Rectangulo((1, 3), (5, 1))
print("Perímetro:", rectangulo1.calcular_perimetro())
print("Área:", rectangulo1.calcular_area())
print("¿Es un cuadrado?", rectangulo1.es_cuadrado())
