# Import the random library to be able to generate a random number
import random

# Create sym and history list
sym = ['rock', 'paper', 'scissors']
history = []

# Intro text
print('Select rock, paper or scissors to play')
print('Type "exit" to exit the program')


# Define functions

# Checks if user input is valid
# Mainly determines who has won
def who_won(user, comp):
    while user != 'rock' and user != 'paper' and user != 'scissors':
        print('Invalid Selection')
        user = input('Rock, Paper, or Scissors: ')
        user = user.lower()

    if user == 'rock':
        if comp == 'rock':
            print('It is a tie')
            history.append('Tie')
        elif comp == 'paper':
            print('You lost')
            history.append('Lost')
        elif comp == 'scissors':
            print('You won!')
            history.append('Won')
    elif user == 'paper':
        if comp == 'rock':
            print('You won!')
            history.append('Won')
        elif comp == 'paper':
            print('It is a tie')
            history.append('Tie')
        elif comp == 'scissors':
            print('You lost')
            history.append('Lost')
    elif user == 'scissors':
        if comp == 'rock':
            print('You lost')
            history.append('Lost')
        elif comp == 'paper':
            print('You won!')
            history.append('Won')
        elif comp == 'scissors':
            print('It is a tie')
            history.append('Tie')


# Defines user selection
def user_select():
    selection = input('Rock, Paper, or Scissors: ')
    selection = selection.lower()
    return selection


# Defines computer selection
# Generates a int from 0 to 2 inclusive and uses the index of the 'sym' list
def comp_select():
    number = random.randint(0, 2)
    comp = sym[number]
    return comp


# Main UI
while 1 == 1:
    user = user_select()
    computer = comp_select()
    # If statement is able to terminate the program at the users desire
    if user == 'exit':
        print('OK, Thanks for playing')
        break
    else:
        print('You have selected ' + user + ', and the computer has selected ' + computer)
        who_won(user, computer)
        print('Games History: ' + str(history))
        print('')
