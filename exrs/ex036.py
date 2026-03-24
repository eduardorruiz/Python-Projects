comprador = str(input('Qual é seu nome? '))
print('-=-' * 25)
valor = float(input('Qual o valor da casa: R$'))
print('-=-' * 25)
salario = float(input('Qual é o seu salário: R$'))
print('-=-' * 25)
anos = int(input('Em quantos anos você vai pagar: '))
print('-=-' * 25)
prestaçaomensal = valor / (anos * 12)
porcentagem = salario * 0.3
from time import sleep
print('Analisando seus dados, espere um instante!!')
sleep(1.5)
print('-' * 25)
if prestaçaomensal <= porcentagem:
    print(f'O empréstimo foi \033[1;32mACEITO\033[m, parábens {comprador}.\nAs prestações mensais serão de R${prestaçaomensal:.2f} por {anos} anos.')
else:
    print(f'Caro {comprador}, o empréstimo foi \033[1;31mNEGADO\033[m, tente uma casa mais barata!')