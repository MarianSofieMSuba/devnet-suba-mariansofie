"""
Module 2 — Lesson 3: Loops & Lists
Student: Marian Sofie M. Suba
Date: 10/3/26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================

Loops are basically when you want to repeat something,
it can repeat itself for as long as how you want it to be,
whether if its forever or only stops at a specific condition.

Lists can store multiple pieces of data inside a single container,
like a basket containing with different kinds of fruits.

============================================
KEY VOCABULARY
============================================
- list: stores multiple data inside a single variable
- for loop: its only repeats once
- while loop: keeps repeating unless specified
- index: the position of an item
- iteration: a repitation of a loop
- match: checks if the value matches the following cases
- input: lets user input any information
- break: stops the loop
- append(): adds something to the list
- remove(): removes something to the list

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

my_bag = []

while True:

    pick = int(input("What will you do?: \n[1]Put something in the bag\n[2]Take something out of the bag\n[3]Look inside the bag\n[4]I think I'm okay\n-----------------------------\n"))

    match pick:

        case 1:
            put_inside = input("What item will you put inside the bag?: \n-----------------------------\n")
            my_bag.append(put_inside)

        case 2:
            if my_bag:
                take_out = input("What item will you take out?: \n-----------------------------\n")

                if take_out in my_bag:
                    my_bag.remove(take_out)

                else:
                    print("There's no item like that\n-----------------------------\n")

            else:
                print("There's nothing in here\n-----------------------------\n")

        case 3:

            if my_bag:
                print(my_bag)
            else:
                print("There's nothing in here\n-----------------------------\n")

        case 4:
            print("Ready to go!\n-----------------------------\n")
            
            break



adopt_a_cat = ["Charlez","Joshua","Michelle"]

print("These are the cats")

for cat in adopt_a_cat:
        print(cat)

i_want_this = input("Pick a cat that you want: \n")

if i_want_this in adopt_a_cat:
        print(f"You got {i_want_this}")
        adopt_a_cat.remove(i_want_this)
else:
        print("That cat doesn't exist")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================

Not using the correct formatting of how a while loop works,
switching places the input and datatype which equals to why match or even if-else can't detect my input,
leaving the parentheses for .append and .remove empty instead of putting,
getting confused from the use of index since I got used to seeing [i] instead of a renamed version of it ex. [cat]
which sometimes viewed as a variable to me

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
