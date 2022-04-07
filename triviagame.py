#!/usr/env python3

from questionbank import gameQuestions
from os import system, name

def answer_check(question, player_answer, score):

    if gameQuestions[question]['answer'].lower() == player_answer.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!\n")
        input("Press enter key to continue...")
        clear()
        return True
    else:
        print(f"Wrong Answer :( \n Try again...")
        input("Press enter key to continue...")
        clear()
        return False


def intro_message():

    print("Welcome to the trivia questions! \n")
    print("There are a total of 6 questions, if you're in a pickle and cant figure it out. You can skip a question anytime by typing 'skip'\n")
    input("Press the enter key to get started ;) ") 
    clear()
    return True


def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# starts the game
intro_message()

while True:
    score = 0
    for question in gameQuestions:
        while score >= 0:
            print(gameQuestions[question]['question'])
            player_answer = input("Enter Answer (To move to the next question, type 'skip') : ")
            if player_answer == "skip":
                clear()
                break
            player_answer_check = answer_check(question, player_answer, score)
            if player_answer_check:
                score += 1
                break
    break
    
clear()
print(f"Your final score is {score}!\n\n")
print("Thanks for playing! 💜")