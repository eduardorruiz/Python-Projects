print('-=-'*25)
print('Olá, este programa irá avaliar três números e dizer qual é o maior e o menor número.')
print('-=-'*25)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
from time import sleep
print(f'Ótimo, entre os números {n1}, {n2} e {n3} o menor é ...')
sleep(1.3)
#Verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O número {menor} é o menor.')
print(f'E o maior número é ...')
#Verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
sleep(1)
print(f'O número {maior} é o maior.')
print('Até mais a proxima!')