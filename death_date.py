import datetime
import random

AVERAGE_LIFESPAN = 80

SMOKER_PENALIZATION = 4
DRINKER_PENALIZATION = 6
SEDENTARY_PENALIZATION = 16

years_lost = 0


def print_with_underscores(message):
    print(message)
    print(len(message) * "-")


def ask_yes_or_not(message,penalization,year_lost):
    response = None
    while response != "S" and response != "N" and response != "A":
        response = input(message + " [S/N/A veces]")
    if response == "S":
        year_lost += penalization
    elif response == "A":
        year_lost += penalization/2
    return year_lost


def ask_yes_or_not_negative(message,penalization,year_lost):
    response = None
    while response != "S" and response != "N" and response != "A":
        response = input(message + " [S/N/A veces]")
    if response == "N":
        year_lost += penalization
    elif response == "A":
        year_lost += penalization/2
    return year_lost


print_with_underscores("¡Averigua cuanto te queda de vida!")
print("Completa esta encuesta para saber cuanto tiempo de vida te queda")

birth_date = input("¿Cuál es tu fecha de nacimiento (formato: dd/mm/yyyy)? ")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")


years_lost = ask_yes_or_not("¿Fumas?",SMOKER_PENALIZATION,years_lost)
years_lost = ask_yes_or_not("¿Bebes?",DRINKER_PENALIZATION,years_lost)

years_lost = ask_yes_or_not_negative("¿Haces deporte?",SEDENTARY_PENALIZATION,years_lost)

base_lifespan = random.random() * AVERAGE_LIFESPAN / 2 + AVERAGE_LIFESPAN / 2

lifespan = base_lifespan - years_lost

death_day = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()

print("Fecha de muerte {}, te quedan {} días para morir".format(death_day.strftime("%d/%m/%Y"), days_to_death.days))