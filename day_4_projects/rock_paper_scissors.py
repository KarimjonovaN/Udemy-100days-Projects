import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#player choice
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
if player_choice == "0":
    print(rock)
elif player_choice == "1":
    print(paper)
else:
    print(scissors)

#computer choice
computer = [ rock, paper, scissors]
computer_choice = random.choice(computer)
print(f"Computer Choose: {computer_choice}")

#result
if player_choice == "0" and computer_choice == rock:
    print("It's a draw!")
elif player_choice == "0" and computer_choice == paper:
    print("You lose!")
elif player_choice == "0" and  computer_choice == scissors:
    print("You win!")

elif player_choice == "1" and computer_choice == rock:
    print("You win!")
elif player_choice == "1" and computer_choice == paper:
    print("It's a draw!")
elif player_choice == "1" and computer_choice == scissors:
    print("You lose!")

elif player_choice == "2" and computer_choice == rock:
    print("You lose!")
elif player_choice == "2" and computer_choice == paper:
    print("You win!")
elif player_choice == "2" and computer_choice == scissors:
    print("It's a draw!")
