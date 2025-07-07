# from turtle import Turtle, Screen

# color_list = ["Yellow", "Green", "Red", "Blue", "Orange"]
# nanny = Turtle()
# nanny.speed("fastest")
# nanny.pensize(5)
# nanny.hideturtle()
# nanny.penup()
# nanny.setposition(-150, 0)
# nanny.pendown()

# for i in range(5):
#     nanny.pencolor(color_list[i])
#     nanny.forward(300)
#     nanny.right(144)

# screen = Screen()
# screen.exitonclick()


# from turtle import Turtle, Screen

# t = Turtle()
# screen = Screen()

# for i in range(4):
#     t.forward(60)
#     t.left(90)
#     t.forward(60)
#     t.right(90)
#     t.forward(60)
#     t.right(90)

# for i in range(4):
#     t.forward(60)
#     t.left(90)
#     t.forward(60)
#     t.right(90)
#     t.forward(60)
#     t.left(90)

# t.left(90)
# for i in range(4):
#     t.forward(60)
#     t.left(90)
#     t.forward(60)
#     t.right(90)
#     t.forward(60)
#     t.left(90)

# t.left(90)
# for i in range(4):
#     t.forward(60)
#     t.left(90)
#     t.forward(60)
#     t.right(90)
#     t.forward(60)
#     t.left(90)

# screen.exitonclick()


# from turtle import Turtle, Screen

# def plus_sign(t):
#     for i in range(4):
#         t.forward(60)
#         t.left(90)
#         t.forward(60)
#         t.right(90)
#         t.forward(60)
#         t.left(90)

# t = Turtle()
# screen = Screen()

# for n in range(4):
#     plus_sign(t)
#     t.left(90)

# screen.exitonclick()


# from turtle import Turtle, Screen

# t = Turtle()
# screen = Screen()

# for i in range(8):
#     t.forward(50)
#     t.right(45)
#     t.forward(50)
#     t.left(90)

# screen.exitonclick()


# from turtle import Turtle, Screen

# t = Turtle("turtle")
# screen = Screen()
# for i in range(6):
#     t.forward(150)
#     t.backward(150)
#     t.right(60)

# for side in [30, 60, 90, 120, 150]:
#     t.setheading(0)  # Face right
#     t.forward(side)
#     t.left(120)
#     for _ in range(6):
#         t.forward(side)
#         t.left(60)
#     t.goto(0, 0)


# screen.exitonclick()



# from turtle import Turtle, Screen

# t = Turtle()
# screen = Screen()
# screen.setup(width=600, height=600)

# for i in range(1):
#     t.penup()
#     t.goto(y= 0, x= -150)
#     t.pendown()

#     t.goto(y= -150, x=0)
#     t.goto(y= 0, x=150)
#     t.goto(y= 150, x=0)
#     t.goto(y= 0, x= -150)

# for n in range(1):
#     t.penup()
#     t.goto(y= -130, x= -130)
#     t.pendown()

#     # t.goto(y= -150, x=0)
#     t.goto(y= -75, x=75)
#     t.goto(y= 130, x=130)
#     t.goto(y= 75, x= -75)
#     t.goto(y= -130, x= -130)

# for m in range(1):
#     t.penup()
#     t.goto(y= -130, x= 130)
#     t.pendown()

#     # t.goto(y= -150, x=0)
#     t.goto(y= 75, x=75)
#     t.goto(y= 130, x= -130)
#     t.goto(y= -75, x= -75)
#     t.goto(y= -130, x= 130)

# screen.exitonclick()

from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)

t = Turtle()
t.hideturtle()
t.pensize(2)

# Define points for each square/diamond
square = [(-150, 0), (0, -150), (150, 0), (0, 150)]
diamond_1 = [(-130, -130), (75, -75), (130, 130), (-75, 75)]
diamond_2 = [(130, -130), (75, 75), (-130, 130), (-75, -75)]

def draw_shapes(coords):
    t.penup()
    t.goto(coords[0])
    t.pendown()
    for point in coords[1:]:
        t.goto(point)
    t.goto(coords[0])  # Close the shape

# Drawing all shapes
for shape in [square, diamond_1, diamond_2]:
    draw_shapes(shape)

screen.exitonclick()
