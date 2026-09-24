from classes import *
from rich import inspect


def main():
    p1 = Guerreiro("Guerreiro", 100)

    p2 = Mago("Mago", 100)
    p1.atacar(p2, 100)
    p3 = Guerreiro("Kratos", 150)
    p2.curar()
    p2.atacar(p3, 100)
    #inspect(p1)
    #inspect(p2)
    #inspect(p3)

if __name__ == "__main__":
    main()