""" Desafio 16 """

from rich import print
from rich import inspect

class Funcionario:
    """
    DOC:
    """
    # Atributos de Classe (todos objetos tem esse atributo).
    empresa = "Curso em Vídeo"
    # Atributos de Instancia (Cada OBJETO tem o seu proprio atributo.)
    def __init__(self, nome = "", setor = "", cargo = ""):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f" Olá, sou [bold]{self.nome}[/] e sou [bold]{self.cargo}[/] do setor de [bold]{self.setor}[/] na empresa {Funcionario.empresa}."

    # COM O PRINT Lá em baixo não coloco o print - Guanabara não recomenda
    def apresentar(self) -> str:
        print(f" Olá, sou [bold]{self.nome}[/] e sou [bold]{self.cargo}[/] do setor de [bold]{self.setor}[/].")

c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())
#inspect(c1, methods=True)

c2 = Funcionario("Pedro", "Ti", "Programador")
c2.apresentar()