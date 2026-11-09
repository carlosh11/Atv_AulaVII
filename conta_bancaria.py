class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado!")
        else:
            print("Valor inválido!")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido!")
        elif valor > self._saldo:
            print("Saldo insuficiente!")
        else:
            self._saldo -= valor
            print("Saque realizado!")

    @property
    def saldo(self):
        return self._saldo


conta = ContaBancaria("Carlos", 100.00)

conta.depositar(50.00)
conta.sacar(30.00)

print(f"Titular: {conta.titular}")
print(f"Saldo final: R$ {conta.saldo:.2f}")