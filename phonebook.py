import os
from typing import cast, Dict, Any

import json_tools
from common_func import root_path


class Contact:
    def __init__(self, name: str,
                 phone: str,
                 city: str | None,
                 email: str | None):

        self.name: str = name
        self.phone: str = phone
        self.city: str = city
        self.email: str = email

    def show(self):
        print(self.name)
        print(f"     Телефон: {self.phone}")
        if self.city:
            print(f"     Город: {self.city}")
        if self.email:
            print(f"     email: {self.email}")


class Phonebook:
    def __init__(self):
        self.contact_list: [Contact] = []
        self.phonebook_path = os.path.join(root_path, "phonebook.json")
        self.load()

    def load(self):
        json = cast(Dict[str, Any], json_tools.load(self.phonebook_path))
        if json:
            for value in json.values():
                self.contact_list.append(Contact(**value))

    def show(self):
        if len(self.contact_list) == 0:
            print("Телефонный справочник пуст.")
        else:
            print("Телефонный справочник:")
            for contact in self.contact_list:
                contact.show()
            print("\n\n")

    def add(self, contact: Contact):
        if self.check_contact_exist(contact.name):
            print(f"Контакт с именем {contact.name} уже существует.")
        else:
            self.contact_list.append(contact)
        self.save()

    def check_contact_exist(self, name: str) -> bool:
        for contact in self.contact_list:
            if contact.name == name:
                return True
        return False

    def save(self):
        json_dict = {}
        for contact in self.contact_list:
            json_dict[contact.name] = contact.__dict__
        json_tools.save(file_path=self.phonebook_path, data=json_dict)

    def update(self, old_name: str, update_contact: Contact):
        for contact in self.contact_list:
            if contact.name == old_name:
                self.contact_list.remove(contact)
                self.contact_list.append(update_contact)
        self.save()

    def delete(self, name: str):
        for contact in self.contact_list:
            if contact.name == name:
                self.contact_list.remove(contact)
        self.save()

