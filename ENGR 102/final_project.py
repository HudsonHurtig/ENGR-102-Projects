# -*- coding: utf-8 -*-

#import the modules we will use
import requests
import json
import random
import turtle
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True) #initialize colorama

'''FOOTNOTE: If turtle crashes when you try to run it, 
change graphical preference to tfinker'''

def mainMenu(gameChoice = 0): #function for the main menu, parameter is defaulted at zero so it gives directions the first time
    validNums = [1,2,3,4] #list of valid inputs

    if not gameChoice in validNums:
        #intro
        print('')
        print("Welcome to our games! Here are the options:")
        print("1: Tic-Tac-Toe")
        print("2: Wordle")
        print("3: Crossy Road")
        print("4: Quit Program")

        while True: #loops until valid input
            gameSelect = input("Please enter the number corresponding to the game you would like to play (or to quit): ")
            try:
                gameSelect = int(gameSelect)
            except:
                print("Please enter a valid number (1, 2, 3, or 4)")
            else:
                if gameSelect in validNums:
                    break
                else:
                    print("Please enter a valid number (1, 2, 3, or 4)")
    else:
        gameSelect = gameChoice
    
    #calls the appropriate game (or quits)
    if gameSelect == 1:
        print('')
        tic_tac_toe()
    elif gameSelect == 2:
        print('')
        wordle()
    elif gameSelect == 3:
        print('')
        #crossy_road()
        print("crossy_road()")
    else:
        print('')
        print("See you next time!")

def gameEnd(gameId): #function for playing again or quitting to main menu
    while True: #loops until valid input
        playAgain = input('Press 0 if you would like to play again.\nPress 1 if you would like to quit to the main menu.\n')

        try: #try to convert playAgain to an integer
            playAgain = int(playAgain)
        except:
            print("Invalid Input")
        else:
            if playAgain == 0 or playAgain == 1: #if the integer is 0 or 1
                break
            else:
                print("Invalid Input")
        
    if playAgain == 1: #main menu
        mainMenu()
    else: #play again
        mainMenu(gameId) #replay the game

