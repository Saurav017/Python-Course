
import random
import art
from game_data import data
import os
clear = lambda: os.system('cls')

def random_account():
    """Get a random account for the dictionary"""
    return random.choice(data)


def printable_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

# Ask user for a guess.
def check_guess(guess,followerA, followerB):
    """Checks followers against user's guess
      and returns True if they got it right.
      Or False if they got it wrong."""
    if followerA > followerB:
        return guess == "a"
    else:
        return guess == "b"

is_game_continue = True
score = 0

account_a = random_account()
account_b = random_account()
if account_a == account_b:
    account_b = random_account()
while is_game_continue:
    print(art.logo)

    final_score = score
    print(f"Compare A : {printable_data(account_a)}")
    print(art.vs)
    print(f"Against B: {printable_data(account_b)}")
    guess = input("Who has more followers? 'A' of 'B' :").lower()
    result = check_guess(guess, account_a["follower_count"], account_b["follower_count"])
    if result == True:
        score +=1
        print(f"You are right! Your current score is {score}.")
        account_a = account_b
        account_b = random_account()
    else:
        is_game_continue = False
        print(f"Sorry that's wrong! Final Score = {final_score}")
