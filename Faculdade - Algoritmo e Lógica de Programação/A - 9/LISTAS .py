# Exemplo de acesso a elementos de uma lista
Dados = [17, 8, 12, 25, 4, 16]

print('Exibir cada elemento na tela, usando while')
i = 0 # índice
while i <= 5:#len(Dados):
    print(Dados[i])
    i += 1
print('Exibir cada elemento na tela, usando for')
for valor in Dados:
    print(valor)
# sempre que puder usar o for --> USE ( + otimizado que o while )
print('\nIteração\n')
while i <= 5:# Usar o len(Dados) torna o programa muito mais esperto
    Dados[i] = Dados[i] * 2 # Multiplica a lista por 2 ( tbm pode ser Dados[i] *= 2 ))
    i += 1

for valor in Dados: # Vai dar errado
    valor *= 2
    print(Dados) # Daria errado pq printei o Dados
# Se a manipulação que preciso fazer, precisa alterar o elemento da lista --> não da pra usar o FOR

Dados = Dados * 2 # Duplica a lista

print(' - Range - ')
range(6) # range(0, 6) o 6 não está incluido
list(range(6))  # Cria uma lista do 0 até o 5
list(range(2 , 6)) # Começa do 2 e para no 5
list(range(2, 6, 2)) # Comecça no 2 e para no 5, pulando de 2 em 2

for i in range(len(Dados)): # Deste modo, vai dar certo.
    Dados[i] *= 2
    print(Dados)


# - ADICIONAR NA LISTA
L = [1, 2, 3, 4, 5]
L.append(5) # adiciona um cinco no final da lista

L.insert(1, 5) # Adicionou na posição 1, o número 5

L.insert(21230120, 1) # Vai adicionar o número 1, no último elemento, pq a lista é menor que o index)

# - REMOVER DA LISTA
# 1. DEL
L = [1, 2, 3 , 4, 5]
del L[0] # excluiu o primeiro elemento

del L[len(L) -1] # exclui o último

# de excluir o último com esse len(L) veio o negativo, portanto:
del L[-1] # Também exclui o último --> subentende que tem um len(L) antes do -1

# 2. REMOVE - espera que você coloque oque você quer remover
L.remove(0) # Exlui o indicado, remove o elemento indicado
L.remove(43) # ERRO, pq não tem 43 na lista
# Se tiver três 8 na lista

L2 = [1, 8, 2, 8, 3, 8]
L2.remove(8) # vai excluir só o primeiro
# Pra excluir todos
# ERRADO
L2.count(8)
posição = L2.index(8)
posição = L2.index(8, posição + 1) # Erro quando passar do último 8 da lista
# CERTO
lugares = [] # Criar uma lista para adicionar onde estão os 8 na lista
contador = L2.count(8)  # Conta quantos 8 tem na lista L2
posição = -1
for i in range(contador): # O laço vai repetir quantas vezes apareceu o 8 na lista
    posição = L.index(8, posição + 1) # Mostra onde está o elemento 8, a partir da posição 0 e quando repetir, a partir da posição 1 e assim em diante...
    lugares.append(posição) # Adiciona as posições onde foram encontrados os elementos 8 em L2, na lista LUGARES
print(lugares) # mostraria 1, 3, 5

# 3. POP
L.pop() # Exclui do final
lixeira = L.pop

# - INDEX
L.index(8) # mostra onde está o elemento 8 na lista
L.index(8, 4) # mostra onde está o elemento 8, a partir da posição 4

# - COUNT
L.count(10) # Verifica quantos elementos '10' existem na lista L

# - - - ACHAR TODOS OS ELEMENTOS IGUAIS NA LISTA - - -
# vamos supor que quero achar todos os 8 em L2
L2 = [1, 8, 2, 8, 3, 8]
lugares = [] # Criar uma lista para adicionar onde estão os 8 na lista
contador = L2.count(8)  # Conta quantos 8 tem na lista L2
posição = -1
for i in range(contador): # O laço vai repetir quantas vezes apareceu o 8 na lista --> obs: o i não ta sendo usado pra nada entao pode ser substituído por '_'
    posição = L.index(8, posição + 1) # Mostra onde está o elemento 8, a partir da posição 0 e quando repetir, a partir da posição 1 e assim em diante...
    lugares.append(posição) # Adiciona as posições onde foram encontrados os elementos 8 em L2, na lista LUGARES
print(lugares) # mostraria 1, 3, 5




