from figura import Figura


class Quadrado(Figura):
    def __init__(self, nome , lado):
        super().__init__(nome)
        self.lado = lado

    def desenhe(self) -> str:
        print(super().desenhe(), 'de lado x lado:', str(self.lado * self.lado))