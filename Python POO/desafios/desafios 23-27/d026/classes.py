from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    salario_min = 1_612
    desconto_inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.bruto = 0
        self.salario = 0


    def analisar_sal(self):
        base = self.salario / self.salario_min
        mensagem = f"O salário de {self.nome} é de R${self.salario:.2f} e corresponde a {base:.1f} salários mínimos."
        panel = Panel(mensagem, title="Analisando Salário", width=50)
        print(panel)

    @abstractmethod
    def calc_sal(self):
        pass

class Horista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, horas_trab = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trab
        self.bruto = self.valor_hora * self.horas_trabalhadas

    def calc_sal(self):
        self.salario = self.bruto - (self.bruto * self.desconto_inss / 100)

class Mensalista(Funcionario):
    def __init__(self, nome = None, salario_bruto = Funcionario.salario_min):
        super().__init__(nome)
        self.bruto = salario_bruto

    def calc_sal(self):
        self.salario = self.bruto - (self.bruto * self.desconto_inss / 100)