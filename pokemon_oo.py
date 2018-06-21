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
pokemon_enemigo = None

pokemon_elegido = input("¿Contra que pokemon quieres combaatir?").upper()

while  pokemon_elegido != "bulbasaur".upper() and pokemon_elegido != "squirtle".upper() and pokemon_elegido != "charmander".upper():
    pokemon_elegido = input("¿Contra que pokemon quieres combaatir?").upper()

if pokemon_elegido == "bulbasaur".upper():
    pokemon_enemigo = Bulbasur()
elif pokemon_elegido == "squirtle".upper():
    pokemon_enemigo = Squirtle()
elif pokemon_elegido == "charmander".upper():
    pokemon_enemigo = Charmander()

for ataque in mi_picachu.ataques:
    print(ataque)

while mi_picachu.vida > 0 and pokemon_enemigo.vida > 0:

    habilidad_picachu, poder_picachu = random.choice(list(mi_picachu.ataques.items()))
    print(habilidad_picachu)
    print(poder_picachu)
    mi_picachu.elegir_ataque(habilidad_picachu)
    mi_picachu.atacar(pokemon_enemigo)

    habilidad_enemiga, poder = random.choice(list(pokemon_enemigo.ataques.items()))
    print(habilidad_enemiga)
    print(poder)

    pokemon_enemigo.elegir_ataque(habilidad_enemiga)
    pokemon_enemigo.atacar(mi_picachu)

    print("Picachu {}".format(mi_picachu.vida))

    print("{} {} \n".format(pokemon_enemigo.nombre, pokemon_enemigo.vida))

if mi_picachu.vida <= 0 and pokemon_enemigo.vida <= 0:
    print("empate")
elif mi_picachu.vida <= 0:
    print("ha ganado ",pokemon_enemigo.nombre)
else:
    print("ha ganado picachu")