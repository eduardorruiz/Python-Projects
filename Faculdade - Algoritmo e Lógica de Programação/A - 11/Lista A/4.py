""" Faça um programa que leia do teclado um string que representa um conjunto de dados separados por ponto e vírgula ( ; ).
Os dados contidos em cada linha contém três partes:
• Um primeiro número inteiro de 1 dígito, que chamaremos de categoria (Categ);
• Um segundo número inteiro qualquer, que será a quantidade (Qtde);
• Um número real com duas casas decimais (na verdade isso não é muito relevante), que será o valor (Valor).
Faça um programa que leia todos os dados, carregando-os na forma de sublistas contidas em uma lista. Em cada sublista
inclua o Total que é o resultado da multiplicação de Qtde pelo Valor.
Exiba todos os dados na tela formatados em forma de tabela, sendo uma linha para cada conjunto de dados.
Por fim, some todos os totais obtendo um total geral e mostre-o na tela com duas casas decimais.
1;16;23.55
6;414;2.43
3;319;16.50
1;10;22.62
2;16;25.94
3;1;39.14
O total geral do exemplo acima é 7326,70"""

def processaEntrada():
    linha = input('Digite uma linha: ')
    if linha == '':
        return ''
    linha = linha.split(';')
    linha[0] = int(linha[0])
    linha[1] = int(linha[1])
    linha[2] = float(linha[2])
    linha.append(linha[1] * linha[2])
    return linha

def exibeDados(Dados):
    print('-*' * 10)
    print('Dados Lidos...')
    print('   Categ  Qtde   Pc.unit     Total')
    for dado in Dados:
        print(f'   {dado[0]:3} {dado[1]:7} {dado[2]:8.2f} {dado[3]:10.2f} ')

def CalcTotal(Dados):
    tot = 0
    for dado in Dados:
        tot += dado[3]
    return tot

def CalcTotCateg(Dados):
    d = {}
    for dado in Dados:
        if dado[0] in d:
            d[dado[0]] += dado[3]
        else:
            d[dado[0]] = dado[3]

def exibeTotCateg(TotCateg):
    print('falta copiar')

# Programa Principal
Dados = []
entrada = processaEntrada()
while entrada != '':
    Dados.append(entrada)
    entrada = processaEntrada()

exibeDados(Dados)
total = CalcTotal(Dados)
print(f'Soma de todos os valores = {total:.2f}')

# INCOMPLETO