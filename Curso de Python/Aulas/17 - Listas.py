    lista = ['Corinthians', 'Palmeiras', 'Santos', 'São Paulo']

lista.append('Portuguesa') #.append adiciona no final da lista, ent Portuguesa ficou na quarta posição
lista.insert(0, 'Brasil')#.insert abre um espaço na numeração escolhida e adiciona algo lá

del lista[1] #excluiria o palmeiras na lista
lista.pop(1) #geramente usado para eliminar o último elemento (.pop()), mas pode eliminar outros também
lista.remove('Portuguesa') # Invés de usar pela posição, elimina pelo conteúdo
# Se tentar excluir um conteúdo que não existe na lista, vai dar erro, portanto podemos fazer assim:
if 'Flamengo' in lista:
    lista.remove('Flamengo')

# OUTRO MODO DE DECLARAR LISTA:
valores = list(range(1, 11)) # cria uma lista de contagem de 1 a 10

# Organizar lista
numeros = [2, 1, 4, 5, 3]
numeros.sort() # Deixaria os números em ordem crescente
numeros.sort(reverse=True) # Deixaria em ordem decrescente

len(numeros) # Mostra quantos elementos tem na lista numeros

# CRIAR LISTA VAZIA
vazia = []
vazia2 = list()

#MOSTRAR BONITO
for valor in valores: # Para cada valor em valores...
    print(f'{valor}... ', end='')

# pra criar mostrando a posição
for posição, valor in enumerate(valores):
    print(f'Na posição {posição}̣ encontrei o valor {valor}')

#Pra adicionar valores na lista
vazia.append(int(input('Digite algo pra lista não ficar vazia: ')))

# Cópia de uma lista
a = [1, 2, 3]
b = a
b[0] = 10
# na lista a e na lista b o primeiro elemento sera dez, no python quando se iguala uma lista elas se conectam
c = a[:] # ASSIM criou uma cópia!!!
