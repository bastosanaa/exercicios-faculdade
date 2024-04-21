from aluno import Aluno

class AlunoPosGraduacao(Aluno):
    def __init__(self, matricula: int, cpf: int, dias_de_emprestimo: int):
        super().__init__(matricula, cpf, dias_de_emprestimo)
        self.__elaborando_tese = bool
        if self.__elaborando_tese:
            self.dias_de_emprestimo *= 2

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese
    
    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese:bool):
        self.__elaborando_tese = elaborando_tese

    def emprestar(self, titulo_livro: str):
        return super().emprestar(titulo_livro)
    
    def devolver(self, titulo_livro: str):
        return super().devolver(titulo_livro)
    

    
