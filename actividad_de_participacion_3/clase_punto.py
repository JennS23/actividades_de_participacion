from math import sqrt

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f'Punto: ({self.x}, {self.y})')

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def distancia(self, otro_punto):
        return ((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2) ** 0.5
    
    def __str__(self):
        return f"Punto({self.x}, {self.y})"