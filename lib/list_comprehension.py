#!/usr/bin/env python3

def return_evens(num_list):
    #Returns a list of even numbers from a list of integers.
    evens = [num for num in num_list if num % 2 == 0]
    return evens
    

def make_exclamation(sentence_list):
    #Returns a list of sentences with an exclamation point at the end
    exclamations = [sentence + "!" for sentence in sentence_list]
    return exclamations