from abc import ABC, abstractmethod 
from usuario_bu import UsuarioBU

class Aluno(UsuarioBU, ABC):
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int,matricula:int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula = str(matricula)

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula:int):
        if isinstance(matricula,int):
            self.__matricula = matricula

    def emprestar(self, titulo_livro:str):
        return f'Aluno de matricula "{self.matricula}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'

    def devolver(self, titulo_livro:str):
        return f'Aluno de matricula "{self.matricula}" devolveu o livro: {titulo_livro}'