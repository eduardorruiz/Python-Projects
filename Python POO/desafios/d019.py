from rich import print
from time import sleep

class Livro:
    # Atributos de instancia
    def __init__(self, nome_do_livro, numero_de_paginas):
        self.titulo = nome_do_livro
        self.pag = numero_de_paginas
        self.pag_atual = 1

        print(f":book: Você acabou de abrir o livro\n[b u]{self.titulo}[/]\nEle tem [b u]{self.pag} páginas[/] no total.\nVocê está na [yellow]página [b]1[/][/]")

    def mostrar_final(self):
        return f":closed_book: [red]Você chegou ao final do Livro: {self.titulo}[/]"

    def fim_do_livro(self) -> bool:
        return True if self.pag_atual == self.pag else False
        # Mesma coisa que:
        if self.pag_atual == self.pag:
            return True
        else:
            return False

    def avancar_paginas(self, paginas_para_avancar = 1):
        cont = 0
        for pg in range(0, paginas_para_avancar, 1):
            if not self.fim_do_livro():
                self.pag_atual += 1
                print(f"Pág{self.pag_atual} --> ", end=" ")
                cont += 1
                sleep(0.5)
        print(f"Você avançou [u][b]{cont}[/] páginas[/] e agora está na [u]página [b]{self.pag_atual}[/][/]")
        if self.fim_do_livro():
            print(self.mostrar_final())

l1 = Livro("Diario de um Banana - edição: 3", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)