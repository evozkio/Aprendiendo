palabra_usuario=input("Dime una palabra")
vocales = "AEIOUaeiou"

numero=0


for vocal in vocales:
    palabra_usuario=palabra_usuario.replace(vocal,str(numero))
    for digito in palabra_usuario:
        if digito == str(numero):
            numero +=1


print(palabra_usuario)