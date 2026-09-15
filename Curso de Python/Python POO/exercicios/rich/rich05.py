from rich.traceback import install
install() # monitora, caso tenha algum erro, fica muito + visual.

def divisao(x, y):
    return x / y

print(divisao(500, 0))