palabra_usuario=input("Dime una palabra")
vocales = "AEIOUaeiou"


for vocal in vocales:
    palabra_usuario=palabra_usuario.replace(vocal,"i")

print(palabra_usuario)

