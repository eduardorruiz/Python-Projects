""" O Sr. Joaquim Manoel possui uma grande loja de artigos que vende todos os produtos pelo mesmo preço
(antigamente era R$ 1,99). Nesta loja há 10 caixas para pagamento. Para agilizar o cálculo de quanto cada cliente deve
pagar ele desenvolveu uma tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta.
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de
preços. Você foi contratado para desenvolver o programa que lê um número real de entrada que é o preço unitário
dos produtos e monta esta tabela de preços, que conterá os preços de 1 até 50 produtos. A saída deverá ter a
aparência conforme o exemplo abaixo.
Lojas J.M. – Tabela de Valores a Pagar
Valor unitário do produto: 1,99
Qtde deve Pagar
 1        1,99
 2        3,98
 3        5,97
...
 49       97,51
 50       99,50"""
print('- Lojas J.M. – Tabela de Valores a Pagar -')
preço_un = float(input('Digite o preço unitário dos produtos: '))
print('-*-' * 14)
print(f'Lojas J.M. – Tabela de Valores a Pagar'
      f'\n- - - - - - - - - - - - - - - - - - - -'
      f'\nValor unitário do produto: R${preço_un}'
      f'\n- - - - - - - - - - - - - - - - - - - -'
      f'\nQtde deve Pagar'
      f'\n- - - - - - - -')
for c in range(1, 51):
    resul = c * preço_un
    if c < 10:
        print(f'0{c}   -->   {resul:.2f}')
    else:
        print(f'{c}   -->   {resul:.2f}')
print('- - - - - - - -')
print('-*-' * 10)
