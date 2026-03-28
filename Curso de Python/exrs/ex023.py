number = int(input(' Digite o número que devo analisar: '))
print(f'Analisando o número {number} sua unidade, dezena, centena e milhar são respectivamente...')
uni = number//1 % 10
dzn = number//10 % 10
cntn = number//100 % 10
mlhr = number//1000 % 10
print(f'unidade: {uni}')
print(f'dezena: {dzn}')
print(f'centena: {cntn}')
print(f'milhar: {mlhr}')
