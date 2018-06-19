texto_usuario = input("Dime una frase para hacer una lista de vocales")

vocal= "aoeiu"

mi_lista_vocales=[]

for vocales in texto_usuario:
    for igual in vocal:
        if vocales == igual:
            mi_lista_vocales.append(vocales)

print(mi_lista_vocales)
