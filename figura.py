from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def __init__(self, nome: str):
        self.nome = nome

    @abstractmethod
    def desenhe(self) -> str: #documentação
        return 'Desenhando - ' + self.nome
