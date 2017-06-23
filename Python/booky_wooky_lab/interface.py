import math
import re
from collections import Counter
import pandas as pd
import nltk
from nltk.corpus import cmudict
import string

ari_scale = {

    1: {'ages': '5-6', 'grade_level': 'Kindergarten'},

    2: {'ages': '6-7', 'grade_level': '1st Grade'},

    3: {'ages': '7-8', 'grade_level': '2nd Grade'},

    4: {'ages': '8-9', 'grade_level': '3rd Grade'},

    5: {'ages': '9-10', 'grade_level': '4th Grade'},

    6: {'ages': '10-11', 'grade_level': '5th Grade'},

    7: {'ages': '11-12', 'grade_level': '6th Grade'},

    8: {'ages': '12-13', 'grade_level': '7th Grade'},

    9: {'ages': '13-14', 'grade_level': '8th Grade'},

    10: {'ages': '14-15', 'grade_level': '9th Grade'},

    11: {'ages': '15-16', 'grade_level': '10th Grade'},

    12: {'ages': '16-17', 'grade_level': '11th Grade'},

    13: {'ages': '17-18', 'grade_level': '12th Grade'},

    14: {'ages': '18-22', 'grade_level': 'College'}

}


def count_words(file):
    book = open_file(file)
    num_words = 0

    for word in book.read().split():
        num_words += 1

    return num_words


def count_characters(file):
    file.seek(0)

    number_chars = 0

    blanks = 0

    for line in file:

        number_chars += len(line)

        for char in line:

            if char == ' ' or char == '\n':
                blanks += 1

    return number_chars - blanks


def count_sentences(book):
    with open(book, 'r') as myfile:
        booky = myfile.read().lower()

    count = nltk.sent_tokenize(booky)

    return len(count)


def open_file(text):
    return open(text, 'r', encoding="utf-8-sig")

    # print(type(text))


def calculate_ari(x, y, z):
    return 4.71 * x / y + 0.5 * y / z - 21.43


def longest_words(book):
    """Returns a list of the 10 longest words"""

    unique_dict = unique_words(book)

    word_array = pd.DataFrame(list(unique_dict.items()), columns=['Word', 'Occurence'])
    word_array['length'] = word_array['Word'].map(lambda x: len(x))

    sorted = word_array.sort_values('length', ascending=False)
    max_value = max(sorted['length'])

    longest_list = word_array.loc[word_array['length'] == max_value]

    return longest_list




def shortest_words(book):
    # TODO
    unique_dict = unique_words(book)

    word_array = pd.DataFrame(list(unique_dict.items()), columns=['Word', 'Occurence'])
    word_array['length'] = word_array['Word'].map(lambda x: len(x))

    sorted = word_array.sort_values('length', ascending=False)
    min_value = min(sorted['length'])

    longest_list = word_array.loc[word_array['length'] == min_value]

    return longest_list


def unique_words(book):
    with  open(book, 'r') as myfile:
        booky = myfile.read().lower()

    seperate_into_words = re.findall(r'\b\w+\b(?![^<]*>)', booky)

    unique = Counter(seperate_into_words)
    return unique


def unique_word_count(book):
    """Counts the number of unique words in bookx returns integer count"""

    count = unique_words(book)

    return len(count)


def rarest_words(book):
    """Returns list of top 10 rarest words"""
    unique_dict = unique_words(book)

    count_list = []
    unsorted = [(v, k) for k, v in unique_dict.items()]

    smallest_num = min(unsorted)
    word_array = pd.DataFrame(list(unique_dict.items()), columns=['Word', 'Occurence'])

    for index, row in word_array.iterrows():
        if row['Occurence'] == smallest_num[0]:
            count_list.append(row['Word'])

    return count_list


def word_frequency(book):
    """Returns count of user input word."""
    unique_dict = unique_words(book)

    word_array = pd.DataFrame(list(unique_dict.items()), columns=['Word', 'Occurence'])

    return word_array




def average_length_sentence(file):  # feels bad man
    sentences = count_sentences(file)
    words = count_words(file)

    return words/sentences


def sentence_tuples(book):
    with open(book, 'r') as myfile:
        booky = myfile.read().lower()

    sentences = nltk.sent_tokenize(booky)

    sentences_tuple_list = []

    for sentence_element in sentences:
        num_words = 0

        words_in_sentences = nltk.word_tokenize(sentence_element)
        sentences_tuple_list.append((len(words_in_sentences), sentence_element))

    return sentences_tuple_list

def minimum_sentence_length(book):
    '''test'''
    sentence_tuple_list = sentence_tuples(book)
    minimum = min(sentence_tuple_list)

    return minimum[0]


def max_sentence_length(book):
    '''test'''
    sentence_tuple_list = sentence_tuples(book)
    maximum = max(sentence_tuple_list)

    return maximum[0]

def mimic():
    # TODO """TBD"""
    '''test'''


def count_syllables(book):
    """"Returns total number of syllables in book."""
    d = dict(cmudict.entries())
    with  open(book, 'r') as myfile:
        booky = myfile.read().lower()
    tokenized_book = nltk.word_tokenize(booky)

    count = 0
    for word in tokenized_book:
        count += ( nsly(word, d))

    return count

def nsly(word, d):
    if word in d:
        return len([ph for ph in d[word] if ph.strip(string.ascii_letters)])
    else:
        return 0



def lexical_density(book):
    """Returns lexical density."""
    unique = len(unique_words(book))
    with  open(book, 'r') as myfile:
        booky = myfile.read().lower()
    total =  len(re.findall(r'\b\w+\b(?![^<]*>)', booky))

    return unique/total