def tic_tac_toe():
    gameId = 1

    #Game instructions, formatted in a list because it looked nicer in the coding, centered and all that.
    instructions = ['Welcome to Tic-Tac-Toe!!',
                    'The rules are the same as regular Tic-Tac-Toe: try to get three in a row, column, or diagonal.',
                    'You choose a location by entering the number of the location in the console.',
                    'Player one goes first and always uses circles.',
                    'The winner will be announced in the console.',
                    'After the game is done, do NOT close the tic-tac-toe window, this causes an error because turtle cannot be restarted after closing.'
                    '']

    for i in instructions:
        print(i)

    #Determines if the User wants to start, gives them time to read the instructions.
    start = ''
    while start != 'Y':
        try:
            start = str(input('Enter Y into the console to start: '))
        except ValueError:
            print('Please input \'Y\' to start the game.')

    #This is for spacing in the console, makes it look nicer.
    print('')
            
    #scr = turtle.getscreen()
    turt = turtle.Turtle()
    turtle.title("Tic-Tac-Toe: ENGR 102 Edition")
    turt.color('Red')

    #This creates the board for the turtle.
    def board(a):
        #draw board
        a.color('black')
        a.speed(10000)
        a.penup()
        a.goto(-400,-100)
        a.pendown()
        a.forward(800)
        
        a.penup()
        a.goto(-400,100)
        a.pendown()
        a.forward(800)
        
        a.penup()
        a.goto(-150.0,301.0)
        a.pendown()
        a.right(90)
        a.forward(600)
        
        a.penup()
        a.goto(150.0,301.0)
        a.pendown()
        a.forward(600)

        #write numbers
        a.penup()
        a.goto(-350,100)
        a.pendown()
        a.write('1', font=('Arial', 12, 'normal'))
        
        a.penup()
        a.goto(-100,100)
        a.pendown()
        a.write('2', font=('Arial', 12, 'normal'))

        a.penup()
        a.goto(200,100)
        a.pendown()
        a.write('3', font=('Arial', 12, 'normal'))

        a.penup()
        a.goto(-350,-100)
        a.pendown()
        a.write('4', font=('Arial', 12, 'normal'))
        
        a.penup()
        a.goto(-100,-100)
        a.pendown()
        a.write('5', font=('Arial', 12, 'normal'))

        a.penup()
        a.goto(200,-100)
        a.pendown()
        a.write('6', font=('Arial', 12, 'normal'))

        a.penup()
        a.goto(-350,-300)
        a.pendown()
        a.write('7', font=('Arial', 12, 'normal'))
        
        a.penup()
        a.goto(-100,-300)
        a.pendown()
        a.write('8', font=('Arial', 12, 'normal'))

        a.penup()
        a.goto(200,-300)
        a.pendown()
        a.write('9', font=('Arial', 12, 'normal'))

        #back to home
        a.penup()
        a.home()
        a.left(180)
        a.pendown()
        a.speed(10)

    #This function returns the turtle from wherever it is to home
    def return_t(a):
        a.penup()
        a.home()
        a.left(180)
        a.pendown()

    '''the next nine functions mark locations on the board
    These locations are so the Cross and Circle functions, to be created later,
    have locations.'''


    def top_left(a):
        a.penup()
        a.goto(-288.0,305.0)
        a.pendown()
        
    def center_left(a):
        a.penup()
        a.goto(-255.0,100.0)
        a.pendown()
        
    def bottom_left(a):
        a.penup()
        a.goto(-255.0,-99.0)
        a.pendown()
        
    def middle_top(a):
        a.penup()
        a.goto(25.0,304.0)
        a.pendown()
            
    def middle(a):
        a.penup()
        a.goto(35,99)
        a.pendown()
        
    def middle_bottom(a):
        a.penup()
        a.goto(40.0,-103.0)
        a.pendown()

    def top_right(a):
        a.penup()
        a.goto(288.0,308.0)
        a.pendown()
        
    def center_right(a):
        a.penup()
        a.goto(265,101.0)
        a.pendown()

    def bottom_right(a):
        a.penup()
        a.goto(266.0,-99.0)
        a.pendown()

    #Creates an X, supposed to be called after a location function.
    def cross(a):
        a.ht()
        a.width(6)
        a.color('blue')
        a.speed(20)
        a.penup()
        a.left(180)
        a.forward(45)
        a.right(180)
        a.pendown()

        a.left(45)
        a.forward(175)
        a.penup()
        a.left(135)
        a.forward(130)
        a.pendown()
        a.left(135)
        a.forward(175)
        a.width(1)


    #Creates a circle, supposed to be called after a location function.
    def circle(a):
        a.ht()
        a.color('red')
        a.fillcolor('red')
        a.begin_fill()
        a.circle(100)
        a.end_fill()
        
    #Calls the location functions to place the turtle.
    def marker(a):
        if selection == 'top_left':
            top_left(a)
        if selection == 'top_center':
            middle_top(a)
        if selection == 'top_right':
            top_right(a)
        if selection == 'mid_left':
            center_left(a)
        if selection == 'mid':
            middle(a)
        if selection == 'mid_right':
            center_right(a)
        if selection == 'bottom_left':
            bottom_left(a)
        if selection == 'bottom_right':
            bottom_right(a)
        if selection == 'bottom_center':
            middle_bottom(a)
            
    #Function that returns the user's selected location.
    def pick():
        while True:
            validLocs = [1,2,3,4,5,6,7,8,9]
            loc = input("Please enter the number of the location you would like (1-9): ")
            try:
                loc = int(loc)
            except:
                print("Invalid Input")
            else:
                if loc in validLocs:
                    break
                else:
                    print("Invalid Input")

        if loc == 1:
            selection = 'top_left'
        elif loc == 2:
            selection = 'top_center'
        elif loc == 3:
            selection = 'top_right'
        elif loc == 4:
            selection = 'mid_left'
        elif loc == 5:
            selection = 'mid'
        elif loc == 6:
            selection = 'mid_right'
        elif loc == 7:
            selection = 'bottom_left'
        elif loc == 8:
            selection = 'bottom_center'
        else:
            selection = 'bottom_right'

        return selection

    #Calls a function to create the board.
    board(turt)

    #This dictionary keeps track of everything on an internal dictionary version of the game.
    text_board = {'top_left': '',
                'top_center': '',
                'top_right': '',
                'mid_left': '',
                'mid': '',
                'mid_right': '',
                'bottom_left': '',
                'bottom_center': '',
                'bottom_right': ''
                }

    #Checks to see if any kind of win condition has been met
    def win_checker(a, win, j):
        if a['top_left'] == a['top_center'] == a['top_right']:
            if a['top_left'] != '':
                win = True

        if a['mid_left'] == a['mid'] == a['mid_right']:
            if a['mid'] != '':
                win = True

        if a['bottom_left'] == a['bottom_center'] == a['bottom_right']:
            if a['bottom_left'] != '':
                win = True         
                
        if a['top_left'] == a['mid_left'] == a['bottom_left']:
            if a['top_left'] != '':
                win = True
        
        if a['top_center'] == a['mid'] == a['bottom_center']:
            if a['mid'] != '':
                win = True
        
        if a['top_right'] == a['mid_right'] == a['bottom_right']:
            if a['mid_right'] != '':
                win = True
        
        if a['top_left'] == a['mid'] == a['bottom_right']:
            if a['mid'] != '':
                win = True
        
        if a['top_right'] == a['mid'] == a['bottom_left']:
            if a['mid'] != '':
                win = True
        elif k == 9 and win == False:
            print('')
            print('It is a tie')
            win = True
            j = 0

        return win

    #defining win as False before the game starts, in order to utilize the win function.
    win = False

    #keeps track of player 1 and player 2, change this value when referring to each turn.
    j = 1

    #Keeps track of turns, only used internally.
    k = 0

    while win == False:
        #Selection calls the pick function and is returned a string from it.
        selection = pick()
        
        turt.speed(10)
        #checks to see if the selection is one of the keys
        if selection in text_board:
            #checks to see if the selection is taken.
            if text_board[selection] == '':
                if j == 1:
                    text_board[selection] = 'O'
                    marker(turt)
                    circle(turt)
                    return_t(turt)
                    j = 2
                    k += 1
                    win = win_checker(text_board, win, j)
                elif j == 2:
                    text_board[selection] = 'X'
                    marker(turt)
                    cross(turt)
                    return_t(turt)
                    j = 1
                    k += 1
                    win = win_checker(text_board, win, j)
            elif text_board[selection] != '':
                print('Choose a valid area.')
    if j == 1:
        print('')
        print('Player 2 Won!')
    if j == 2:
        print('')
        print('Player 1 Won!')

    turt.clear()
    del turt
    #turtle.bye()

    gameEnd(gameId)

