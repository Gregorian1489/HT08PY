from phonebook import Phonebook, Contact


def create_contact() -> Contact:
    name = input("Введите имя контакта.\n")
    if not name:
        print("Имя контакта не может быть пустым.\n")
        return
    phone = input("Введите номер телефона.\n")
    if not phone:
        print("Номер телефона не может быть пустым.\n")
        return
    city = input("Введите город.\n")
    email = input("Введите email.\n")
    return Contact(name=name, phone=phone, city=city, email=email)


def menu():
    while True:
        command = input("Выберите действие:\n"
                        "1. Показать записи справочника.\n"
                        "2. Добавить запись.\n"
                        "3. Удалить запись.\n"
                        "4. Изменить запись.\n"
                        "5. Выход.\n")
        match command:
            case "1":
                ph.show()
            case "2":
                print("Добавление контакта:")
                ph.add(create_contact())
            case "3":
                name = input("Введите имя удаляемой записи.\n")
                if ph.check_contact_exist(name):
                    ph.delete(name)
                    print(f"Контакт с именем {name} удален.\n")
                else:
                    print(f"Контакт с именем {name} не найден.\n")
            case "4":
                name = input("Введите имя изменяемой записи.\n")
                if ph.check_contact_exist(name):
                    ph.update(name, create_contact())
                else:
                    print(f"Контакт с именем {name} не найден.\n")
            case "5":
                exit()
            case _:
                pass


if __name__ == '__main__':
    ph = Phonebook()
    menu()
