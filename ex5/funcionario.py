from usuario_bu import UsuarioBU
from abc import ABC, abstractmethod 

class Funcionario(UsuarioBU, ABC):
    @abstractmethod
    def __init__(self,departamento:str, cpf: int, dias_de_emprestimo: int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento:int):
        if isinstance(departamento,int):
            self.__departamento = departamento

    def emprestar(self, titulo_livro:str):
        return f'do departamento "{self.departamento}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'

    def devolver(self, titulo_livro:str):
        return f'Funcionario do departamento "{self.departamento}" devolveu o livro: {titulo_livro}'
