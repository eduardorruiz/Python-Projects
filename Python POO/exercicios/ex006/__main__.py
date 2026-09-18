from rich import inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno("Eduardo", 18, "ADS", "2S")
    a1.fazer_matricula()
    a1.fazer_aniversario()
    inspect(a1)

    p1 = Professor("Gustavo", 37, "Tecnologia", "Mestrado")
    p1.fazer_aniversario()
    p1.dar_aula()
    inspect(p1)

    f1 = Funcionario("Emileide", 29, "Representante Administrativa", "T.I")
    f1.bater_ponto()

if __name__ == "__main__":
    main()