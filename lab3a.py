#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 30/09/2026
# Purpose: Generate a sequence of 20 random values between 0 and 99, store them in a list, print the sequence, sort it, and print the sorted sequence.
# Usage: ./lab3a.py

# Write a Python program that generates a sequence of 20 random values between 0 and 99, 
# stores them in a list, prints the sequence, sorts it, and prints the sorted sequence. Use the list sort method.

import random

randomValues = []

for i in range(20):
    randomValues.append(random.randint(0,99))

randomValues.sort()
print("Sorted sequence:", randomValues)

