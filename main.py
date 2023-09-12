from circulo import Circulo
from quadrado import Quadrado
from triangulo import Triangulo

figuras = []

um_circulo= Circulo('circulo da silva', 10)
um_quadrado = Quadrado('quadrado da silva', 25)
um_triangulo = Triangulo('triangulo da silva', 5)
# 1 2 3 ... 5 6 7 ...

figuras.append(um_circulo)
figuras.append(um_quadrado)
figuras.append(um_triangulo)
figuras.append('EU SOU UM COMPUTADOR')

#Comportamento Polimórfico
for figura in figuras:
    figura.desenhe()
