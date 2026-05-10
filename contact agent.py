import json
import os
from datetime import datetime , date


class Contact_Agenda:
    def __init__(self):
     self.contacts = self.load_contacts()
    def load_contacts(self):
       try:
          with open("contacts.json" , "r") as archive:
             return json.load(archive)
       except FileNotFoundError:
          return []
    def save_contacts(self):
       with open("contacts.json", "w") as archive:
          json.dump(self.contacts , archive)
    def add_contacts(self):
       name = input("introduce contact name")
       phone = input("introduce phone contact")
       email = input("introduce email contact")
       now = datetime.now()
       self.contacts.append({"name" : name , "phone" : phone , "email" : email , "time" : now.strftime("%d%m%Y %H:%M")})
       self.save_contacts()
    def show_all(self):
       if self.contacts ==  []:
          print("No Contacts yet")
       else:
          for contact in self.contacts:
             print(f" name : {contact['name']} phone : {contact['phone']} , email:  {contact['email']} , {contact['time']} ")
    def search(self):
       name = input("Write contact name").lower()
       found = False
       for contact in self.contacts:
          if contact['name'].lower() ==  name.lower():
             print(f" name : {contact['name']} phone : {contact['phone']} , email:  {contact['email']} , {contact['time']}")
             found = True
             break
          if not found:
             print("contact not found")
    def delete(self):
        name = input("write contact name to delete").lower()
        found = False
        for contact in self.contacts:
           if contact['name'].lower() == name.lower():
             self.contacts.remove(contact)
             self.save_contacts()
             print(f"{contact['name']}deleted")
             found = True
           if not found:
              print("contact not found  abort delete contact operation")
Agenda_1 = Contact_Agenda()


while True:
    print("\n=== CONTACT AGENDA ===")
    print("1. Add contact")
    print("2. Show all")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")

    option = input("\nChoose: ")

    if option == "1":
        Agenda_1.add_contacts()
    elif option == "2":
        Agenda_1.show_all()
    elif option == "3":
        Agenda_1.search()
    elif option == "4":
        Agenda_1.delete()
    elif option == "5":
        break
   
              
          
          