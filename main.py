import random

menu = 0
quit_character = "quit"
user_input = ""

#https://replit.com/@lagrassom/chatbot01#main.py refrenced this source code for def rando_response(user_input)
def rando_response(user_input):
  responses = [
    "That's Cool!",
    "Fascinating!",
    "Very Interesting!",
    "Wow that's good!",
    "Amazing !",
    "That's Great !"
  ]
  return random.choice(responses)

def start_convo(user_input):
  print("Hello My name is ChatBot! When you want to quit this conversation just say \"quit\"\n")
    
  user_input = input("Hello What's your name\n")
  if user_input == "quit":
    exit()
  print(f"Hello, {user_input}")
  
  user_input = input("How are you doing today !\n")
  if user_input == "quit":
    exit()
  if user_input.casefold() == "bad":
    print("oh sorry to hear that, I hope you feel better :(")
  elif user_input.casefold() == "mad":
    print("oh sorry to hear that, I hope you feel better :(")
  elif user_input.casefold() == "sad":
    print("oh sorry to hear that, I hope you feel better :(")
  else:
    print(rando_response(user_input))
  
  user_input = input("How old are you ?\n")
  if user_input == "quit":
    exit()
  if user_input <= "17":
    user_input = input("You're very young !\nWhat is your goals in life ?\n")
    print(rando_response(user_input))
  elif user_input <= "21":
    user_input = input("You're starting to grow up. \nHave you decided what you want to be in life ?\n")
    if user_input == "quit":
      exit()
    if user_input.casefold() == "yes":
      user_input = input("Has it changed since you were younger ?\n")
      if user_input == "quit":
        exit()
      if user_input.casefold() == "yes":
        user_input = input("What have you decided to be ?\n")
        print(rando_response(user_input))
      elif user_input.casefold() == "no":
        print(rando_response(user_input))
    elif user_input.casefold() == "no":
      print("Don't worry you'll know soon !\nDon't rush it it'll come to you !")
  elif user_input <= "30":
    user_input = input("Have you got your dream job ?\n")
    if user_input == "quit":
      exit()
    if user_input.casefold() == "yes":
      print("Congrats!")
      user_input = input("What is your job ?\n")
      print(rando_response(user_input))
    elif user_input.casefold() == "no":
      print("You'll get there one day")
  elif user_input <= "40":
    user_input = input("Have you completed your lifetime goals ?\n")
    if user_input == "quit":
      exit()
    if user_input.casefold() == "yes":
      print("I'm proud of you ! Congrats !")
    elif user_input.casefold() == "no":
      print("Maybe one day you can accomplish them !")
  else:
    user_input = input("Are you happy with what you accomplished?\n")
    if user_input == "quit":
      exit()
    if user_input.casefold() == "yes":
      print(rando_response(user_input))
    elif user_input.casefold() == "no":
      print("Maybe one day you can accomplish it. Don't ever stop trying")

start_convo(user_input)
    
def main_topics(menu):
    if menu == 0:
      topic = input("Pick A Topic:"
      "\n1. Guess A Number"
      "\n2. Family"
      "\n3. Hobbies\n")
      menu = 1
  
    if topic == "1":
      trys = 0
      number = random.randint(1, 10)
      print('Guess the number between 1-10. You have 3 trys')
      while trys != 3:
        number_guess = input()
        if number_guess == str(number):
          print("You got it!")
          menu = 0
        else:
          trys += 1
          print(f"Incorrect, You have {3 - trys} trys remaining")
    if topic == "2":
      family_total = 0
      family = input("Do you have a Dad?\n")
      if family.casefold() == "yes":
        family_total += 1
        print("That's great to hear !")
      elif family.casefold() == "no":
        print("Sorry to hear that :(")
      else:
        print("")
  
      family = input("Do you have a Mom?\n")
      if family.casefold() == "yes":
        family_total += 1
        print("That's good !")
      elif family.casefold() == "no":
        print("Sorry to hear that :(")
      else:
        print("")
  
      family = input("How Many Siblings do you have ?\n")
      if family.casefold() >= "1":
        family_total += int(family)
        print("That's great to hear !")
        print(f"You have a family of: {family_total}")
        menu = 0
      elif family.casefold() == "0":
        print("Sorry to hear that :(")
        menu = 0
      else:
        print("")
        menu = 0
  
    
      
    if topic == "3":
      hobbies = input("What do you like to do on your spare time ?\n")
      print(rando_response(hobbies))
      print("I like to do that too !")
      menu = 0

while user_input != quit_character:
  main_topics(menu)