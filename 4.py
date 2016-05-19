#!/usr/bin/env python

# You're challenge for today is to create a 
# random password generator!
# For extra credit, allow the user to specify 
# the amount of passwords to generate.
# For even more extra credit, allow the user to 
# specify the length of the strings he wants to generate!

import random
import string

password_len = int(raw_input("How long should the passwords be? "))
for i in range(int(raw_input("How many passwords should I generate? "))):
    print("".join(random.sample(string.ascii_letters, password_len)))
