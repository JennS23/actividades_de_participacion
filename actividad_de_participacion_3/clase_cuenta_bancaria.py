class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.balance += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if monto > self.balance:
            raise ValueError("Fondos insuficientes.")
        self.balance -= monto

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se ha aplicado una cuota de manejo de ${cuota:.2f}. Nuevo saldo: ${self.balance:.2f}")

    def mostrar_detalles(self):
        print("Detalles de la cuenta:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print("Propietarios:")
        for propietario in self.propietarios:
            print(f"- {propietario}")
        print(f"Saldo:   
 ${self.balance:.2f}")