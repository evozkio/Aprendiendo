mi_lista = []
producto= input("Dime cosas")

lista_strings=[]
lista_enteros=[]

while producto != "FIN":
    if producto.isdigit():
        producto=int(producto)
    mi_lista.append(producto)
    producto = input("Dime cosas (Para finalizar pon Fin)")

for tipos in mi_lista:
    if type(tipos)== int:
        lista_enteros.append(tipos)
    else:
        lista_strings.append(tipos)

print("Lista de strings es {}".format(lista_strings))
print("Lista de numeros es {}".format(lista_enteros))
