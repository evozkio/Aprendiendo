number_to_guees = int(input("elige un numero"))
user_number =int(input("adivina  un numero: "))


while user_number != number_to_guees:
    print("No es")
    user_number = int(input("adivina  un numero: "))

print("Has acertado")
