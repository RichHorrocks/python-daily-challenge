#! /usr/bin/env python

name = raw_input("What's your name? ")
age = raw_input("What's your age? ")
username = raw_input("What's your username? ")

print("Your name is %s, you are %s years old, and your username is %s"
      % (name, age, username))

with open('somefile.txt', 'a') as f:
    f.write("%s, %s, %s\n" % (name, age, username))
