from AbstractPersonagem import *


class Personagem(AbstractPersonagem):
    #Construtor fornecido, nao deve ser alterado
    def __init__(self, energia: int, habilidade: int,
                 velocidade: int, resistencia: int, tipo: Tipo):
        if isinstance(energia, int):
            self.__energia = energia
        if isinstance(habilidade,int):
            self.__habilidade = habilidade
        if isinstance(velocidade, int):
            self.__velocidade = velocidade
        if isinstance(resistencia, int):
            self.__resistencia = resistencia
        if isinstance(tipo, Tipo):
            self.__tipo = tipo


    @property
    def tipo(self) -> Tipo:
        pass#implementar

    @property
    def energia(self) -> int:
        pass#implementar

    @property
    def habilidade(self) -> int:
        pass#implementar

    @property
    def velocidade(self) -> int:
        pass#implementar

    @property
    def resistencia(self) -> int:
        pass#implementar
