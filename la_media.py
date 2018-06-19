mi_lista = []
numero= int(input("dime un numero"))

while numero != 0:
    mi_lista.append(numero)
    numero = int(input("Dime un numero (Para finalizar pon 0)"))

suma = None

for number in mi_lista:
    suma += number

media = suma/len(mi_lista)

print("los numeros son {} y la media es {} ".format(mi_lista,media))