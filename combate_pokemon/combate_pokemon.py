import random
from time import sleep

from pokemon_oo import Pikachu, Bulbasur, Squirtle, Charmander

mi_pikachu = Pikachu()


def choose_pokemon():
    pokemon_elegido = input("¿Contra que pokemon quieres combaatir?").upper()

    while pokemon_elegido != "bulbasaur".upper() and pokemon_elegido != "squirtle".upper() \
            and pokemon_elegido != "charmander".upper():
        pokemon_elegido = input("¿Contra que pokemon quieres combaatir?").upper()

    if pokemon_elegido == "bulbasaur".upper():
        return Bulbasur()
    elif pokemon_elegido == "squirtle".upper():
        return Squirtle()
    elif pokemon_elegido == "charmander".upper():
        return Charmander()


def show_my_pokemon_attacks():
    for ataque in mi_pikachu.ataques:
        print(ataque.name)


def show_hp_pokemon(pokemon):
    if pokemon.vida < 0:
        pokemon.vida = 0
    print("La vida de {} esta a {}".format(pokemon.name, pokemon.vida))

def show_attack(skill, pokemon):
    print("{} ataca con  {} y hace {}".format(pokemon.name, skill.name, skill.dmg))

def combat(pokemon_enemigo):
    while mi_pikachu.vida > 0 and pokemon_enemigo.vida > 0:

        habilidad_picachu = random.choice(list(mi_pikachu.ataques))
        mi_pikachu.elegir_ataque(habilidad_picachu.dmg)
        mi_pikachu.atacar(pokemon_enemigo)
        show_attack(habilidad_picachu, mi_pikachu)

        habilidad_enemiga = random.choice(list(pokemon_enemigo.ataques))
        pokemon_enemigo.elegir_ataque(habilidad_enemiga.dmg)
        pokemon_enemigo.atacar(mi_pikachu)
        show_attack(habilidad_enemiga, pokemon_enemigo)

        show_hp_pokemon(mi_pikachu)
        show_hp_pokemon(pokemon_enemigo)
        print("\n \n")

        sleep(1)
    if mi_pikachu.vida <= 0 and pokemon_enemigo.vida <= 0:
        print("empate")
    elif mi_pikachu.vida <= 0:
        print("ha ganado ",pokemon_enemigo.nombre)
    else:
        print("ha ganado picachu")

def main():
    pokemon_enemy = choose_pokemon()

    show_my_pokemon_attacks()

    combat(pokemon_enemy)


if __name__ == '__main__':
    main()

