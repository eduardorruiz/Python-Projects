from rich import print

class Caneta:
    def __init__(self, cor_da_caneta = "black"):
        escolha = ""
        match cor_da_caneta.lower().strip():
            case "azul":
                escolha = "blue"
            case "vermelho" | "vermelha":
                escolha = "red"
            case "verde":
                escolha = "green"
            case "amarelo" | "amarela":
                escolha = "yellow"
            case _:
                escolha = "black"
        self.cor = escolha
        self.tampada = True

    def tampar(self) -> bool:
        self.tampada = True

    def destampar(self) -> bool:
        self.tampada = False
        return self.tampada

    def escrever(self, escreva):
        if self.tampada:
            print(f":prohibited: [red b]A caneta está tampada![/] ")
        else:
            print(f"[{self.cor}]{escreva}[/]", end='')

    def quebrar_linha(self, vezes = 1):
        for c in range(0, vezes):
            print(" ")

c1 = Caneta("azul")
c2 = Caneta("vermelha")

c1.destampar()
c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2)
c2.destampar()
c2.escrever("Olá, Eduardo!")