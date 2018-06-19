numero_elegido= int(input("Elige un numero"))
for a in range (10,0,-1):
    calculo = numero_elegido * a
    print("{} x {} = {}".format(numero_elegido,a,calculo))