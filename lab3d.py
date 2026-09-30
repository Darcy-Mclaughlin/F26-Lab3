#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 30/09/2026
# Purpose: Practice adding and removing elements in list.
# Usage: ./lab3d.py

# Follow the specific instructions given in the README.md file

# - Fill in the required fields in the comment section.
# - Create a variable `mylist` that conatins  first 6 natural numbers.
# - Use the `append()` method and add a new element, number 7 in the variable `mylis`t. 
# - Use the `inser()` method and insert the element 0 at index 0.
# - Use the `pop()' method to remove the element from index 2.
# - Print the variable `mylist`.
# - Add another statement in the script to find the index of the element 6 and print `The element 6 is present at the index ---`

mylist = [1, 2, 3, 4, 5, 6]
mylist.append(7)
mylist.insert(0, 0)
mylist.pop(2)
print(mylist)
print(f"The element 6 is present at the index {mylist.index(6)}")