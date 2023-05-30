import random
from words import *

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
alphabet = vowels + consonents

letters = []
solutions = []

def get_user_letters():

    letters_a = int(input('how many letters would you like? '))
    vowels_a = int(input('how many vowels would you like? '))
    lettersToGet_a = letters_a - vowels_a
    for i in range(vowels_a):
        letters.append(vowels[random.randint(0,5)])

    for i in range(lettersToGet_a):
        letters.append(consonents[random.randint(0,19)])

    print(letters)


def check_word(word, letters=list):
    word = list(word)
    count = word.__len__()
    for letter in word:
        if word.__len__() < 3:
            return
        if letter in letters:
            letters.remove(letter)
            count -= 1
        elif letter == ' ':
            count -= 1
        else:
            return
           
    return count

trialwords = get_words()

for i in trialwords:
    count = check_word(i, ['p', 's', 'a', 'c', 'b', 't', 'r', 'a', 'n', 's', 'e', 'e'])
    if count == 0:
        solutions.append(i)

print(solutions)
