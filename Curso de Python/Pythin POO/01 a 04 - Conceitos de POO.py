# Aula 01 - - - - - - - - - - - - - - - - - - -

    # OOP - Object Oriented Programming
    # OOAD - Object Oriented Analysis and Design ( Analise e Projeto de Sistemas Orientado a Objetos )
    # UML

# Aula 02 - - - - - - - - - - - - - - - - - - -

    # Vantagens de programar em POO: COMERN
        # C - Confiabilidade: O isolamento entre as partes gera algo mais seguro. Ao alterar uma, nenhuma outra é afetada.
        # O - Oportunidade: Ao dividir tudo em partes, cada uma delas pode ser desenvolvidas de maneira simultanêa.
        # M - Manutenibilidade: Atualizar é mais facil. Uma alteração vai beneficiar todas as partes relacionadas.
        # E - Extensividade: Um sistema consegue aclopar outras partes, não é estático, para crescer e permanecer útil.
        # R - Reuso: Objetos que foram criados para um sistema podem ser aproveitados em outros sistemas.
        # N - Naturalidade: Mais fácil de entender. Maior atenção as funcionalidades do que aos detalhes de implementação.

# Aula 03 - - - - - - - - - - - - - - - - - - -

    # Definição de CLASSE:
        # as classes são como moldes e modelos, que contém os mesmo atributos e métodos.
    # Definição de INSTANCIA:
        # seguir o padrão que foi definido na classe, para criar um objeto.
    # Definição de OBJETOS:
        # Um objeto é a instância de uma classe.
        # Coisa material ou abstrata que é feita a partir de um modelo(classe) e pode ser
# descrita por meio das suas caracteristicas(atributos), comportamentos(métodos) e estado atual.
    # Definição de ESTADO:
        # Os estados são definidos a partir dos valores dos atributos, de um objeto, que foi gerado atraves de uma classe.

# Aula 04 - - - - - - - - - - - - - - - - - - -

# Definição de Objetos, usando variaveis:
    # As variaveis simples, primeiro tinham o problema de conseguir armazenar apenas um valor.
    # Esse problema foi solucionado com a criação de variaveis compostas, como listas e tuplas.
    # As variaveis compostas tinham problemas por não conseguir dar nome aos indices, surgem os dicionarios.
    # O problema principal das variaveis era a separação entre dados e funções, que ficavam em lugares dif.
    # Portanto, surgem os OBJETOS, que são a evolução das variaveis.
    # Assim, um OBJETO é uma variavel que além de guardar dados, pode executar funcionalidades.
    # Em outras palavras, OBJETOS, são variaveis que, além de guardar dados, podem fazer coisas com os dados.

# CRIANDO UM EXEMPLO:
# Declaração da Classe
class MinhaClasse: #ideal que o nome da classe começe com letra MAIUSCULAS.
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
obj = MinhaClasse() # Os "()" estão instanciando, chamando o metodo construtor
# o metodo construtor é feito por ( def __init__(self): )



