agenda=[["adolfo","11"],["pepe","12"],["ana","13"],["maria","44"]]

hacer = input("Añadir un numero /Consultar numero (A/C)")


while hacer != "FIN":
    if hacer == "A":
       nombre = input("Nombre :")
       telefono = input("Telefono :")
       agenda.append([nombre,telefono])

    elif hacer == "C":
        consultar = input("nombre o numero :")

        if consultar == "nombre":
            buscar = input("Que nombre :")

            for nombre_numero in agenda:
                if nombre_numero[0] == buscar:
                    print("Me has pedido el numero de {} y  es {}".format(buscar,nombre_numero[1]))


        elif consultar == "numero":
            buscar = (input("Que numero :"))

            for nombre_numero in agenda:
                if nombre_numero[1] == buscar:
                    print("Me has pedido el numero de {} y  es {}".format(buscar, nombre_numero[0]))
    hacer = input("Quieres consultar,añadir o FIN (C/A/FIN)")