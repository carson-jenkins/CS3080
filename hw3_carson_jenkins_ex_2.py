# -*- coding: utf-8 -*-
"""hw3_carson_jenkins_ex_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wyul34ZmgNPhM7TdBaqvL-HRE3ZoLczi
"""

'''
Homework 3, Exercise 2
Carson Jenkins
02/23/23
This program takes in a string and counts 
the number of characters in the given string.
'''

def key(input):
  dictionary = {}
  counter = 1
  for i in range(len(input)):
    for j in range(len(input)):
      try:
        if input[i] == input[j]:
          counter = counter + 1
      except:
        pass
    dictionary[input[i]] = counter-1
    counter = 1
  return dictionary

dictionary = key('The quick brown fox jumps over the lazy dog.')

import pprint
pprint.pprint(dictionary)