import pickle

from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas? ")

    return int(selected_action)

def information(data,location,contacts):
    print("\nInformación sobre {}\n".format(contacts[location][data]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**contacts[location]))
    sleep(2)


def select_two(one, two, question):
    response = input(question)
    while response != one and response != two:
        response = input(question)
    return response


def found_element (element, data,contacts):
    search_term = input("Introducir el {} del contacto o parte de él: ".format(data))
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact[element].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact[element]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        return

    return contact_index


def show_menu():
    print("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts):
    found = "Y"

    while found != "N":

        print("\n\nAñadir contacto\n")
        contact = {
            "name": input("Nombre: "),
            "phone": input("Teléfono: "),
            "email": input("Email: ")
        }
        contacts.append(contact)
        print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
        sleep(2)

        found = select_two("S", "N", "Quieres seguir añadiendo contactos (S/N)")


def remove_contact(contacts):

    print("Que contacto quieres borrar")
    del_contact = found_element("name", "nombre", contacts)

    if select_two("S", "N", "Quieres borrar este contacto (S/N)") == "S":
        del contacts[del_contact]

    print("El contacto a sido borrado con exito")
    sleep(2)


def find_contact(contacts):
    found = "Y"

    while found != "N":

        print("\n\nBuscar contacto\n")
        name_or_email = select_two("nombre","email","Que quires buscar un nombre o un email ?")

        if name_or_email == "nombre":
            index = found_element("name", "nombre", contacts)
            information("name", index,contacts)

        elif name_or_email == "email":
            index = found_element("email", "email", contacts)
            information("email", index,contacts)

        found = select_two("S", "N", "Quieres seguir buscando (S/N)")


def export_contacts():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def main():
    contacts = load_contacts()
    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            export_contacts()

        action = show_menu()

    save_contacts(contacts)
    print("¡Adiós!")


if __name__ == "__main__":
    main()
