mi_lista=[]
numero_usuario = int(input("Dime un  numero"))

while numero_usuario != 0:
    mi_lista.append(numero_usuario)
    numero_usuario = int(input("Dime un  numero"))


valor=1

for multiplicar in mi_lista:
    valor *= multiplicar

print("El resultado de multiplicar  estos numeros {} son {}".format(mi_lista,valor))


