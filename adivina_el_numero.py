number_to_guees = 2
user_number =int(input("adivina  un numero: "))
if user_number == number_to_guees:
    print("has adivinado")
else:
    print("has fallado")
    user_number =int(input("adivina  un numero: "))
    if user_number == number_to_guees:
        print("has adivinado")
    else:
        print("has fallado")
        user_number = int(input("adivina  un numero: "))
        if user_number == number_to_guees:
            print("has adivinado")
        else:
            print("has fallado")
            user_number = int(input("adivina  un numero: "))
            if user_number == number_to_guees:
                print("has adivinado")
            else:
                print("has fallado")
                user_number = int(input("adivina  un numero: "))
                if user_number == number_to_guees:
                    print("has adivinado")
                else:
                    print("has fallado")

