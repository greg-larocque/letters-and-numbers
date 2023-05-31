import requests
import re

url = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

words = []
words_dict = {}

def get_words():
    with open('english_words.txt', 'r') as file:
        for line in file:
            raw = list(line)
            raw = raw[:-1]
            raw = str(raw)
            word = re.sub(r'[^a-zA-Z]', '', raw)
            words.append(word)
    
    return words


def get_words_dictionary():
    with open('english_words.txt', 'r') as file:
        for line in file:
            raw = list(line)
            raw = raw[:-1]
            value = raw
            raw = str(raw)        
            word = re.sub(r'[^a-zA-Z]', '', raw)
            words_dict[word] = value

    return words_dict


def get_definition(word):
    data = requests.get(url.format(word)).json()
    definition = (data[0]['meanings'][0]['definitions'][0]['definition'])
    print(definition)
