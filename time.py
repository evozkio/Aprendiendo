from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 1





def ask_yes_or_not(message):
    response = None
    while response != "S" and response != "N":
        response = input(message + " [S/N]")
    return response


def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)


def main():
    current_time = datetime.datetime.now()
    is_night = False

    day_week = ""
    day = ""
    hour = None

    if ask_yes_or_not("Quieres una alarma para alguna hora ?") == "S":
        hour = int(input("Hora ?"))
        if ask_yes_or_not("Para algun dia?") == "S":
            day_week = input("Que dia en ingles")
        elif ask_yes_or_not("Quieres que suene en un dia concreto ?") == "S":
            day = input("Que dia  (formato: dd/mm/yyyy)?")

    while True:
        now = current_time.strftime("%d/%m/%Y")
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True

        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True

        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de día", "horas.txt")

        if day_week != "" or day != "":
            if hour == current_time.hour and day_week == current_time.strftime("%A"):
                write_file_and_screen("Es la hora y el dia", "horas.txt")
            if hour == current_time.hour and day == now:
                write_file_and_screen("Es la hora y fecha ", "horas.txt")
        elif hour == current_time.hour:
            write_file_and_screen("Es la hora", "horas.txt")





        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")




if __name__ == "__main__":
    main()
