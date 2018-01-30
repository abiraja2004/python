import math
import random

guess = input('enter the guess number ')
g = int(guess)
n = random.randint(0,9)
if g == n:
    print('your guess ',g,' is right')
elif g < n:
    print('your guess ',g,' is less than ',n)
elif g > n:
    print('your guess ',g,' is greater than ',n)