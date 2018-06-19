
vida_pikachu =100

chispazo = 15
bola = 18

pokemon_elegido = input("¿Contra que pokemon quieres combaatir?").upper()

while  pokemon_elegido != "bulbasaur".upper() and pokemon_elegido != "squirtle".upper() and pokemon_elegido != "charmander".upper():
    pokemon_elegido = input("¿Contra que pokemon quieres combaatir?").upper()

if pokemon_elegido == "bulbasaur".upper():
    ataque = 12
    vida = 100
    nombre = "Bulbasur"
elif  pokemon_elegido != "squirtle".upper():
    ataque = 15
    vida = 90
    nombre = "Squirtle"
elif  pokemon_elegido != "charmander".upper():
    ataque = 16
    vida = 80
    nombre = "Charmander"

while vida_pikachu > 0 and vida > 0:
    poder = input("chispazo o bola :")

    while poder != "chispazo" and poder != "bola":
        poder = input("chispazo o bola :")

    if poder == "chispazo":
        vida -= chispazo
    else:
        vida -= bola

    vida_pikachu -= ataque

    print("Picachu {}".format(vida_pikachu))

    print("{} {} ".format(nombre,vida))

if vida_pikachu <=0 and vida <=0:
    print("empate")
elif vida_pikachu <= 0:
    print("ha ganado ",nombre)
else:
    print("ha ganado picachu")


