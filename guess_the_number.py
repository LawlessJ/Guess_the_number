import random
import time


def guess_the_number():
    print("\nLet\'s play guess the number! I\'ll think of a number and you try to guess.")
    valid_opening_choices = ["1","2","3"]
    print("--------------------------------------------------")
    print("\nWhat diffculty do you want? Easy, medium, or hard?")
    while True:
        first_input = input("\nPress 1 for easy. Press 2 for medium. Press 3 for hard.\n")
        if first_input not in valid_opening_choices:
            print("\nPlease enter the numbers 1, 2 or 3.\n(Geez, if this is too hard, the game\'s gonna be tough for you...")
            continue
        if first_input == "1":
            a = [i for i in range(1,11)]
            print("\nEasy peasy it is! Let\'s take it nice and slow.")
            break
        if first_input == "2":
            a = [i for i in range(1,21)]
            print("\nTime for a little challenge!")
            break
        if first_input == "3":
            a = [i for i in range(1,101)]
            print("\nGood luck! Bet you can\'t guess in under 10 tries!")
            break
    guess = random.randint(1,a[-1])
    print("\n...thinking...")
    time.sleep(1)
    print("Ok, got it!")
    print("--------------------------------------------------")
    
    print("\nI\'m thinking of a number between {0} and {1}...".format(1,a[-1]))
    print("\nGuess which number I\'m thinking of!")
    number_of_guesses = 0
    
    while True:
        given_guess = input("What is your guess? Please enter a number between 1 and {0}.\n".format(a[-1]))
        try:
            user_guess = int(given_guess)
        except ValueError:
            print("\nYou didn\'t enter a number!")
            continue
        if user_guess < 1 or user_guess > a[-1]:
            print("\nRemember, the number I am thinking of is between 1 and {0}. Try again!".format(a[-1]))
            number_of_guesses +=1
            continue
        if user_guess - 10 > guess:
            print("\nWAY too high! Try again.")
            continue
        if user_guess > guess:
            print("\nNope! Too high. Try again!")
            number_of_guesses +=1
        if user_guess + 10 < guess:
            print("\nWAY too low! Try again.")
            continue
        if user_guess < guess:
            print("\nNope! Too low. Try again!")
            number_of_guesses +=1
        if user_guess == guess:
            print("\nDing Ding Ding!!! You got it! I was thinking of {0}.".format(guess))
            number_of_guesses +=1
            break
    if number_of_guesses == 1:
        print("You got it on the first try! You must have read my mind.")
    else:
        print("You got the number in {0} tries.".format(number_of_guesses))

    while True:
        valid_answers = ["Y","y","N","n"]
        once_more = input("\nWant to play again? Press Y for yes or N for no.\n")
        if once_more not in valid_answers:
            print("\nYea... let\'s try this again. Press Y for yes (it\'s under your 6 key, genius) or N for no (right over your space bar... I\'ll wait.)")
            continue
        if once_more == "Y" or once_more == "y":
            guess_the_number()
            break
        else:
            print("\nIt\'s been real! See you next time.")
            break
            
    
        




guess_the_number()
