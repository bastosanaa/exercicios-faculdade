from abc import ABC, abstractmethod
from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):

    def __init__(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        self.__mao = []

    @property
    def nome(self) -> str:
        return self.__nome

    def baixa_carta_da_mao(self) -> Carta:
        if len(self.__mao) >= 1:
            numero_aleatorio_carta = random.randint(1, len(self.__mao))
            carta_aleatoria = self.__mao[numero_aleatorio_carta-1]
            self.__mao.remove(carta_aleatoria)
            return carta_aleatoria

    @property
    def mao(self) -> list:
        return self.__mao

    def inclui_carta_na_mao(self, carta:Carta):
        if isinstance(carta, Carta):
            self.__mao.append(carta)
