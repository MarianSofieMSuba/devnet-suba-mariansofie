"""
Module 2 — Activity: File Sorting with os and shutil
Student: Marian Sofie M. Suba
Date: 9/26/26

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]

Its a simple file sorting that lets you sort a specifed user-input folder path
it is only limited for these specific file type (JPG,PNG and PDF)
the script would run into a for loop to:
check the file type --> creates a new folder for that specified file type --> moves the selected file type that matches the type of folder
but if there's already an existing folder
check the file type --> moves the selected file type that matches the type of folder
then its all done

============================================
KEY VOCABULARY
============================================
- os module: it provides commands to interact with the operating system
- shutil module: it provides commands to manipulate files and directories like (copy, move and delete)
- file path: location of the file
- directory: folder to manage files
- os.listdir: creates a folder
- os.mkdir: shows the files and folders inside of a folder
- os.path: lets you manipulate paths of a file and folder
> .join: lets you combine things like combining a file inside a folder
> .isfile: checks what file type it is
> .exists: checks if the file or folder is already there
- shutil.move: moves a file or folder from one location to another


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

folder_searcher = input("Enter the folder path that you want to sort: ")

for filename in os.listdir(folder_searcher):
    file_path = os.path.join(folder_searcher, filename)

    if os.path.isfile(file_path):

        if ".jpg" in filename:
            new_folder = os.path.join(folder_searcher, "JPG Files")

        elif ".png" in filename:
            new_folder = os.path.join(folder_searcher, "PNG Files")

        elif ".pdf" in filename:
            new_folder = os.path.join(folder_searcher, "PDF Files")

        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

        shutil.move(file_path, os.path.join(new_folder, filename))

print("All Done")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]

The moment I tried to test with input, I had some small errors specifically due to python considering (/) a string so I had to use (//).
I had trouble figuring out how to use os.path only for me to realized there can be different specified syntaxes
my first goal was if it can detect a file and so I used os.path.isfile
then after figuring how shutil.move works I made an if and elif statement
each time I run it, I kept getting an error that it could not find a specified path
I thought shutil.move was the issue until I solved the problem by making the folder checker into a "if not"
previously it was an "elif"

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
