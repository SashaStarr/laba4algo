import csv
from typing import List


def longest_chain(list_words: List[str]) -> int:
    list_words.sort(key=lambda x: len(x))
    words_dictionary = {}
    max_chain = 0
    for word in list_words:
        iterator = 0
        max_word = 1
        while iterator < len(word):
            next_word = word[:iterator] + word[iterator + 1:]
            iterator = iterator + 1
            if next_word in words_dictionary:
                max_word = max(max_word, words_dictionary[next_word] + 1)
        words_dictionary[word] = max_word
        max_chain = max(max_chain, max_word)
    return max_chain


def read_csv_file():
    words = []
    with open("wchain.in") as input_file:
        csv_reader = csv.reader(input_file, delimiter=",")
        next(csv_reader)
        for line in csv_reader:
            words.append(line[0])
        print(words)
    return words
