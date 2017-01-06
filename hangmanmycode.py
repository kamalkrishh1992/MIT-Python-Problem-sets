# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 17:28:16 2017

@author: Admin
"""

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True 

# 4. b) Printing out the user's guess
def getGuessedWord(secretWord, lettersGuessed):
    return "".join([letter if letter in lettersGuessed else "_ " for letter in secretWord])

# 4. c) Printing out all available letters
def getAvailableLetters(lettersGuessed):
    return "".join([letter if letter not in lettersGuessed else "" for letter in string.ascii_lowercase])

# 5. Hangman - the game
def hangman(secretWord):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {0:d} letters long".format(len(secretWord)))
    print("You have eight guesses left.")    
    guessesleft=8
    letterGuessed=[]
    while guessesleft>0:
        PrevGuess=getGuessedWord(secretWord,letterGuessed)
        a=input("Enter a letter: ")
        if a in letterGuessed:
            print("Already Guessed letter.Guess again ")
            print("Guesses left:",guessesleft)
            continue
        else:    
            letterGuessed.append(a)
            Guess=getGuessedWord(secretWord,letterGuessed)
            print(Guess)
            if Guess==PrevGuess or Guess=="".join("_ "*len(secretWord)):
                print("Bad Guess",a)
                guessesleft-=1
            else:
                print("Good Guess",a)
                guessesleft-=1

            AL=getAvailableLetters(letterGuessed)
            print(AL)
            print("Guesses left:",guessesleft)
            if isWordGuessed(secretWord, letterGuessed)==True:
                print("Game Over.You found the word")
                break   
    print("You lost....Secret word is:",secretWord)        
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)


