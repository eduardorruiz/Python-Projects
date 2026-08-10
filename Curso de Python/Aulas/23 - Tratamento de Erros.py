try: # Aqui colocamos a operação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except: # Caso de erro, aparece isso, e não aquele erro em vermelho
    print('Infelizmente tivemos um problema')
else: # Se der certo ocorre isso
    print(f'O resultado é {r}')
finally: # Isso acontece sempre, dando erro ou dando certo
    print('Volte sempre, muito obrigado!')

"""Outro tipo de usar o except"""
try:
    z = 10
    y = 'um'
    w = z / y
except Exception as erro: # Criei a variavel erro, e agora posso usá-la.
    print(f'Ocorreu um erro na entrada {erro.__class__}')

""" Normalmente cada except precisa ter seu erro acompanhado, ex: """
try:
    d = a / 0
except ZeroDivisionError:
    print('Não existe divisão por zero.')
# Posso colocar entre () se tiver mais de um erro
# except (ValueError, ZeroDivisionError):