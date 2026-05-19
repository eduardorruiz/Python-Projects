""" Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno. """

def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno de [{larg}] X [{comp}] é de {area}m².')

#Programa Principal
print('Controle de Terrenos'
      '\n--------------------')
la = float(input('Largura (m): '))
co = float(input('Comprimento (m): '))
area(la, co)