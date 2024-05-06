from AbstractControladorJogo import *
from Personagem import Personagem
from AbstractPersonagem import Tipo
from Carta import Carta
from Mesa import Mesa


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__personagems = []
        self.__baralho = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagems

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        personagem = Personagem(energia,
                                habilidade,
                                velocidade,
                                resistencia,
                                tipo)
        self.__personagems.append(personagem)
        return personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        if isinstance(personagem, Personagem):
            carta = Carta(personagem)
            self.__baralho.append(carta)
            return carta
        return None

    def jogada(self, mesa: Mesa) -> Jogador:
        if isinstance(mesa, Mesa):
            valor_carta_j1 = mesa.carta_jogador1.valor_total_carta()
            valor_carta_j2 = mesa.carta_jogador2.valor_total_carta()
            if valor_carta_j1 != valor_carta_j2:
                if valor_carta_j1 > valor_carta_j2:
                    mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador2)
                    mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
                    if mesa.jogador2.mao == []:
                        return mesa.jogador1
                else:
                    mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador1)
                    mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
                    if mesa.jogador1.mao == []:
                        return mesa.jogador2
            else:
                mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
                mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
                return None
