def aumentar(preço = 0, taxa = 0):
    return preço + (preço * taxa/100)

def diminuir(preço= 0, taxa = 0):
    return preço - (preço * taxa/100)

def dobro(preço= 0):
    return preço * 2

def metade(preço= 0):
    return preço / 2

def formatação(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço= 0, txa = 0, txd = 0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: {formatação(preço)}')
    print(f'Dobro do preço:  {formatação(dobro(preço))}')
    print(f'Metade do preço: {formatação(metade(preço))}')
    print(f'{txa}% de aumento:  {formatação(aumentar(preço, txa))}')
    print(f'{txd}% de redução:  {formatação(diminuir(preço, txd))}')
    print('-'*30)
