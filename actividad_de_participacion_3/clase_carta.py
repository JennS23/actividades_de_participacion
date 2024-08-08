class Carta:
    PICAS = "picas"
    CORAZONES = "corazones"
    DIAMANTES = "diamantes"
    TREBOLES = "tréboles"

    def __init__(self, valor, pinta):
        
        self.valor = valor
        if pinta not in (Carta.PICAS, Carta.CORAZONES, Carta.DIAMANTES, Carta.TREBOLES):
            raise ValueError("Pinta inválida")
        self.pinta = pinta

