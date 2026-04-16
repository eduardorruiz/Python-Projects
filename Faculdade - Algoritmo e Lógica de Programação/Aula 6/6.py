'''Elaborar um programa que apresente o somatório dos valores pares existentes na faixa entre 1 e N,
onde N é um número digitado pelo usuário e que deve ser no mínimo 100 (obrigatório garantir esse
requisito). '''
soma = cont = 0
n = int(input('Digite o número que terminará o somatório: '))
if n >= 100: # se quisesse que o código não terminasse com um numero menor de 100, usar um while > 100
    while soma <= n:
        soma += cont
        cont += 2
    print(f'O somatório dos valores pares entre 1 e {n} é igual a {cont}')
else:
    print('ERRO, ESCREVA UM NÙMERO MAIOR QUE 100!')
    