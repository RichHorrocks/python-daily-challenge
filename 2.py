#! /usr/bin/env python

# Challenge is to make something useful.
# I'm making a script to calculate compound interest, 
# which can be adjusted for different compounding periods.

pv = int(raw_input("What is the starting investment? "))
i = int(raw_input("What is the interest rate %? "))
cp = int(raw_input("How many times per year is the interest calculated? "))
n = int(raw_input("How many years are we talking about? "))

# Apply the formula:
#  future value = present value * (1 + i)**n

print("The future value is: %.2f" % 
      (pv * ((1 + (float(i) / 100)) ** (cp * n))))
