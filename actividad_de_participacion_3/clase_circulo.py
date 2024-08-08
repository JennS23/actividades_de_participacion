import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def pertenece_al_circulo(self, punto):
        x_centro, y_centro = self.centro
        x_punto, y_punto = punto
        distancia = math.sqrt((x_punto - x_centro)**2 + (y_punto - y_centro)**2)
        return distancia <= self.radio

