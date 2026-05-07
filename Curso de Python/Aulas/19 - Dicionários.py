# EX de DICIONÁRIOS --> 90 a 95
# Dicionários = Estruturas de dados com índices literais
dicionário = dict()
dados = {} # Declarar dados
dados = {'nome':'Eduardo', 'idade':18} # Colocar os dados em dados
dados['sexo'] = 'Masculino' # Adicionar mais um elemento em dados.
print(f'O {dados["nome"]} tem {dados["idade"]} anos.') # Utiliza-se aspas duplas para não dar erro
dados['nome'] = 'Dudu' # alterou o nome EDUARDO p/ DUDU
del dados['idade'] # Excluir o elemento idade do dicionário.
print(dados.values()) # Mostra oq tem dentro do elemento --> [Eduardo, 18 , Masculino]
print(dados.keys()) # Mostra o nome do elemento --> [nome, idade, sexo]
print(dados.items()) # Mostra tanto os values, quanto os keys --> [Nome, Eduardo][Idade, 18][...]
for k, v in dados.items(): # Para cada chave(keys[k]) e valor(values[v]) em dados
    print(f'O {k} é {v}') # [O nome é Eduardo][O sexo é Masculino]

# É possível juntar TUPlAS, LISTAS e DICIONÁRIOS:

pessoas = list() # pessoas é uma lista
pessoas.append(dados) # adicionei o meu dicionário de dados dentro da lista pessoas
print(pessoas) # Mostra que no elemento 0 da lista pessoas, temos o nome: Eduardo, o sexo: Masculino
print(pessoas[0]['nome']) # Mostra EDUARDO, que é dentro do dicionário dados no elemento 1 da lista pessoas o nome

print(' --- ' * 10) #  CRIANDO LISTAS E DICIONARIOS

brasil = []
estado1 = {'nome' : 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'nome': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1) # mostra {'nome': 'Rio de Janeiro', 'sigla': 'RJ'}
print(estado1['sigla']) # mostra apenas RJ
print(brasil) # Mostra [{'nome' : 'Rio de Janeiro', 'sigla': 'RJ'}, {'nome': 'São Paulo', 'sigla': 'SP']
print(brasil[0]) # É igual a print(estado1)
print(brasil[1]['sigla']) # Mostra apenas SP

# CRIANDO UM PROGRAMINHA
estado = {}
brasil = []
for c in range(0, 2):
    estado['nome'] = str(input('Digite o nome do estado: '))
    estado['sigla'] = str(input('Informe o nome da sigla: '))
    #brasil.append(estado) daria erro pois não estou copiando
    brasil.append(estado.copy()) # copiei as respostas de estado['nome'] e estado['sigla']
# Para mostrar bonito
for estado in brasil: # Esse for é da lista
    for key, value in estado.items(): # Esse for é para o dicionário
        print(f'{key} do estado é {value}')

