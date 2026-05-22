""" Escreva um programa que leia do teclado um número inteiro de 5 dígitos. Em seguida calcule e mostre na tela o dígito
verificador do número lido, o qual é calculado segundo as regras a seguir.
Exemplo de cálculo do DV do Código do Produto para o código 21956:
Dígitos                                      2 1 9  5  6
Pesos                                        6 5 4  3  2
Cada dígito deve ser multiplicado pelo peso 12 5 36 15 12
Some todos os valores acima 12 + 5 + 36 + 15 + 12 = 80
Calcule o resto da somatória por 7 Resto de 80 por 7 = 3
Portanto o DV do código 21956 é 3 e o código completo ficará sendo 21956-3 """
código = input('Digite o código: ')
# Solução 1 - código com str
print(' - SOLUÇÃO 1')
i = soma = 0
peso = 6
while i < len(código):
    valor = (ord(código[i]) - 48) * peso
    soma += valor
    peso -= 1
    i += 1
dv = soma % 7
print(f'  o DV de {código} é {dv}')

#Solução 2 - código com inteiro
# se o código é inteiro fazemos sua decomposição através de decompo
print(' - SOLUÇÃO 2')
códigoauxiliar = int(código)
i = soma = 0
peso = 6
divisor = 10000
while códigoauxiliar > 0:
    valor = códigoauxiliar // divisor # para pegar o valor + significativo
    soma += valor * peso
    códigoauxiliar = códigoauxiliar % divisor
    divisor = divisor // 10
    peso -= 1
dv = soma % 7 # dv = dígito verificador
print(f'  o DV de {código} é {dv}')