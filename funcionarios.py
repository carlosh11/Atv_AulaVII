class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def bonus(self):
        return self.salario * 0.10


class Gerente(Funcionario):
    def bonus(self):
        return self.salario * 0.20


funcionarios = [
    Funcionario("João", 3000.00),
    Gerente("Maria", 5000.00)
]

for funcionario in funcionarios:
    print("Nome:", funcionario.nome)
    print(f"Bônus: R$ {funcionario.bonus():.2f}")
    print()