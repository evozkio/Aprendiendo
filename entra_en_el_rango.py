def unocien (valor):
    if valor <= 100 and valor >= 1:
        unocien = True
    else:
        unocien = False

    return unocien

numero = int(input("dime un numero: "))

print(unocien(numero))