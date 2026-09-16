""" Desafio 17 """

from rich import print
from rich.panel import Panel

class Produto:
    # Atributos de Classe

    # Atributos de Instancia
    def __init__(self, nome, preco = 0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        preco_formatado = f"R${self.preco:,.2f}"
        conteudo += f"{preco_formatado.center(30, '.')}"
        etiqueta = Panel(conteudo, title = "Produto", width = 34)
        print(etiqueta)

p1 = Produto("Iphone 13 Pro Max", 2500)
p2 = Produto("Notebook Asus Vivobook", 3200)

p1.etiqueta()
p2.etiqueta()