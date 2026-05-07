import json
import os 
import random
from datetime import  date , datetime
class Random_Game:
    def __init__(self):
      self.records = self.reload_record()
      self.difficulties = {"easy" : 10 , "medium" : 20 , "hard" : 30}

    def reload_record(self):
       try:
         with open("records.json" ,"r") as archive:
           return json.load(archive)
       except FileNotFoundError:
         return []
    def save_record(self,winner,attempts,difficulty,seconds):
      seconds = datetime.now().strftime("%S")
      self.records.append({"winner" : winner , "attempts" : attempts , "difficulty" : difficulty , "seconds" : seconds})
      with open ("records.json", "w") as archive:
        json.dump(self.records , archive)
    def show_records(self):
      if self.records == []:
       print("no records yet")
      else:
        for record in self.records:
          print(f"the last winner was {record['winner']} in {record['attempts']} with {record['difficulty']} difficulty and in {record['seconds']}")
    def choose_difficulty(self):
     while True:
      difficulty = input("Choose a difficult \neasy \nmedium \nhard \n").lower()
      if difficulty == "easy":
        return self.difficulties[difficulty]
        break
      elif difficulty == "medium":
        return self.difficulties[difficulty]
        break
      elif difficulty == "hard":
        return self.difficulties[difficulty]
        break
      else:
        print("valor incorrecto")
    def get_players(self):
      player_1_name = str(input("Player 1 Name:\n"))
      player_2_name =  str(input("player 2 name:\n"))
      return player_1_name , player_2_name
    def play(self):
       dificultad = self.choose_difficulty()
       player_1 , player_2 = self.get_players()
       Numero = random.randint(1 , dificultad)
       chosen_player = random.choice([player_1 , player_2])
       attempts = 0
       start = datetime.now()
       while True:
        guess  = int(input("guess the secret number\n"))
        attempts += 1
        if guess == Numero:
          seconds = (datetime.now() - start).seconds
          print(f"the current winner is {chosen_player} in {seconds} seconds and {attempts} attempts")
          self.save_record(chosen_player , seconds , attempts ,dificultad)
          break
        elif guess > Numero:
          print("Lower")
        elif guess < Numero:
          print("Higher")
        if chosen_player == player_1:
          chosen_player = player_2
        else:
          chosen_player  = player_1
game_1 = Random_Game()
while True:
  print("Number Quest")
  print("1.- Play")
  print("2.-Records")
  print("3.-Exit")
  option = (input())
  if option == "1":
     game_1.play()
  elif option == "2":
     game_1.show_records()
  elif option == "3":
    break


