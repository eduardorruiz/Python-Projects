# Recriação do ex01 mais simplificado.
# Declaração de Classe
class Pessoa:
    def __init__(self, nome = "", idade = 0): # Metodo construtor
        # Atributos de instancia
        self.nome = nome
        self.idade = idade

    # Metodos de instancia
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome}, Idade = {self.idade}"
# Declaração de Objetos
pss1 = Pessoa('Kaleb', 7)
pss1.aniversario()
print(pss1.mensagem())
print(pss1.__dict__) # Attribute
print(pss1.__getstate__()) # Method

pss2 = Pessoa("Eduardo", 18)
print(pss2.mensagem())