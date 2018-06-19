mi_lista = []
producto= input("Que hay que comprar")

while producto != "FIN":
    mi_lista.append(producto)
    producto = input("Que hay que comprar (Para finalizar pon Fin)")

for item in mi_lista:
    print("Hay que comprar : {}".format(item))

print("Esto es lo que hay que comprar")