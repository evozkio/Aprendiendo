agenda = dict()

while hacer != "SI":
    if hacer == "A":
       nombre = input("Nombre :")
       nacimiento = input("cuando nacio :")
       agenda[nombre] = nacimiento

    hacer = input("Quieres terminar ")