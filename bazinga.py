numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,20,15,30,60,70]

for number in range(len(numeros)):
    numero = numeros[number]
    if numero % 3 == 0 and numero % 5 == 0:
        numeros[number] = "Bazinga"
    elif numero % 3 == 0:
        numeros[number] = "Fizz"
    elif numero % 5 == 0:
        numeros[number] = "Buzz"

print(numeros)
