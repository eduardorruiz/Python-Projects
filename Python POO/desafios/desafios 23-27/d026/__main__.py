from rich import inspect

from classes import *

def main():
    f1 = Horista("Paulo", 25, 250)

    f1.calc_sal()
    f1.analisar_sal()
    #inspect(f1)
    f2 = Mensalista("Amanda", 8500)
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == "__main__":
    main()
    