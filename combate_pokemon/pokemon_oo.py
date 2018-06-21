class Pokemon:
    vida_base = 0
    ataques = {"Nada": 0}
    poder = 0

    def __init__(self):
        self.vida = self.vida_base

    def elegir_ataque(self, damage):
        self.poder = damage

    def atacar(self, enemigo):
        enemigo.recibir_danio(self.poder)

    def recibir_danio(self, danio):
        self.vida -= danio


class Chizpazo:
    name = "Chizpazo"
    dmg = 15
    type = "Electric"


class Bola_Voltio:
    name = "Bola Voltio"
    dmg = 18
    type = "Electric"

class Araniozo:
    name = "Arañazo"
    dmg = 8
    type = "Normal"

class Ascuas:
    name = "Ascuas"
    dmg = 15
    type = "Fire"

class Placaje:
    name = "Placaje"
    dmg = 7
    type = "Normal"

class Latigo_Cepa:
    name = "Latigo Cepa"
    dmg = 17
    type = "Grass"

class Pistola_Agua:
    name = "Pistola Agua"
    dmg = 13
    type = "Water"


class Pikachu(Pokemon):
    vida_base = 100
    ataques = [Bola_Voltio, Chizpazo]
    bola = 18
    name = "Pikachu"


class Charmander(Pokemon):
    ataques = [Araniozo, Ascuas]
    vida_base = 80
    name = "Charmander"


class Bulbasur(Pokemon):
    ataques = [Latigo_Cepa, Placaje]
    vida_base = 100
    name = "Bulbasur"


class Squirtle(Pokemon):
    ataques = [Pistola_Agua, Placaje]
    vida_base = 90
    name = "Squirtle"


