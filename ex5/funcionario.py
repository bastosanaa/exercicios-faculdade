from usuarioBU import UsuarioBU
from abc import ABC, abstractmethod 

class Funcionario(UsuarioBU, ABC):
    @abstractmethod
    def __init__(self,departamento:int, cpf: int, dias_de_emprestimo: int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento:int):
        if isinstance(departamento,int):
            self.__departamento = departamento

    def emprestar(self, titulo_liro:str):
        pass

    def devolver(self, titulo_livro:str):
        pass
