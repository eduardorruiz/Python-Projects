lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') # Pode sem parenteses também
# Tuplas são IMUTÁVEIS!
# Fatiamento
print(lanche[1]) # mostra o suco.
print(lanche[1:3]) # mostra do elemento 1 ao 3, eliminando o 3, logo mostra: suco e pizza
print(lanche[:2]) #mostra do ínicio até o elemento 2, eliminando o 2 , logo: Hambúrguer e Suco
print(lanche[-2]) #mostra ao contrário, ou seja, -1 = Pudim, -2 = Pizza, -3 = Suco, -4 = Hambúrguer
print(lanche[-2:]) #mostra do -2(Pizza) até o final, normalmento, logo: Pizza e Pudim

# Nesses fatiamentos aparece feio --> ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Para aparecer sem as () e sem as aspas, use estrutura de repetição:
for comida in lanche: #Não tem como mostrar a posição.
    print(comida)
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print(len(lanche)) # Conta os elementos da Tupla, no caso 4

# Outro modo de usar o for, com o len
for cont in range(0, len(lanche)): # tem como mostrar a posição
    print(comida) # Mostra do 0 a 4
    print(f'Eu vou comer {lanche[cont]}') # Mostra que nem o primeiro for, só que usando o range.
    #print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

# Outro modo
for posição, comida in enumerate(lanche): #Mostra a posição também
    print(f'Eu vou comer {comida} na posição {posição}')

print(sorted(lanche)) # mostra uma lista organizada em ordem

a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(a) #mostra (1, 2, 3)
print(b) #mostra (4, 5, 6)
print(c) #mostra as duas em conjunto, logo: (1, 2, 3, 4, 5, 6)
d = b + a
print(d) #mostra (4, 5, 6, 1, 2, 3)
print(c.count(5)) # isso é: quantas vezes está aparecendo 5 em c, no caso 1.
print(c.index(5)) # isso é: em qual posição está o 5, no caso 4.
# se tivesse dois 5, e um deles estivesse depois do primeiro, poderia usar
# print(c.index(5, 4)) esse 4 é a partir dessa posição.

pessoa = ('Eduardo', 39, 'M', 62.5)
print(pessoa) # escreve sem problemas, pode misturar.
del(pessoa) # posso deletar da memória, é imutavel, menos para apagar.
# Não posso deletar um elemento especifico em uma tupla, só ela inteira.

