#!/usr/bin/env python

# Welcome to cipher day!
# write a program that can encrypt texts with an 
# alphabetical caesar cipher. This cipher can ignore numbers, 
# symbols, and whitespace.
# For extra credit, add a "decrypt" function to your program!

# Single-liner for brevity.
print(raw_input("Enter the string to encode: ").encode('rot13'))

# Then...
# Note that in the case of rot13, decoding is the same as
# encoding twice, i.e. rot13(foo) == rot13(rot13(foo))
encode = raw_input("Would you like to (e)ncode or (d)ecode? ")
user_str = raw_input("Enter the string to (d)encode: ")
if encode == "e":
    print(user_str.encode('rot13'))
elif encode == "d":
    print(user_str.decode('rot13'))
