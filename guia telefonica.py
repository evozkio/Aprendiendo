nombre_telefonico = ["adolfo","pepe","ana","maria","isaac"]
numero_telefonica = [66,77,88,99,11]

indice = 0
valor = None
hacer = input("Añadir un numero /Consultar numero (A/C)")

nombre = None
telefono = None

while hacer != "FIN":
    if hacer == "A":
       nombre = input("Nombre :")
       nombre_telefonico.append(nombre)

       telefono = input("Telefono :")
       numero_telefonica.append(telefono)

    elif hacer == "C":
        consultar = input("nombre o numero :")

        if consultar == "nombre":
            buscar = input("Que nombre :")

            for nombres in nombre_telefonico:
                if nombres == buscar:
                    valor = indice
                indice += 1
            print("Me has pedido el numero de {} y  es {}".format(buscar,numero_telefonica[valor]))

        elif consultar == "numero":
            buscar = int(input("Que numero :"))

            for numeros in numero_telefonica:
                if numeros == buscar:
                    valor = indice
                indice += 1
            print("Me has pedido el nombre de  {} y  es {}".format(buscar, nombre_telefonico[valor]))
    hacer = input("Quieres consultar,añadir o FIN (C/A/FIN)")