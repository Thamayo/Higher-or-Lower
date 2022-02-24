# Coded by ThaMayo 
# Higher or Lower Guessing Game

from art import logo, vs
from game_data import data
import random
from replit import clear

print(logo)
score = 0
gameContinue = True
randomName2 = random.choice(data)

def formatData(account):
    """Format the account data into printable format."""
    name1 = account["name"]
    description1 = account["description"]
    country1 = account["country"]
    return(f"{name1}, a {description1} from {country1}")

def checkAnswer(guess, followers1, followers2):
    """Take the user guess and follower counts and returns if they got it right."""
    if followers1 > followers2:
        return guess == "a"
    else:
        return guess == "b"

while gameContinue:
    randomName1 = randomName2
    randomName2 = random.choice(data)
    while randomName1 == randomName2:
        randomName2 = random.choice(data)
    
    print(f"Compare A: {formatData(randomName1)}.")
    print(vs)
    print(f"Against B: {formatData(randomName2)}.")
    
    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()
    
    followers1 = randomName1["follower_count"]
    followers2 = randomName2["follower_count"]
    is_correct = checkAnswer(guess, followers1, followers2)

    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}\n")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        gameContinue = False