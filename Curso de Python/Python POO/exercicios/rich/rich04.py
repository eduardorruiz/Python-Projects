from rich import inspect

# EX 03 - Só para ver o inspect(lá no final)
class ContaBancaria:
    """
    DOC: Cria uma conta bancária e permite fazer saques e depósitos.
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print('-*-' * 20)
        print(f"Conta [{self.id}] criada com sucesso. Saldo atual de {self.saldo:,.2f}.")
        print('-*-' * 20)

    def __str__(self):
        return f"\n\nA conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo."

    def depositar(self, valor):
        self.saldo += valor
        print(f'\nDepósito de R${valor:,.2f} autorizado com sucesso {self.titular}, na conta: [{self.id}].\nO saldo atual de sua conta é: R${self.saldo:,.2f}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'\nSaque de R${valor:,.2f} --> NEGADO, na conta [{self.id}] : SALDO INSUFICIENTE')
        else:
            self.saldo -= valor
            print(f'\nSaque de R${valor:,.2f} autorizado com sucesso {self.titular}, na conta: [{self.id}].\nO saldo atual de sua conta é: R${self.saldo:,.2f}')


c1 = ContaBancaria(2007, "Eduardo", 2075)
print(c1.__doc__)
c1.depositar(855)
c1.sacar(1150)
print(c1)

inspect(c1)