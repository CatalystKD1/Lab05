import random
def start():
  print("What would you like the highest number to be?")
# You could also have them input the value on the same line as the text, however it looks nicer in the comand line like this
  maxNum = int(input())
  rnd = random.randint(0, maxNum)
  guessFunc(maxNum, rnd)
def hint(help):
  print(help)
def guessFunc(maxNum, rnd):
  print("Guess a number between 0 and " + str(maxNum))
  guess = int(input())
  if guess > maxNum:
    print("Your guess is higher then your max value dumby! In case you need a reminder, you max number is " + str(maxNum))
    guessFunc(maxNum, rnd)
  else:
    game(maxNum, rnd, guess)
def playAgain():
  print("Would you like to paly again? Type y or n (yes or no).")
  answer = input()
  if answer == "n" or answer == "N":
    print("Have a good day!")
    return;
  elif answer == "y" or answer == "Y":
    print("Let's play again!")
    start()
def game(maxNum, rnd, guess):
  if guess == rnd:
    print("You are correct!")
    playAgain()
  elif guess < rnd:
    hint(str(guess) + " is lower then the nubmer you are looking for.")
    guessFunc(maxNum, rnd)
  elif(guess> rnd):
    hint(str(guess) + " is higher then the nubmer you are looking for.")
    guessFunc(maxNum, rnd)
start()