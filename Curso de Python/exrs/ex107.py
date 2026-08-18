""" Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções
incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também
um programa que importe esse módulo e use algumas dessas funções."""

from Módulos import moeda
num = float(input('Digite o preço: '))
aum = moeda.aumentar(num, 10) # Esse parametro 10 signiifica que está aumentando 10%
dim = moeda.diminuir(num, 10) # Esse parametro 10 signiifica que está diminuindo 10%
dob = moeda.dobro(num)
met = moeda.metade(num)
print(f'Aumentando 10%, temos R${aum}.')
print(f'Diminuindo 10%, temos R${dim}.')
print(f'O dobro de {num} é R${dob}.')
print(f'A metade de {num} é R${met}.')
