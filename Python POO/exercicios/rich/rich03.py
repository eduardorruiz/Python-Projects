from rich import print
from rich.table import Table

tabela = Table(title="Tabela da Familia")
tabela.add_column("Nome", width=14, justify="left")
tabela.add_column("Sexo", width=14, justify="center")
tabela.add_row("Eduardo", "Masc")
tabela.add_row("Norma", "Fem")
tabela.add_row("Kaleb", "Masc")

print(tabela)