def wordle():
    gameId = 2

    response = requests.get('https://www.wordgamedictionary.com/word-lists/5-letter-words/5-letter-words.json') #call API to generate list of five-letter words

    jsonData = json.loads(response.text) #store the response

    validWordList = [] #initialize variable to store a list of five-letter words

    for elem in jsonData: #parse through data and store in list
        validWordList.append(elem['word'])

    answer = random.choice(validWordList) #select a random word from that list as the answer

    guessCount = 0 #initialize variable to store number of guesses
    bar = Back.BLACK + '|' #helps condense text formatting

    def letterInList(letter, list):
        for elem in list:
            if letter in elem:
                return True

    def guess(): #defines a function that will take in a guess and check how 'good' it is
        outputList = ['','','','',''] #initialize list to store each letter in the guess
        correctCount = 0 #initialize variable to count how many fully correct letters there are

        while True: #loops until the guess is valid
            guess = input("Please guess a 5-letter word: ") #stores the user's input
            if guess.lower() in validWordList: #checks that the input is a valid five-letter word
                guess = guess.lower()
                break
            else: #loop if input is invalid
                print("Invalid Input")

        for i in range(len(guess)): #iterate through each letter in the guess
            
            if guess[i] == answer[i]: #if the letter is in the right spot
                correctCount += 1 #add one to correctCount
                outputList[i] = Back.GREEN + f' {guess[i].upper()} ' #green background
            elif guess[i] in answer and ((not letterInList(guess[i].upper(), outputList)) or (answer.count(guess[i].lower()) > 1)): #if the letter is in the answer but not in that spot
                outputList[i] = Back.YELLOW + f' {guess[i].upper()} ' #yellow background
            else: #if the letter is not in the answer
                outputList[i] = Back.BLACK + f' {guess[i].upper()} ' #black background

        return outputList, correctCount #return the output list and the number of fully correct letters

    #intro
    print("Welcome to Wordle! Try to guess the 5-letter word in six tries!")
    print('')
    print("RULES")
    print("For each guess, if a letter is not highlighted then it is NOT in the answer.")
    print("If the letter is highlighted yellow then the letter is in the answer, but not in that location.")
    print("If the letter is highlighted green then the letter is in the answer in that exact spot.")
    print('')

    #six guesses
    for i in range(6):

        if i == 0: #first guess, each of the subsequent guesses follow the same method
            outputList, correctCount = guess() #call and store function output
            guessCount += 1 #add one to guessCount

            guessOne = bar + outputList[0] + bar + outputList[1] + bar + outputList[2] + bar + outputList[3] + bar + outputList[4] + bar #output

            #print board
            print('')
            print('---------------------')
            print(guessOne)
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('')

            if correctCount == 5: #if user won
                break

        if i == 1: #second guess
            outputList, correctCount = guess()
            guessCount += 1

            guessTwo = bar + outputList[0] + bar + outputList[1] + bar + outputList[2] + bar + outputList[3] + bar + outputList[4] + bar

            print('')
            print('---------------------')
            print(guessOne)
            print('---------------------')
            print(guessTwo)
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('')

            if correctCount == 5:
                break

        if i == 2: #third guess
            outputList, correctCount = guess()
            guessCount += 1

            guessThree = bar + outputList[0] + bar + outputList[1] + bar + outputList[2] + bar + outputList[3] + bar + outputList[4] + bar

            print('')
            print('---------------------')
            print(guessOne)
            print('---------------------')
            print(guessTwo)
            print('---------------------')
            print(guessThree)
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('')

            if correctCount == 5:
                break

        if i == 3: #fourth guess
            outputList, correctCount = guess()
            guessCount += 1

            guessFour = bar + outputList[0] + bar + outputList[1] + bar + outputList[2] + bar + outputList[3] + bar + outputList[4] + bar

            print('')
            print('---------------------')
            print(guessOne)
            print('---------------------')
            print(guessTwo)
            print('---------------------')
            print(guessThree)
            print('---------------------')
            print(guessFour)
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('')

            if correctCount == 5:
                break

        if i == 4: #fifth guess
            outputList, correctCount = guess()
            guessCount += 1

            guessFive = bar + outputList[0] + bar + outputList[1] + bar + outputList[2] + bar + outputList[3] + bar + outputList[4] + bar

            print('')
            print('---------------------')
            print(guessOne)
            print('---------------------')
            print(guessTwo)
            print('---------------------')
            print(guessThree)
            print('---------------------')
            print(guessFour)
            print('---------------------')
            print(guessFive)
            print('---------------------')
            print('| _ | _ | _ | _ | _ |')
            print('---------------------')
            print('')

            if correctCount == 5:
                break

        if i == 5: #sixth guess
            outputList, correctCount = guess()
            guessCount += 1

            guessSix = bar + outputList[0] + bar + outputList[1] + bar + outputList[2] + bar + outputList[3] + bar + outputList[4] + bar

            print('')
            print('---------------------')
            print(guessOne)
            print('---------------------')
            print(guessTwo)
            print('---------------------')
            print(guessThree)
            print('---------------------')
            print(guessFour)
            print('---------------------')
            print(guessFive)
            print('---------------------')
            print(guessSix)
            print('---------------------')
            print('')

            if correctCount == 5:
                break

    if correctCount == 5: #if user won
        if guessCount == 1: #output
            print(f'You won in {guessCount} guess!') #single guess
        else:
            print(f'You won in {guessCount} guesses!') #multiple guesses
    else: #if user lost
        print(f'You lose! The word was: {answer.upper()}.') #reveal answer

    gameEnd(gameId)

mainMenu()