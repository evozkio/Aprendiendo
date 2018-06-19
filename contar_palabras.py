dime = input("Dime  una frase para contar sus palabras")

diccionario = dict()

lista_dime = dime.split(" ")

for contar in lista_dime:
    if contar in diccionario:
        diccionario[contar] += 1
    else:
        diccionario[contar] = 1

print(diccionario)