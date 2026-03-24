import math
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
# OU hipotenusa = math.sqrt(oposto** 2 + adjacente** 2)
hi = math.hypot(oposto,adjacente)
print(f'A hipotenusa vai medir {hi:.2f}')

