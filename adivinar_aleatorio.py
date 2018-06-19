import random
from time import sleep

number_to_guees = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor = random.choice(number_to_guees)
user_number =int(input("adivina  un numero: "))

sleep(3)
if user_number == valor:
    print("has adivinado")
else:
    print("has fallado y era el {}".format(valor))