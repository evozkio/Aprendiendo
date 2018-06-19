texto_usuario = input("Dime una frase que quieras que cuente sus mayusculas  ")

mayusculas = 0

for mayus in texto_usuario:
    if mayus.upper() == mayus:
        mayusculas += 1

print("El numero de mayus son : {}".format(mayusculas))