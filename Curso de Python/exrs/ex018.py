import math
ang = float(input(' Digite o ângulo que você gostaria de saber o sen, cos e tg: '))
sen = math.sin(math.radians(ang))
print(f'O seno de {ang} é = {sen:.2f}.')
cos = math.cos(math.radians(ang))
print(f'O cosseno de {ang} é = {cos:.2f}.')
tg = math.tan(math.radians(ang))
print(f'A tangente de {ang} é = {tg:.2f}')
