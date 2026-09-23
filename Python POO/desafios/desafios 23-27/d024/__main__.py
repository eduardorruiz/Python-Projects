from cafeteria import *

def main():
    bebida_norma = Cha()
    bebida_norma.preparar()
    bebida_eduardo = Leite()
    bebida_eduardo.preparar()
    bebida_carlos = Cafe()
    bebida_carlos.preparar()

if __name__ == "__main__":
    main()