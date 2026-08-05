""" Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""

def fatorial(n, show=False):
    """--> Calcula o Fatorial de um número.
     :parametro n: O número a ser calculado.
     :parametro show(opicional): Mostrar ou não a conta.
     :return: O valor do fatorial de um número n."""
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =', end=' ')
        f *= c
    return f
print(fatorial(6))
print(fatorial(5, show=True))
help(fatorial)

# Fazer com while dps