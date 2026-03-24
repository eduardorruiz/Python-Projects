print('{:-^30}'.format(' LOJA DO DUDZ '))
preço = float(input('Qual é o preço do produto: R$'))
print('Formas de Pagamento')
print('[ 1 ] à vista no dinheiro')
print('[ 2 ] no Débito')
print('[ 3 ] no Crédito')
pagamento = int(input('Qual será a forma de pagamento: '))
if pagamento == 1:
    desconto = preço - (preço * 0.1)
    print(f'O valor a ser pago é de R${desconto}.')
elif pagamento == 2:
    print(f'O valor a ser pago é de R${preço}')
elif pagamento == 3:
    print('Em até 3x sem JUROS!')
    parcelas = int(input('Em quantas parcelas: '))
    precoparcelado = preço / parcelas
    if parcelas == 1:
        print(f'O valor total a ser pago é de R${preço}.')
    elif parcelas <= 3:
        print(f'O valor total a ser pago é de R${preço}, em {parcelas} vezes de R${precoparcelado}.')
    else:
        precoparceladocomjuros = (preço + (preço * 0.2)) / parcelas
        print(f'O valor total a ser pago é de R${preço}, em {parcelas} vezes de R${precoparceladocomjuros}.')
else:
    print('-=-' * 15)
    print('\033[1mOPÇÃO DE PAGAMENTO INVÁLIDA\033[m, tente novamente!')
    print('-=-' * 15)