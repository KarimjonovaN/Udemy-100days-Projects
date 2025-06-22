import random
from art import logo, vs
from game_data import data

def game_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Function to check if the user's guess is correct
def is_guess_correct(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"

print(logo)

score = 0
game_on = True

# Start with a random account
account_b = random.choice(data)

while game_on:
    # Move previous B to A, and get a new B
    account_a = account_b
    account_b = random.choice(data)

    # # Make sure A and B are not the same
    # while account_a == account_b:
    #     account_b = random.choice(data)

    print(f"Compare A: {game_data(account_a)}.")
    print(vs)
    print(f"Against B: {game_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower counts
    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]

    correct = is_guess_correct(guess, followers_a, followers_b)
    print("\n" * 20)
    print(logo)

    if correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False

