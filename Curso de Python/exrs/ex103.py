""" Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois
parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz
 de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""

def ficha(nome='<desconhecido>',gols=0):
    nome = str(input('Digite o nome do jogador: ')).strip()
    gols = str(input(f'Digite quantos gols {nome} fez no campeonato: ')).strip()
    if gols.isnumeric(): #gols com str permite não colocar nada.
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
ficha()