print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_right= input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if left_right == "right" or left_right == "Right":
    print("You fall into a hole. Game over!")
elif left_right == "left" and "Left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    swim_wait = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if swim_wait == "swim" or swim_wait == "Swim":
        print("You get attacked by an angry trout. Game Over.")
    elif swim_wait == "wait" or swim_wait == "Wait":
        print("You arrive at the island unharmed. 'There is a house with 3 doors.")
        colors = input("One red, one yellow and one blue. Which colour do you choose?\n")
        if colors == "red" or colors == "Red":
            print("It's a room full of fire. Game Over.")
        elif colors == "yellow" or colors == "Yellow":
            print("You found the treasure! You Win!")
        elif colors == "blue" or colors == "Blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose the door that does not exist. Game over!")
    else:
        print("Please type 'swim' or wait' correctly!")
else:
    print("Please type 'right' or 'left' correctly!")


# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")


#
# cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
# if cross_road == "right" and "Right":
#     print("You fall into a hole. Game over!")
# elif cross_road == "left" and "Left":
#      print("You've come to a lake. There is an island in the middle of the lake.")
# else:
#      print("Please type 'right' or 'left' correctly!")
#
# swim_wait = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n"
# if swim_wait == "swim" and "Swim":
#     print("You get attacked by an angry trout. Game Over.")
# elif swim_wait == "wait" and "Wait":
#     print("You arrive at the island unharmed. 'There is a house with 3 doors.")
# else:
#     print("Please type 'swim' or wait' correctly!")
#
# red_blue_yellow = input("One red, one yellow and one blue. Which colour do you choose?\n")
# if red_blue_yellow == "red" and "Red":
#     print("It's a room full of fire. Game Over.")
# elif red_blue_yellow == "yellow" and "Yellow":
#     print("You found the treasure! You Win!")
# elif red_blue_yellow == "blue" and "Blue":
#     print("You enter a room of beasts. Game Over.")
# else:
#     print("You chose the door that does not exist. Game over!")

