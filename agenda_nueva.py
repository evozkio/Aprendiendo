dicipnario = dict()
agenda = {"adolfo": "11", "pepe": "12", "ana": "13", "maria": "44"}

hacer = input("Añadir un numero /Consultar numero (A/C)")


while hacer != "FIN":
    if hacer == "A":
       nombre = input("Nombre :")
       telefono = input("Telefono :")
       agenda[nombre] = telefono

    elif hacer == "C":
        consulta = input("Que quieres consultar")
        print(agenda[consulta])

    hacer = input("Quieres consultar,añadir o FIN (C/A/FIN)")