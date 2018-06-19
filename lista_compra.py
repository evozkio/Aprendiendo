mi_lista = []
producto= input("Que hay que comprar")

while producto != "FIN":
    mi_lista.append(producto)
    producto = input("Que hay que comprar (Para finalizar pon Fin)")

largo_lista = len(mi_lista)
indice = 0

while largo_lista != indice:
    print("Hay que comprar : {}".format(mi_lista[indice]))
    indice +=1

print("Esto es lo que hay que comprar")
