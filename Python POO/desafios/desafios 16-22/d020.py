""" Desafio 20 """

from rich import print, inspect
from rich.panel import Panel
class Gamer:
    def __init__(self, nome, nickname):
        self.nome = nome
        self.nick = nickname
        self.jogos_favoritos = list()
    def add_favoritos(self, favoritos):
        self.jogos_favoritos.append(favoritos)

    def ficha(self):
        conteudo = f"Nome real: [b on blue] {self.nome} [/]\n"
        conteudo += f"Jogos favoritos:\n"
        #manipulando a lista pra mostrar
        self.jogos_favoritos.sort()
        for jogos in self.jogos_favoritos:
            conteudo += f":video_game:[bold] {jogos} [/]\n"
        panel = Panel(conteudo, title=f"Jogador <{self.nick}>", width = 40)
        print(panel)

j1 = Gamer("Eduardo Ruiz", "1Dudzz")
j1.add_favoritos("Fortnite")
j1.add_favoritos("Valorant")
j1.add_favoritos("Minecraft")
j1.add_favoritos("Pokemon GO")
j1.ficha()
inspect(j1)