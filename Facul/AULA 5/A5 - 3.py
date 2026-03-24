print('Soma de N inteiros com N reais')
print('Digite 0 para parar')
n = 10
n1 = 10
somaint = 0
somareais = 0

while n != 0:
    n = int(input('Digite um número inteiro: '))
    somaint += n
print('- - ' * 7)
while n1 != 0:
    n1 = float(input('Digite um número real: '))
    somareais += n1
somatotal = somaint + somareais
print(somatotal)