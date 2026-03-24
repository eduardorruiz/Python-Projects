larg = float(input('Qual é a largura da sua parede?'))
alt = float(input('E qual a altura da sua parede?'))
area = larg * alt
litro = area / 2
print(f'Sua parede tem uma área de {area}m², cada litro de tinta, pinta uma área de 2m², portanto irá precisar de {litro}L de tinta.' )