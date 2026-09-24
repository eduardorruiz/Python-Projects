import random
from abc import ABC, abstractmethod
from rich import print

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 100):
        if self.vida > 0 and alvo.vida > 0:
            # vai rolar o golpe
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f"[blue]{self.nome}({self.vida})[/] atacou [red]{alvo.nome}({alvo.vida})[/] com um [blue]{golpe}[/]")
            alvo.receber_dano(forca)
        else:
            print(f"O ataque [{self.nome} --> {alvo.nome}] não pode acontecer.")


    def receber_dano(self, dano):
        qntd_dano_sofrida = random.randint(0, dano)
        self.vida -= qntd_dano_sofrida
        if self.vida < 0:
            self.vida = 0
            print(f"[b]{self.nome} morreu...[/]")
        print(f"[blue b]{self.nome}({self.vida})[/] recebeu [b][ {qntd_dano_sofrida} ] de dano.[/]")
    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe de Machado", "Pulo Giratório"]
    def curar(self, cura = 100):
        qntd_de_cura = random.radint(0, cura)
        self.vida += qntd_de_cura
        print(f"[blue]{self.nome}({self.vida})[/] usou uma atadura e [green]recuperou {qntd_de_cura} pontos[/] de vida.")

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio de Luz", "Magia Estática"]

    def curar(self, cura = 100):
        qntd_de_cura = random.randint(0, cura)
        self.vida += qntd_de_cura
        print(f"[blue]{self.nome}({self.vida})[/] fez uma magia e [green]recuperou {qntd_de_cura} pontos[/] de vida.")