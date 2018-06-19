numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,20,15,30,60,70]

multiplos_dos = []
multiplos_tres = []
multiplos__cinco = []
multiplos_siete = []

for number in range(len(numeros)):
    numero = numeros[number]
    if numero % 2 == 0:
        multiplos_dos.append(numero)
    if numero % 3 == 0:
        multiplos_tres.append(numero)
    if numero % 5 == 0:
        multiplos__cinco.append(numero)
    if numero % 7 == 0:
        multiplos_siete.append(numero)

print(numeros)
print(multiplos_dos)
print(multiplos_tres)
print(multiplos__cinco)
print(multiplos_siete)