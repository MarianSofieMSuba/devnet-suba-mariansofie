"""
Module 2 — Lesson 1: Variables & Data Types
Student: Marian Sofie M. Suba
Date: 9/27/26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================

Variables are containers that stores any information whether its a text or a number
They carry the stored information so that it can be used when its needed

Data type are the ones that specify what type of information a variable contains
it will tell you whether if this one is a text, number or a group of text and numbers

============================================
KEY VOCABULARY
============================================
- variable: the containers of information
- data type: specifies the type of data
- int: specifies if the information is a number
- float: specifies if the information has a decimal
- string: specifies if the information is a text
- boolean: specifies whether the information is true or false
- list: is a collection of values that can modify
- tuple: is a collection of values that you can't modify
- type(): checks what data type the value is


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

thisIsAVariable = "I am a string"
thisIsAIntVariable = 4
thisIsAFloatVariable = 4.3
isThisBoolean = True
iAmAList = [1,2,3,]
iAmATuple = (1,2,3)

print(type(thisIsAVariable))
print(type(thisIsAIntVariable))
print(type(thisIsAFloatVariable))
print(type(isThisBoolean))
print(type(iAmAList))
print(type(iAmATuple))

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

Lists and Tuples, they look a bit similar in terms of functionality to me
I was more used to handling arrays from Java and thought this would do the same thing
even if they have different symbols from one and another but I was wrong
it doesn't work similarily close to Java arrays and they're completely their own thing
because lists and tuples can mix other datatypes while arrays stays with one datatype
and I also keep thinking they're "arrays" from time to time even though that is not
the correct syntax for python

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
