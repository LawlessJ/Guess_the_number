import random


def guess_the_number():
    a = [i for i in range(1,11)]
    guess = random.randint(1,a[-1])
    print("\nI\'m thinking of a number between {0} and {1}...".format(1,a[-1]))







guess_the_number()
