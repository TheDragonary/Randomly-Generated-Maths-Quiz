import random
import operator
import sys
import os
from getkey import getkey, keys
import time

operator_functions = {
    '+': operator.add, 
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

op = ["+","-","*"]
question = 0
answer = 0
num1 = 0
num2 = 0
score = 0

os.system('cls')

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

def timed():
  os.system('cls')
  try:
	  timer = int(input("Timer length in seconds: "))
  except ValueError:
  	print("Try again!\n")
  	timer = int(input("Timer length in seconds: "))

  try:
  	min = int(input("Minimum number: "))
  except ValueError:
    print("Try again!\n")
    min = int(input("Minimum number: "))
	
  try:
  	max = int(input("Maximum number: "))
  except ValueError:
	  print("Try again!\n")
	  max = int(input("Maximum number: "))

  start = time.time() + timer
  end = time.time()

  while (start - end) > 0:
    os.system('cls')
    print(f"You have {round(start - end)}s remaining")
    global question
    question = question + 1
    global num1
    int(num1)
    global num2
    int(num2)
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)
    operator = random.choice(op)
    print("\nQuestion " + str(question))
    
    try:
      answer = int(input("What is {} {} {}? ".format(num1,operator,num2)))
      
      if answer == (operator_functions[operator](num1, num2)):
        global score
        score = score + 1
        print("Correct")
        time.sleep(1)
        start = start + 1
      else:
        print("Wrong")
        time.sleep(1)
        start = start + 1
        continue
        
    except ValueError:
      print("Skipped!")
      time.sleep(1)
      start = start + 1
      
    end = time.time()

  print("\nTotal score: " + str(score) + "/" + str(question) + "\n")
    
def infinite():
  try:
  	min = int(input("Minimum number: "))
  except ValueError:
    print("Try again!\n")
    min = int(input("Minimum number: "))
	
  try:
  	max = int(input("Maximum number: "))
  except ValueError:
	  print("Try again!\n")
	  max = int(input("Maximum number: "))

  while True:
    os.system('cls')
    global question
    question = question + 1
    global num1
    int(num1)
    global num2
    int(num2)
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)
    operator = random.choice(op)
    print("Question " + str(question))
    
    try:
      answer = int(input("What is {} {} {}? ".format(num1,operator,num2)))
    except ValueError:
      print("No input = Game over!")
      time.sleep(1)
      break
      
    if answer == (operator_functions[operator](num1, num2)):
      global score
      score = score + 1
      print("Correct")
      time.sleep(1)
    else:
      print("Wrong")
      break

  print("\nTotal score: " + str(score) + "\n")

def tutorial():
  os.system('cls')
  tut = int(input("Choose the gamemode you'd like a tutorial for:\n1. Timed\n2. Infinite\n"))
  
  if tut == 1:
    os.system('cls')
    print("This is the tutorial for Timed Mode\n\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("'Timer length in seconds:'\n\nChoose how long you'd want the timer for the quiz to be in seconds (Example: 60 = 60 seconds)\n\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("'Minimum number:'\n'Maximum number:'\n\nChoose the range of numbers you'd want the quiz to randomly pick numbers from (Example: Minimum = 1, Maximum = 10)\n\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("Simply type the answers to each question\n\nCorrect answers = 1 point\nWrong answers = 0 points and goes to the next question\nNo input would just skip the question\n\nWhen the time is up, the game will show your score\n\n")
    print("That's the end of Timed Mode tutorial!\n\nPress Enter to go back to the main menu")

  if tut == 2:
    os.system('cls')
    print("This is the tutorial for Infinite Mode\n\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("'Minimum number:'\n'Maximum number:'\n\nChoose the range of numbers you'd want the quiz to randomly pick numbers from (Example: Minimum = 1, Maximum = 10)\n\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("Simply type the answers to each question\n\nCorrect answers = 1 point\nWrong answers and no input would end the game and show your score\n\n")
    print("That's the end of Infinite Mode tutorial!\n\nPress Enter to go back to the main menu")
    
  key = getkey()
  if key == keys.ENTER:
    restart_program()

print("The Randomly Generated Maths Quiz!")
gamemode = int(input("Choose a gamemode:\n1. Timed\n2. Infinite\n3. Tutorial\n"))
if gamemode == 1:
  timed()
elif gamemode == 2:
  infinite()
elif gamemode == 3:
  tutorial()

print("\nPress Enter to restart or Esc to end game:\n")

while True:
	key = getkey()
	if key == keys.ENTER:
		restart_program()
	elif key == keys.ESCAPE:
		print("Game ended")
		exit()
