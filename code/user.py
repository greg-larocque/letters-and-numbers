import random
from words import *

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
alphabet = vowels + consonents

letters = []


def get_user_letters():

    letters_a = int(input('how many letters would you like? '))
    vowels_a = int(input('how many vowels would you like? '))
    lettersToGet_a = letters_a - vowels_a
    for i in range(vowels_a):
        letters.append(vowels[random.randint(0,5)])

    for i in range(lettersToGet_a):
        letters.append(consonents[random.randint(0,19)])

    print(letters)



def check_word_dict(words=dict, letters=list):
    solutions = []
    for i in words:
        count = 0
        target = words[i].__len__()
        for letter in letters:
            if letter in words[i]:
                count += 1
                words[i].remove(letter)
            if count == target and target >=3:
                solutions.append(i)
                break
    print(solutions)
    return solutions

trialwords = get_words()
