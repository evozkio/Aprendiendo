from time import sleep
import datetime
import random

zero = ["viva la vida", "besos para todos"]
one = ["silla", "mesa", "armario"]
two = ["Cocacola", "fanta", "Pepsi", "Kas", "Zumo"]
three = ["Ojala te mueras", "Que te parta un rayo"]
four = ["espaguetis", "tortilla de patatas"]
five = ["eqwerqerw" , "ertw gdfs"]
six = ["leon", "caballo", "mosaca"]
seven = ["vamos que  tu puedes", "eres el mismisimo dios"]
eight = [" Muuuuuuu" ,"Beeeeeeee"]
nine = ["Te vas a morir  mañana ", "Se te morio el perro"]

fin = None

while fin != "FIN":
    sleep(1)
    current_time = datetime.datetime.now()
    last_digit = str(current_time.second)[-1]
    print(current_time.strftime("%H:%M:%S"))
    if last_digit == "0":
        print(random.choice(zero))
    elif last_digit == "1":
        print(random.choice(one))
    elif last_digit == "2":
        print(random.choice(two))
    elif last_digit == "3":
        print(random.choice(three))
    elif last_digit == "4":
        print(random.choice(four))
    elif last_digit == "5":
        print(random.choice(five))
    elif last_digit == "6":
        print(random.choice(six))
    elif last_digit == "7":
        print(random.choice(seven))
    elif last_digit == "8":
        print(random.choice(eight))
    elif last_digit == "9":
        print(random.choice(nine))

