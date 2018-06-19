mi_lista = []
numero= input("dime un numero")

while numero != "FIN":
    mi_lista.append(numero)
    numero = input("Dime un numero (Para finalizar pon Fin)")

cuenta = 0

for number in mi_lista:
    cuenta += 1

print("los numeros son {} y son {} numeros".format(mi_lista,cuenta))