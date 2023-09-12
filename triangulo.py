from figura import Figura


class Triangulo(Figura):
    def __init__(self, nome, base):
        super().__init__(nome)
        self.base = base

    def desenhe(self):
        print(super().desenhe(), 'de base:', str(self.base))