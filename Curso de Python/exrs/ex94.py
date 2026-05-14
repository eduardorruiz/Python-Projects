""" Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas  |  B) A média de idade
C) Uma lista com as mulheres  |  D) Uma lista de pessoas com idade acima da média"""
# INICIANDO O PROGRAMA...
from time import sleep
dados = dict()
lista = list()
mulheres = list()
acima_da_média = list()
cadastros = soma = 0
continuar = 'S'
# CRIANDO O LOOP PARA PERGUNTAS ILIMITADAS
while continuar == 'S':
    nome = str(input('Nome: ')).capitalize().strip() # PERGUNTANDO O NOME
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0] #PERGUNTANDO O SEXO
    while sexo not in 'MF':                              # se não responder M ou F, abre a possibilidade de outra resposta
        print('- - ' * 10)
        print('ERRO, porfavor digite apenas M ou F')
        sexo = str(input('Digite o sexo novamente [M/F]: ')).strip().upper()[0]
    idade = int(input('Idade: ')) # PERGUNTANDO A IDADE
    while idade not in range(0, 150): # limitando para não houver erros grotescos
        print('- - ' * 10)
        print('ERRO, porfavor digite uma idade válida')
        idade = int(input('Digite a idade novamente: '))
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0] # PERGUNTANDO SE DESEJA CONTINUAR
    while continuar not in 'SN':                                          # se não responder S ou N, abre a possibilidade de outra resposta
        print('- - ' * 10)
        print('ERRO, porfavor digite apenas S ou N')
        continuar = str(input('Novamente, deseja continuar [S/N]: ')).strip().upper()[0]
    # TERMINOU AS PERGUNTAS, AGORA ANALISAR E TRATAR OS DADOS:
    if sexo == 'F': # Adicionando as mulheres na lista mulheres
        mulheres.append(nome)
    # Adicionando as informações no dicionário dados:
    dados['nome'] = nome
    dados['sexo'] = sexo
    dados['idade'] = idade
    # Adicionando os dicionários na lista:
    lista.append(dados.copy())
    # Somando o número de cadastros e criando a somatória total das idades:
    cadastros += 1
    soma += idade
    print('-=-=' * 10)
media = soma / cadastros # Calculando a média das idades
# Analisando as pessoas acima da média de idade:
for c in range(0, cadastros):
    if lista[c]['idade'] > media:
        acima_da_média.append(lista[c].copy())
# Mostrando os resultados:
print('RESULTADOS ANALISADOS...')
print('-*-*' * 6)
sleep(1.5)
print()
print(f'A) Ao todo temos {cadastros} pessoas cadastradas.')
print("- - " * 10)
print(f'B) A média de idade é de {media:.1f} anos.')
print("- - " * 10)
print(f'C) As mulheres cadastradas foram: {mulheres} ') #, end='')
if len(mulheres) == 0:
    print('  - Não tiveram mulheres cadastradas.')
print("- - " * 10)
print(f'D) Lista de pessoas que estão acima da média: ')
for c in acima_da_média:
    print(f'  {c}')
print("- - " * 10)
print('Encerrando...')
sleep(2)
print(f'\n- FIM DO PROGRAMA -')
