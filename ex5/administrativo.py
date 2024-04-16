from funcionario import Funcionario

class Administrativo(Funcionario):
    def __init__(self, departamento: int, cpf: int):
        super().__init__(departamento, cpf)
        self.__dias_de_emprestimo = 10

        