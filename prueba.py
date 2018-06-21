import random

class Pokemon:
    vida_base = 0
    ataques = {"Nada": 0}
    poder = 0

    def __init__(self):
        self.vida = self.vida_base

    def elegir_ataque(self, posicion):
        self.poder = self.ataques[posicion]

    def atacar(self, enemigo):
        enemigo.recibir_danio(self.poder)

    def recibir_danio(self, danio):
        self.vida -= danio


class Pikachu(Pokemon):
    vida_base = 100
    ataques = {"Chizpazo": 15, "Bola voltio": 18}
    bola = 18
    nombre = "Picachu"


class Charmander(Pokemon):
    ataques = {"Arañazo": 8, "Ascuas": 15}
    vida_base = 80
    nombre = "Charmander"


class Bulbasur(Pokemon):
    ataques = {"Placaje": 7, "Latigo Cepa": 17}
    vida_base = 100
    nombre = "Bulbasur"


class Squirtle(Pokemon):
    ataques = {"Placaje": 7, "Pistola Agua": 13}
    vida_base = 90
    nombre = "Squirtle"

mi_picachu = Pikachu()

for ataque in mi_picachu.ataques:
    print(ataque)
habilidad_enemiga, poder = random.choice(list(pokemon_enemigo.items()))
print(habilidad_enemiga)
print(poder)
