# Declaração de Classe
class Pessoa:
    def __init__(self): # Metodo construtor
        # Atributos de instancia
        self.nome = ''
        self.idade = 0

    # Metodos de instancia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos de idade"

# Declaração de Objetos
pss1 = Pessoa()
pss1.nome = 'Eduardo'
pss1.idade = 18
print(pss1.mensagem())