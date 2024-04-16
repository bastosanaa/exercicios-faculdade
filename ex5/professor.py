from funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, departamento: int, cpf: int):
        super().__init__(departamento, cpf)
        self.__dias_de_emprestimo = 20


    def devolver(self, titulo_livro: str):
        return super().devolver(titulo_livro)