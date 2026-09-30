#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 30/09/2026
# Purpose: Practice using list methods.
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file

# - Create an empty list
#- Create a while loop that ends when your list size reaches 6
# - Add numbers to your list using input
# - Multiply the numbers by 10
# - Print out the list in reverse order

list = []
while len(list) < 6:
    num  = int(input("Enter a number: "))
    list.append(num * 10)
list.reverse()
print (list)