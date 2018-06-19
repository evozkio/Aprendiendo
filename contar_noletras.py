
texto_usuario = input("Dime una frase que quieras que cuente sus espacios comas y puntos")

espacios = 0
puntos = 0
comas = 0

for caracter in texto_usuario:
    if caracter == " ":
        espacios += 1
    elif caracter == ".":
        puntos += 1
    elif caracter == ",":
        comas += 1

print("Los espacios son : {}".format(espacios))
print("Los puntos son : {}".format(puntos))
print("Las comas son : {}".format(comas))