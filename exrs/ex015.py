km = float(input('Quantos Km você percorreu com o carro? '))
dias = int(input('E quantos dias o carro foi alugado? '))
preço = (60*dias) + (0.15*km)
print(f'O total a pagar, visto que você rodou {km} quilômetros, em {dias} dias foi de: R${preço}.')