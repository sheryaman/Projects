import os
import random
import json
from datetime import datetime

class PasswordGenerator:
    def __init__(self):
      self.passwords = self.load_passwords()
      self.letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
      self.symbols = "!@#$%&*"
      self.numbers = "0123456789"
    def load_passwords(self):
       if not os.path.exists("passwords"):
            os.mkdir("passwords")
       try:
          with open("passwords/passwords.json", "r") as archive:
             return json.load(archive)
       except FileNotFoundError:
             return []
    def save_passwords(self):
       carpeta_guardado = os.path.join("passwords/passwords.json")
       with open(carpeta_guardado , "w") as archive:
          json.dump(self.passwords , archive)
    def generate(self):
       password_type  = input("what type do you like ? \n1.-numbers \n2.-letters \n3.-symbols \n4.-All ").lower()
       caracters = int(input("how many caracters ? up to 15 caracters available"))
       question = str(input("What is this password for ?"))
       while True:
        if password_type == "numbers"and caracters <16 :
          pool = "0123456789"
          password = "".join(random.choices(pool,k=caracters))
          now = datetime.now()
          self.passwords.append({ "password" : password , "password_type" : password_type , "caracters" : caracters , "question" : question , "time" : now.strftime("%d%m%Y %H:%M")})
          self.save_passwords()
          break
        elif password_type == "letters" and caracters < 16:
          pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
          password = "".join(random.choices(pool,k=caracters))
          now = datetime.now()
          self.passwords.append({ "password" : password , "password_type" : password_type , "caracters" : caracters , "question" : question , "time" : now.strftime("%d%m%Y %H:%M")})
          self.save_passwords()
          break
        elif password_type == "symbols" and caracters < 16:
          pool= "!@#$%&*"
          password = "".join(random.choices(pool,k=caracters))
          now = datetime.now()
          self.passwords.append({ "password" : password , "password_type" : password_type , "caracters" : caracters , "question" : question , "time" : now.strftime("%d%m%Y %H:%M")})
          self.save_passwords()
          break
        elif password_type == "All" and  caracters < 16:
          pool = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*"
          password = "".join(random.choices(pool,k=caracters))
          now = datetime.now()
          self.passwords.append({ "password" : password , "password_type" : password_type , "caracters" : caracters , "question" : question , "time" : now.strftime("%d%m%Y %H:%M")})
          self.save_passwords()
          break
        else:
           print("option not available")
    def show_passwords(self):
       if self.passwords == []:
          print("no passwords yet")
       else:
          for password in self.passwords:
             print(f" password : {password['password']} type : {password['password_type']} \n caracters : {password['caracters']} \n question : {password['question']} \n time: {password['time']}")
    def delete_password(self):
       name = input("What password are you going to delete ?")
       found  = False
       for password in self.passwords:
          if password['question'] == name:
             self.passwords.remove(password)
             self.save_passwords()   
             print(f"password {password['password']} deleted sucessfully")
             found = True
             break
       if not found:
             print("not found")
gen = PasswordGenerator()

while True:
    print("\n=== PASSWORD GENERATOR ===")
    print("1. Generate password")
    print("2. Show saved passwords")
    print("3. Delete password")
    print("4. Exit")

    option = input("\nChoose: ")

    if option == "1":
        gen.generate()
    elif option == "2":
        gen.show_passwords()
    elif option == "3":
        gen.delete_password()
    elif option == "4":
        break
             
       
          
          
         
          