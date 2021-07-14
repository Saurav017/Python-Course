
#  Number Guessing Game
import random
NUMBER = random.randint(1, 100)

def check_number(guessed_number):
    if guessed_number == NUMBER:
        return True



print("Welcome to the Number Guessing Game")
print("i am thinking of a number between 1 and 100.")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty_level == 'easy':
    attempts = 10
else:
    attempts = 5

attempts_over = False
while not attempts_over:
    print(f"You have {attempts} remaining to guess the number")

    guess = int(input("Make a guess: "))
    attempts -= 1
    result = check_number(guess)
    if result == True:
        attempts_over = True
        print(f"You Got it ! The answer was {NUMBER}")

    else:
        if attempts <= 0:
            attempts_over = True
            print("You have run out of guesses. You lose!!")
        else:
            if guess > NUMBER:
                print("Too high")
            else:
                print("Too Low")