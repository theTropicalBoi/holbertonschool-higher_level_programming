#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
last_digit_string = "Last digit of " + str(number) + " is " + str(last_digit)
if last_digit > 5:
    print(f"{last_digit_string} and is greater than 5")
elif last_digit == 0:
    print(f"{last_digit_string} and is 0")
else:
    print(f"{last_digit_string} and is less than 6 and not 0")
