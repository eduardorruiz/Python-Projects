# Estrutura de repetição com variável de controle = for
print('oi')
print('oi')
print('oi')
# È Igual a for ... (c, por exemplo) in range(0-->3):
print('OU com estrutura de repetição')
for c in range(0, 3):
    print('Oi')
print('Fim')
# se no lugar do 'oi' colocar o nome dado para o for, nesse caso c ele cria uma contagem
for c in range(0,4):
    print(c)
# se dentro do range pra contar pra trás é so colocar(0, 4, -1) a terceira casa da virgula diz oque é pra fazer
# então pra fazer uma contagem regresiva de 10 a 1 por exemplo ficaria (10, 0, -1)
# Ou seja, se colocar (0,11, 2) vai aparacer o 0,2,4,6,8 e 10.
# criando uma contagem
print('Contagem')
n = int(input('Digite um número: '))
for c in range (0, n+1):
    print(c)
# para somar tudo por exemplo
print('Somatoria')
s = 0
for c in range(0,3):
    n = int(input('Digite um numero: '))
    s += n #Ou s = s + n
print(f'O somatorio foi de {s}')
