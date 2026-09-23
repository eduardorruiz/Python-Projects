from rich import print
from transportes import *
from rich.table import Table

def main():
    distancia = 5
    """ entrega = Drone(distancia)
    print(f" Frete de {type(entrega).__name__} em {distancia}Km = {entrega.calcular_frete()}")"""

    viagem = [Moto(distancia), Caminhao(distancia), Drone(distancia)]
    tabela = Table(title = "Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for item in viagem:
        tabela.add_row(f"{distancia}Km", f"{type(item).__name__}" , f"{item.calcular_frete()}")

    print(tabela)
if __name__ == "__main__":
    main()