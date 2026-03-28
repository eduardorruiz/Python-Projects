"""  Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

dezoito = homens = mulheresvinte = 0
while True:
    print(' - - CADASTRE UMA PESSOA - - ')
    print('-*' * 10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        dezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresvinte += 1
    print('-*' * 10)
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar?[S/N]:')).strip().upper()[0]
    if stop == 'N':
        break
print('~' * 42)
print(' Fim do Programa, seguem os dados analisados...')
print('~' * 42)
print(f'Foram cadastradas {dezoito} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulheresvinte} mulheres com menos de 20 anos.')