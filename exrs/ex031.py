cidade = input('Para onde será sua viagem? ').strip().capitalize()
print(f'UAU {cidade}, espero que sua viagem seja incrível!')
dist = float(input('Qual é a distância da sua viagem, em Km? '))
if dist <= 200:
    preco = dist * 0.5
    print(f'A sua passagem ficou {preco} reais.')
else:
    print('Estamos com promoção e passagens a mais de 200 Km, estão com desconto, aproveite!!')
    promocao = dist * 0.4
    desconto = dist * 0,5 - dist * 0,4
    print('Calculando desconto...')
    from time import sleep
    sleep(1.2)
    print(f'A sua passagem ficou R${promocao} e teve um desconto de R${desconto}.')
print('Tenha uma ótima viagem!')
