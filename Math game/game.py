import random as rand
from sqlite3 import Time
import time
import json as js
import threading as th

#------------------------------------Main game-----------------------------------------------
def main():
    print("Starting the game")

if __name__ == "__main__":
   main()
    
data = {

}
correct_answers = 0

def introduction():
    while True:
     initial = input(
            """Welcome to a math quiz, where we will test you under pressure of time!
90 seconds, 10 questions, the faster the higher in the leaderboard, ready(Y/N) or type l to see leaderboard?: """).lower()
    
     if initial == "y":
        print("Nice! Get ready.")
        return True
    
     elif initial == "n":
        print("Goodbye. LOSER!")
        return False
     
     elif initial == "l":
        see_leaderboard()
     else:
        print("YES or NO, its that simple, dumbo.")
        continue
     
def save_leaderboard(score, time_taken):
   name = input("Enter your name: ")

   data["name"] = name
   data["score"] = score
   data["time"] = time_taken

   with open("E:\\Programming\\Python\\Projects\\Active\\Math game\\leaderboard.json", "r") as file:
      save = js.load(file)

   save['leaderboard'].append(data)

   with open("E:\\Programming\\Python\\Projects\\Active\\Math game\\leaderboard.json", "w") as file:
      js.dump(save, file, indent=4)

def ask_question(num1, num2, op):
    global correct_answers, time_end

    if op == "+":
         correct = num1 + num2
    elif op == "-":
         correct = num1 - num2
    elif op == "*":
         correct = num1 * num2
    elif op == "/":
         correct = num1 / num2
      
    try:
         answer = float(input(f"{num1} {op} {num2} = "))
      
    except ValueError:
         print("Its a math game, dumbo.")
         return ask_question(num1, num2, op) 


    if answer == correct:
         correct_answers += 1
         print("Correct!")
    else:
         print("Wrong!")

def see_leaderboard():
   with open ("E:\\Programming\\Python\\Projects\\Active\\Math game\\leaderboard.json", "r") as file:
      data = js.load(file)
      sorted_leaderboard = sorted(data["leaderboard"], key=lambda player: player["score"], reverse=True) 

      for player in sorted_leaderboard:
         print(f"name:{player['name']} --- score: {player['score']:.0f} --- time: {player['time']:.0f} seconds")

def question_1():
   number = rand.randint(1, 10) 
   number_2 = rand.randint(1, 10)
   ask_question(number, number_2, "+")

def question_2():
   number = rand.randint(50, 100)
   number_2 = rand.randint(50, 100)
   ask_question(number, number_2, "+")

def question_3():
   number = rand.randint(50, 60) 
   number_2 = rand.randint(10, 40)
   ask_question(number, number_2, "-")

def question_4():
   number = rand.randint(100, 150)
   number_2 = rand.randint(50, 100)
   ask_question(number, number_2, "-")

def question_5():
   number = rand.randint(1, 10)
   number_2 = rand.randint(1, 10)
   ask_question(number, number_2, "*")

def question_6():
   number = rand.randint(1, 15) 
   number_2 = rand.randint(1, 15)
   ask_question(number, number_2, "*")

def question_7():
   number = rand.randrange(20, 41, 2) 
   number_2 = rand.randrange(2, 21, 2)
   while True:
       if number % number_2 == 0:
          break
       else:
          number = rand.randrange(20, 41, 2) 
          number_2 = rand.randrange(2, 21, 2)
   ask_question(number, number_2, "/")

def question_8():
   number = rand.randrange(51, 101, 2) 
   number_2 = rand.randrange(2, 51, 2)
   while True:
       if number % number_2 == 0:
          break
       else:
          number = rand.randrange(20, 41, 2) 
          number_2 = rand.randrange(2, 21, 2)
   ask_question(number, number_2, "/")


def question_9():
   number = rand.randint(200, 500) 
   number_2 = rand.randint(100, 200)
   ask_question(number, number_2, "+")

def question_10():
   number = rand.randint(1000, 1400) 
   number_2 = rand.randint(500, 600)
   ask_question(number, number_2, "-")


while True:
   if introduction():
      time_start = time.time()

      functions = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]

      for funct in functions:
         if time.time() - time_start >= 90:
            print("Time's up! LOSER!")
            break
         else:
            funct()

      time_end1 = time.time()

      time_taken = time_end1 - time_start
      time_left = 90 - time_taken
      score = correct_answers * 100 + time_left * 10

      print(f"score: {score:.0f} = {correct_answers} * 100 + {time_left:.0f} * 10")
      save_score = input("Do you want to save your score?(Y/N): ").lower()

      if save_score == "y":
         save_leaderboard(score, time_taken)

      elif save_score == "n":
         print("I BET YOU MESSED UP, LOSER!")
         break

      else:
         print("YES or NO, its that simple, dumbo.")
         continue
   else:
      break
