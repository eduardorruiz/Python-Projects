""" Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as seguintes informações:
Quantidade de notas, A maior nota, A menor nota, A média da turma, A situação"""

def notas(*n, sit=False):
    """ --> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos.
    :param sit: valor opicional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma."""
    notas = {}
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['média'] = sum(n)/len(n)
    if sit == True:
        if notas['média'] >= 7:
            notas['situação'] = 'BOA'
        elif notas['média'] >= 5:
            notas['situação'] = 'RAZOÁVEL'
        else:
            notas['situação'] = 'RUIM'
    return notas
#Prog Principal
resp = notas(6, 8, 10, sit = True)
help(notas)
print(resp)