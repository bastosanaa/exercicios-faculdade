from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        if isinstance(personagem, Personagem):
            self.__personagem = personagem

    def valor_total_carta(self) -> int:
        valor_carta = 0
        valor_carta += self.__personagem.energia
        valor_carta += self.__personagem.habilidade
        valor_carta += self.__personagem.velocidade
        valor_carta += self.__personagem.resistencia
        return valor_carta

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
