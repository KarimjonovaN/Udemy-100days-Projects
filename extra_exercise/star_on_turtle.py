from turtle import Turtle, Screen

color_list = ["Yellow", "Green", "Red", "Blue", "Orange"]
nanny = Turtle()
nanny.speed("fastest")
nanny.pensize(3)
nanny.hideturtle()

for i in range(5):
    nanny.pencolor(color_list[i])
    nanny.forward(200)
    nanny.right(144)


screen = Screen()
screen.exitonclick()