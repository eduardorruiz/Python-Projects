"""Faça um programa que permaneça em laço lendo números inteiros positivos. O laço termina quando for digitado zero
ou negativo. Para cada inteiro lido mostre na tela seu valor convertido para binário. A exibição deve sempre usar uma
quantidade de bits Q que seja do tipo N
N onde N é um número inteiro começando em 1 (ou seja, Q será 8, 16, 32, 64,
128, etc). O programa deve determinar o valor de Q de modo a acomodar os bits necessários para representar o valor
fornecido.
Atenção: não é permitido nenhum recurso automático de Python que converta números inteiros para binário.
A exibição deve ser realizada conforme os exemplos a seguir, colocando um espaço em branco a cada bloco de 4 bits
exibidos (facilita a leitura do conjunto) e entre parênteses ao final a quantidade de bits necessários.
Exemplos
37      0010 0101 (necessários 8 bits)
238     1110 1110 (necessários 8 bits)
256     0000 0000 1000 0000 (necessários 16 bits)
1297    0000 0101 0001 0001 (necessários 16 bits)
70000   0000 0000 0000 0000 0001 0001 0111 0000 (necessários 32 bits) """
num = i = 1
lista = ()
while num > 0:
    num = int(input('Digite um número inteiro positivo: '))
    while num > 2**i:
        i += 1
        print(f'{num} não cabe em [{2**i}] --> 0')
        while num > 2 ** (i - 1) and i > 0:
            i -= 1
            print(f'{num} cabe em [{2 ** i}] --> 1')
            num = num - (num - 2 ** (i - 1))
            int(num)





print('- ' * 18)
