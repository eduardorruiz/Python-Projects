print('Olá, aqui na empresa estamos promovendo aumento no salário dos nossos trabalhadores.')
salario = float(input('Qual é o valor do seu salário atual: R$'))
if salario < 1250:
    print('Parábens, você ganhou um aumento de 15%.')
    aumento15 = (salario * 0.15) + salario
    print(f'O salário foi de R${salario} para R${aumento15}')
else:
    print('Parábens, você recebeu um aumento de 10%.')
    aumento10 = (salario * 0.1) + salario
    print(f'O salário foi de R${salario} para R${aumento10}')
print('Nossa empresa agradeçe seu esforço e desempenho, Bom Trabalho!')