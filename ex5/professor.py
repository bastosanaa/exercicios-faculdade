from funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, departamento: int, cpf: int):
        super().__init__(departamento, cpf,dias_de_emprestimo=20)

    def emprestar(self, titulo_livro: str):
        return f'Professor do departamento "{self.departamento}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'
    
    def devolver(self, titulo_livro: str):
        return f'Professor do departamento "{self.departamento}" devolveu o livro: {titulo_livro}'
    
