""" Faça um programa para o cálculo de uma folha de pagamento de um país fictício. A base de cálculo sempre é o Salário
Bruto e sabe-se que há três contribuições a serem calculadas: Imposto de Renda (regra descrita a seguir), 3% para o
Sindicato e 11% para o Fundo do Trabalhador. Os valores de IR e Sindicato são descontados do empregado. O valor
do Fundo do Trabalhador não é descontado do empregado, pois é a empresa que deposita. O Salário Líquido
corresponde ao Salário Bruto menos os descontos do empregado. O programa deverá ler o Salário Bruto do mês e
mostrar os resultados conforme o modelo de saída abaixo.
Regras para o Desconto do Imposto de Renda:
a. Salário Bruto até 900 (inclusive) - isento
b. Salário Bruto até 1500 (inclusive) - desconto de 5%
c. Salário Bruto até 2500 (inclusive) - desconto de 10%
d. Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade
de hora é 220.
Salário Bruto: : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS ( 10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00 """

salario = float(input('Digite o salário Bruto mensal: R$'))
cinco = salario * 5 / 100
dez = salario * 10 / 100
vinte = salario * 20 / 100
fgts = salario * 11 / 100
if salario < 901:
    salario = salario
elif 900 < salario < 1501:
    salario = salario - cinco
elif 1500 < salario < 2501:
    salario = salario - dez
else:
    salario = salario - vinte


print(ir)
print(inss)
print(fgts)