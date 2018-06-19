apetece_helado= input("te apete un helado ?(Si /No): ").upper()
tiene_dinero = input("Tienes dinero para un helado? (Si / NO): ").upper()
esta_tu_tia = input("Esta tu tia? ").upper()

if apetece_helado == "Si" and (tiene_dinero == "Si" or esta_tu_tia == "Si"):
    print("Compro un helado")
else:
    if apetece_helado == "Si":
        print("No hay dinero o no esta tu tia")
    if tiene_dinero == "Si" or esta_tu_tia == "Si":
        print("No te apetece helado")
    else:
        print("pues nada")


