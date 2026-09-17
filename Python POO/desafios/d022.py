""" DESAFIO 22 - SIMULAÇÃO DE UM CONTROLE REMOTO
onde podemos passar canais e mexer no volume! """

from rich import print
from rich.panel import Panel

def informacoes_iniciais():
    print("-*" * 34)
    print("[bold] ESSE PROGRAMA TEM COMO OBJETIVO A SIMULAÇÃO DE UM CONTROLE REMOTO")
    print("-*" * 34)
    print("[bold] A SEGUIR, OS COMANDOS:[/]")
    print('-+' * 12)
    print("[bold]LIGAR/DESLIGAR A TV [ @ ] [/]")
    print('--' * 12)
    print("[bold]AUMENTAR UM CANAL   [ > ] [/]")
    print('--' * 12)
    print("[bold]DIMINUIR UM CANAL   [ < ] [/]")
    print('--' * 12)
    print("[bold]AUMENTAR UM VOLUME  [ + ] [/]")
    print('--' * 12)
    print("[bold]DIMINUIR UM VOLUME  [ - ] [/]")
    print('--' * 12)
    print("[bold]SAIR DO PROGRAMA    [ 0 ] [/]")
    print('-+' * 12)
    print("-*" * 34)
    print('')

class ControleRemoto:
    # Atributos de Classe
    canal_min: int = 1
    canal_max: int = 6
    volume_min: int = 0
    voleme_max: int = 5

    # Atributos de Instância
    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def ligar_e_desligar(self):
        self.ligado = not self.ligado

    def mostrar_tv(self):
        conteudo = ''
        if not self.ligado: # Se tv não estiver ligada.
            conteudo = f":prohibited: [red b]A TV está desligada[/]"
        else: # Se tv estiver ligada
            conteudo = f"CANAL  = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[yellow on yellow] {canal} [/] "
                else:
                    conteudo += f" {canal} "
            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.voleme_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f"[black on cyan] {volume} [/]"
                else:
                    conteudo += f"[black on white] {volume} [/]"
        tv = Panel(conteudo, title="[ TV ]", width=35)
        print(tv)

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.voleme_max:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1

# Objetos

informacoes_iniciais()
c = ControleRemoto()
comando = ""
while comando != "0":
    c.mostrar_tv()
    comando = str(input(f" < CH{c.canal_atual} >  - VOL{c.volume_atual} + "))
    match comando:
        case '@':
            c.ligar_e_desligar()
        case '>':
            c.canal_mais()
        case '<':
            c.canal_menos()
        case '+':
            c.volume_mais()
        case '-':
            c.volume_menos()
    print("\n" * 10)

