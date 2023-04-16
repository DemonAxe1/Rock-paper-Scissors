###################################################################################################################
#Name: DemonAxe
#
#This code is a friendly game of rock paper scissors with a random bot picker.
#The user picks 1, 2, or 3 which represents rock paper and scissors
#Then the bot randomly picks one too, and then through an algorithm
#the winner is decided then the user is asked if they want to go again
#
###################################################################################################################

#importing the random library
import random

print("lets play Rock, Paper, Scissors!")

#Creating the graphics for the game
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
#Creating come vars to be used later
win = "YOU WIN"
lose = "YOU LOSE"
tie = "YOU TIED"
opt = [rock,paper,scissors]
test = 'y'  #this is set to y so the loop can start at least once


while test == 'y':
    opts = random.randint(1,3)
    player = int(input("'1' for rock, '2' for paper, '3' for scissors\n")) #Prompt the player to pick an option

    #This if statment checks if the player input anything other than 1, 2, or 3.
    if player >3 or player < 1:
      print("!THATS NOT A ANSWER!")
    else:
      print("You Chose: \n" + opt[player -1 ]) #If the user input a accepted value then we print the users selection with the graphic
  
      print("computer Chose: \n" + opt[opts - 1]) #This prints the bots selection with the graphic

    #if statments to check who won the game, could be a tie. Depending on the result we are printing a var that we had set earlier
    if player == 1 and opts == 2:
      print(lose)
    elif player == 2 and opts == 1:
      print(win)
    elif player == 2 and opts == 3:
      print(lose)
    elif player == 3 and opts == 2:
      print(win)
    elif player == 3 and opts == 1:
      print(lose)
    elif player == 2 and opts == 1:
      print(win)
    elif player == opts:
      print(tie)

    test = input("do you want to go again? (y for yes, anything else for no): ")    #Ask the user if they want to go again

print("Thank you for playing! See you next time!")  #Thank you msg when the program ends

#Logic for the conditions of winning
# 1<2 1>2 1=1
# 2<3 2>1 2=2
# 3<1 3>2 3=3
