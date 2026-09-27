"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Marian Sofie M. Suba
Date: 9/27/26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

If-ElseIf-Else are basically conditions that handles the way how the flow is going to work
they're the ones that does the decision-making
it normally goes like this:

if you want to take this first path, go to this path
else if you changed your mind, take the second path
else, you don't want to take both of those path

============================================
KEY VOCABULARY
============================================
- condition:
- if / elif / else: decision-making conditions that helps control the flow
- comparison operator: they check whether its greater than, equal to and less than. there can be more
- boolean expression: they check if the value is true or false
- logical operator: they combine more than one conditional statements by using AND, OR and NOT
- if [thing] in [variable]: it checks for the index of a tuple, lists and arrays (might be more) if its true or false

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

whatIf_ImIndecisive = "1"

if whatIf_ImIndecisive == 1:
    print("I will choose one")

elif whatIf_ImIndecisive == 2:
    print("I will choose two")

else:
    print("I don't know")


iNeedToCompare = 80

if iNeedToCompare > 75:
    print(f"I am greater than 75! because I am {iNeedToCompare}")
elif iNeedToCompare < 74:
    print(f"I am less than 74.. because I am {iNeedToCompare}")
elif iNeedToCompare == 100:
    print(f"I am equal to 100! because I am {iNeedToCompare}")
else:
    print("Wrong input?")

trueOrfalse = True

if trueOrfalse == True:
    print(trueOrfalse)
elif trueOrfalse == False:
    print(trueOrfalse)
else:
    print("decide, true or false")    

whoami = "name"
age = 100

if whoami == "name":
    print(f"Hello {whoami}!")

    if age > 12 and age < 18:
        print("you are a teen")
    elif age < 13:
        print("you are a child")
    elif age > 17 and age < 100:
        print("you are an adult")
    else:
        print(f"are you sure that you're {age}?")

else:
    print("What even is your name")

light = True

if light == True:
    print("Lights on!")
else:
    print("Lights off!")
    

my_bag = ["pencil","eraser","paper"]

if "paper" in my_bag:
    print(f"you have {my_bag[2]}")
else:
    print("where is paper")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

The only thing that's confusing is doing the nested if-elseif-else
but that depends more on how you format an if-elseif-else

Some of the things I want to avoid is miss using greater than and less than
I would often switch them up especially once logical operators comes in
this also includes once I also combine with equals to

And also mistaking the syntax of logical operators by using the Java version instead of Python

Mistakes I sometimes do is putting the variables inside a conditional statement wrong
which would cause an error or it prints out the wrong output


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
