# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:57:10 2020

@author: maryn
"""

import os

questions = []
scientists = []
players = []

# WELCOME WORDS

def Welcome():
    Welcome.name = input("What is your name?")
    print("WELCOME TO THE WORLD OF SCIENCES!\nLET US CHECK IF YOU COULD STILL REMEMBER THE PEOPLE BEHIND SCIENCE!")
    print('\nLet us see how much you remember about the greatest Scientist in the history!\nA little bit of your school memories will be tested.')
    print('\nBut before that let me know a little information about yourself, so I would know how do I call you.\n')
    print("Hello, " + Welcome.name.title() + "! " + "Are you ready to take the exam? If so, then, let's begin!\n")
    
#To save questions and answers on a text file
def save_question(questions,scientists):
    with open("questions.txt","w") as file:
        for question in questions:
            file.write('%s\n' % question)
    with open("scientists.txt","w") as file:
        for scientist in scientists:
            file.write('%s\n' % scientist)

#Original questions and answers(scientists)
def QUIZ():
    questions = ['I am the Father of Mathematics.', 
                 'I am the Father of Geometry.', 
                 'I am the Father of Biology.', 
                 'I am the first recorded Mathematician who used pi as Mathematical symbol.',
                 'The Cartesian Plane is named after me, who am I?',
                 'One of my greatest constributions in Mathematics is the famous Pythagorean Theorem.',
                 'He is known as the Father of Modern Physics.',
                 'I am well-known for I formulated the Law of Gravitation and the Three Laws of Motion.',
                 'I established zero as a number and defined its mathematical properties; discovered the formula for solving quadratic equations.',
                 'I am the author of one of the most famous books in history, On the Origin of Species.']
    
    scientists = ['Archimedes','Euclid','Aristotle','William Jones','Rene Descartes','Pythagoras','Albert Einstein','Isaac Newton','Brahmagupta','Charles Darwin']
    
    save_question(questions,scientists)
    
#Putting file content into the list
def initialize_QUIZ():
    with open("questions.txt") as file:
        for question in file: 
            question = question.strip()
            questions.append(question)
    with open("scientists.txt") as file:
        for scientist in file: 
            scientist = scientist.strip()
            scientists.append(scientist)

#Preparing questions, choices and answers for the QUIZ
def load_QUIZ():
    if os.path.exists('questions.txt'):
        initialize_QUIZ()
    else:
        QUIZ()
        initialize_QUIZ()
        
#Display original questions and answers(scientists)
def display_QUIZ():
    x = len(questions) 
    i = 0

    print ("\n")
    while i < x:
      print(str(i+1) + ". " + questions[i])
      print("SCIENTIST: {0}\n".format(scientists[i]))
      i += 1
    
#Play your quiz
def play_QUIZ():
    x = len(questions)
    i = 0
    score = 0

    while i < x:
        print(str(i+1) + "." + questions[i])
        ask = input("Please enter your answer:")
        if ask.title() == scientists[i]:
            print("\nVery Good!\n")
            score = score + 1
        else:
            print("\nSorry you're wrong!\n")    
        i += 1

    print("Your Score is {0}".format(score))

    #Record Players
    P1 = Player(Welcome.name,score)
    players.append(P1)
    save_player(players)

#Change item/s
def change_question():

    display_QUIZ()

    number=input("Enter item number to update or 0 to add new question: ")
    new_question=input("Enter New question: ")
    new_scientists=input("Enter Answer: ")

    if number == '0':
        questions.append(new_question)
        scientists.append(new_scientists)
    else:
        questions[int(number)] = new_question
        scientists[int(number)] = new_scientists

    save_question(questions,scientists) 

    display_QUIZ()

    print("You have sucessfully update your QUIZ!")

#Deleting question/s

def delete_question():

    display_QUIZ()

    rem = input("Enter item number to delete: ")

    i = int(rem)

    if i == 0:
        print("Invalid Question Number")
    else:
        questions.pop(i)
        scientists.pop(i)
        print("Question {0} has been deleted".format(i))
    
    save_question(questions,scientists)
    display_QUIZ()

#Players
class Player ():
   def __init__(self,name,score):
        self.name = name
        self.score = score  

#Save Players into file
def save_player(players):
  with open("players.txt","w") as file:
        for player in players:
            file.write('%s\n' % "Player Name:{0} | Score:{1}\n".format(player.name,player.score))

#Game Start Here

load_QUIZ()
print('\n')

while True:
    
    QUIZ = input("\nWELCOME \n[1] Play Game \n[2] Update/Add Question \n[3] Delete Question \n[0] Exit \nSelect: ")
    
    if QUIZ == '1':
        os.system('cls')
        Welcome()
        play_QUIZ()
        continue
    elif QUIZ == '2':
        os.system('cls')
        change_question()
        continue
    elif QUIZ == '3':
        os.system('cls')
        delete_question()
        continue
    elif QUIZ == '0':
        break

#Display Game Result
with open("players.txt","r") as file1: 
    text = file1.read() 
    print("\nGame Results:")
    print(text)
    
def main():
     file = open("./auth.txt")
     lines = file.readlines()
     file.close()
     

print('\nThank you for playing!')
