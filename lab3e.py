#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 30/09/2026
# Purpose: Practice using list methods.
# Usage: ./lab3e.py

# Follow the specific instructions given in the README.md file
#- Fill in the required fields in the comment section.
#- Create a list variable called `students`. Add the following names in this list: Ama, Elina, Maija, Daniel, Ibrahim.
#- Next change the element at index 1 and update this element with "Maggy".
#- Now use a` for loop` and iterate over this list and print each element on a separate line. 

students = ["Ama", "Elina", "Maija", "Daniel", "Ibrahim"]
students[1] = "Maggy"
for student in students:
    print(student)
