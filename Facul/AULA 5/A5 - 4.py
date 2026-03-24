print('Soma de N inteiros com N reais')
n = 10
n1 = 10
somaint = 0
somareais = 0

while n != 0:
    n = int(input('Digite um número inteiro, digite [0] para parar: '))
    if n > 0:
        somaint += n
print('- - ' * 7)
while n1 != 0:
    n1 = float(input('Digite um número real, digite [0] para parar: '))
    if n1 > 0:
        somareais += n1
somatotal = somaint + somareais
print(somatotal)