""" Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui."""

from Módulos import moeda
num = float(input('Digite o preço: '))
txaum = int(input('Digite a taxa de aumento: '))
txdim = int(input('Digite a taxa de diminuição: '))
moeda.resumo(num, txaum, txdim)