mi_lista = []
producto= input("Dime cosas ")

while producto != "FIN":
    mi_lista.append(producto)
    producto = input("Dime cosas (Para finalizar pon Fin)")

for palabras in mi_lista:
    print("Esta palabra {} tiene de largo {}".format(palabras,len(palabras)))