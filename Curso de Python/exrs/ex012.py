price = float(input('Qual é o preço inicial do produto? '))
discount = price * 5 / 100
promotion = price - discount
print(f'Seu produto com 5% de desconto fica de R${price} por R${promotion}.\nVocê está economizando um total de R${discount}.')