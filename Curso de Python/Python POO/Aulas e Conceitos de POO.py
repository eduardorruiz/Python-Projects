# Aula 01 - - - - - - - - - - - - - - - - - - -
from urllib.parse import uses_params


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

# Aula 05 - - - - - - - - - - - - - - - - - - -

# Para criar uma documentação para a classe abra """ e feche """, a seguir um exemplo:
class MinhaClasse:
    """
    Essa classe é apenas um exemplo didático.
    """
# Para ver utilize
print(MinhaClasse.__doc__) # Dunder Attribute (__doc__)

# Metodo __str__ (Dunder Attribute também)
    # O metodo str, mostra o endereço na mémoria oque é meio inutil e a classe que pertence
    # então se utilizo um def __str__(self): Mostrando os dados de um jeito + amigavel
    # Então antes era assim, por exemplo:
        #print(fala1.mensagem())
    # Depois do __str__(), fica assim:
        #print(fala1)

# Metodo __dict__ (Attribute)
    # Mostra a exibição como se fosse um dicionário.

# Metodo __getstate__() (Dunder Method(tem parenteses, por isso é um metodo))
    # Mesma coisa que o __dict__, mas pode programar um estado.

# Metodo __class__ (Dunder Attribute também)
    # Mostra o nome da classe do objeto que você coloca

# Aula Extra - RICH Library - - - - - - - - - - - - - - - - - - -
# VEJA EXEMPLOS NA PASTA RICH

    # Ao importar a função print da biblioteca rich
        # Podemos utilizar para colorir as coisas, assim:
        # print("[red]Para pintar tudo isso de vermelho[/]")

    # EMOJIS
        # Para usar emoji é apenas fazer isso:
        # print("nossa que joia:+1:") --> colocar o nome do emoji dentro de "::"

    # Comando rich.emoji
        # Ir no terminal e digitar: python -m rich.emoji
        # Para ver a lista completa de todos os emojis.

    # Classe Panel
        # Para usar: Panel("A mensagem que quer dentro", title="caixa", style="red", width = 10)
        # Width é a largura

    # Classe Table
        # Para usar: Table(title=""TITULO DA TABELA)
        # Adicionar colunas: nome_da_tabela.add_column("COL 1", caracteristicas_aqui)
        # Adicionar linhas: nome_da_tabela.add_column("linha 1", caracteristicas_aqui)
        # Exemplos em rich/rich03

    # Comando Install() de rich.traceback
        # Para usar: from rich.tracebak import install
        # Após isso apenas de um: install() --> no começo do programa
        # Que ele vai deixar a mensagem, caso tenha algum erro, melhor.

    # Comando inspect()
        # Para usar: inspect(algum_objeto)
        # Vai mostrar as informações sobre o objeto de maneira muito melhor.

# Aula 0? - - - - - - - - - - - - - - - - - - -

# Aula 0? - - - - - - - - - - - - - - - - - - -

# Aula 0? - - - - - - - - - - - - - - - - - - -

# Aula 0? - - - - - - - - - - - - - - - - - - -

# Aula 0? - - - - - - - - - - - - - - - - - - -

# Aula 0? - - - - - - - - - - - - - - - - - - -
