""" Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada
moeda() que consiga mostrar os números como um valor monetário formatado. """

from Módulos import moeda
num = float(input('Digite o preço: '))
aum = moeda.aumentar(num, 10) # Esse parametro 10 signiifica que está aumentando 10%
dim = moeda.diminuir(num, 10) # Esse parametro 10 signiifica que está diminuindo 10%
dob = moeda.dobro(num)
met = moeda.metade(num)
print(f'Aumentando 10%, temos R${moeda.moeda(aum)}.')
print(f'Diminuindo 10%, temos R${moeda.moeda(dim)}.')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(dob)}.')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(met)}.')

# A função moeda.moeda() é apenas pra formatar, deixando R$:??,??
