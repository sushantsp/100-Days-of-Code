import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_input = random.randint(0,2)
if user_input>=3 or user_input <=0:
  print("you typed an invalid number. You lose !!")
else:
  if user_input == computer_input:
    print("Its a draw !!")
  elif user_input == 0 and computer_input == 1:
    print("Computer has won the game !!")
    print(rock + "vs" + paper)
  elif user_input == 0 and computer_input == 2:
    print("You have won the game !!")
    print(rock + "vs" + scissors)
  elif user_input == 1 and computer_input == 0:
    print("You have won the game !!")
    print(paper + "vs" + rock)
  elif user_input == 1 and computer_input == 2:
    print("Computer has won the game !!")
    print(paper + "vs" + scissors)
  elif user_input == 2 and computer_input == 0:
    print("Computer has won the game !! !!")
    print(scissors + "vs" + rock)
  elif user_input == 2 and computer_input == 1:
    print("You have won the game !!")
    print(scissors + "vs" + paper)


