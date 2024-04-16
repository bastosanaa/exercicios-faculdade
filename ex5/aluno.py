from usuarioBU import UsuarioBU
from abc import ABC, abstractmethod 

class Aluno(UsuarioBU, ABC):
    @abstractmethod
    def __init__(self,matricula:int, cpf: int, dias_de_emprestimo: int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula:int):
        if isinstance(matricula,int):
            self.__matricula = matricula
