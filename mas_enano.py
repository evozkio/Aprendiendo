mi_lista = []
numero= input("dime un numero")

while numero != "FIN":
    mi_lista.append(numero)
    numero = input("Dime un numero (Para finalizar pon Fin)")

numero_menor = mi_lista[0]

for menor in mi_lista:
    if numero_menor >= menor:
        numero_menor = menor

print("El numero menor es : {} {}".format(numero_menor,min(mi_lista)))