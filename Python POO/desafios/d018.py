from rich.panel import Panel
from rich import print

"""class Churrasco:
    # Atributos de Classe

    # Atributos de Instancia
    def __init__(self, titulo = "Churrasco", quantidade = 1):
        self.title = titulo
        self.quantify = quantidade

    def analisar(self):
        conteudo = f"Analisando [u blue bold]{self.title}[/] com [u bold]{self.quantify}[/] convidados"
        # Fazendo os cálculos necessários
        carne_por_pessoa = 0.4
        kg_carne = 82.40
        qntd_carne = carne_por_pessoa * self.quantify
        preco_total = qntd_carne * kg_carne
        preco_por_pessoa = preco_total / self.quantify
        conteudo += f"\nCada participante comerá [u bold]{carne_por_pessoa}Kg[/] e cada Kg custa [red bold]R${kg_carne:,.2f}[/]"
        conteudo += f"\nRecomendo comprar [u bold]{qntd_carne}Kg[/] de carne"
        conteudo += f"\nO custo total será de [bold red]R${preco_total:,.2f}[/] para comprar tudo"
        conteudo += f"\nCada pessoa pagará [bold red]R${preco_por_pessoa:,.2f}[/] para participar "
        caixa = Panel(conteudo, title=self.title, width=60)
        return print(caixa)

# Objetos
c1 = Churrasco("Churrasco do DUDU", 15)
c1.analisar()"""

# Guanabara
class Churrasco:
    # Atributos de Classe
    carne_por_pessoa = 0.4
    kg_carne = 82.40
    # Atributos de Instancia
    def __init__(self, titulo = "Churrasco", quantidade = 1):
        self.title = titulo
        self.participantes = quantidade

    def __str__(self):
        return f"Esse é o {self.title} com {self.participantes} pessoas participando."

    def calcular_qnt_carne(self)->float:
        return self.participantes * Churrasco.carne_por_pessoa

    def calcular_custo_total(self)->float:
        return self.calcular_qnt_carne() * Churrasco.kg_carne # pode ser também self.__class__.kg_carne

    def calcular_custo_individual(self):
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando [u blue bold]{self.title}[/] com [u bold]{self.participantes}[/] convidados"
        conteudo += f"\nCada participante comerá [u bold]{Churrasco.carne_por_pessoa}Kg[/] e cada Kg custa [red bold]R${Churrasco.kg_carne:,.2f}[/]"
        conteudo += f"\nRecomendo comprar [u bold]{self.calcular_qnt_carne()}Kg[/] de carne"
        conteudo += f"\nO custo total será de [bold red]R${self.calcular_custo_total():,.2f}[/] para comprar tudo"
        conteudo += f"\nCada pessoa pagará [bold red]R${self.calcular_custo_individual():,.2f}[/] para participar "
        caixa = Panel(conteudo, title=self.title, width=60)
        return print(caixa)

# Objetos
c1 = Churrasco("Churrasco do DUDU", 15)
c1.analisar()