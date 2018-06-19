
def mayor (lista):
    mayor = lista[0]
    for grande in lista:
        if grande > mayor:
            mayor = grande
    return mayor

primer_numero = int(input("primer numero: "))
segundo_numero = int(input("segundo numero: "))
tercer_numero = int(input("tercero numero: "))

resultado = [primer_numero,segundo_numero,tercer_numero]

print("El numero mas grande es {}".format(mayor(resultado)))