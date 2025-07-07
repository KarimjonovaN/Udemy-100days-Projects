from turtle import Turtle, Screen
import random

is_race_on = True
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color.")
colors = ["yellow", "green","red", "orange", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
x_position = [ -230, -200, -170, -140, -110]
all_turtles = []

'''creating 6 turtles'''
for turtle_index in range(0,5):
    nanny = Turtle(shape="turtle")
    nanny.penup()
    nanny.color(colors[turtle_index])
    nanny.goto(x=x_position[turtle_index], y=y_positions[turtle_index])
    all_turtles.append(nanny)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        '''250 - (40/2) = 230 - half the width of the turtle.'''
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        '''make turtles move random distance'''
        turtle.pendown()
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
