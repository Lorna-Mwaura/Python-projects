#rock paper scissors game
import random
from secrets import choice

print('Welcome to our game')
print('*'*60)
while True:
    play = input("choose rock, paper or scissors : ").lower() # take user input
    options = ['rock','paper','scissors'] # list of options to choose from in the game

    computer = random.choice(options) # generate a random option from the list and store it
    #print(computer)

    if computer == 'rock':
        if play == 'rock':
            print('Tie!')
        if play == 'paper':
            print('you win')
            break
        if play == 'scissors':
            print ('You loose',computer, 'crashes you !')
        
    elif computer == 'paper':
        if play == 'rock':
            print('You loose',computer, 'crashes you !')
        if play == 'paper':
            print(' you Tie!')
        if play == 'scissors':
            print('you win')
            break
       
    elif computer == 'scissors':
        if play == 'rock':
            print('you win')
            break
        if play == 'paper':
            print ('You loose',computer, 'cuts you !')
        if play == 'scissors':
            print(' You Tie!')
        
    else:
        print('Enter a valid choice')
        break