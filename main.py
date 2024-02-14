from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")

# Turtle Challenge 1 - Draw a square
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# Turtle Challenge 2 - Draw a dashed line
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Turtle Challenge 3 - Draw different shapes

# tim.pencolor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
# for _ in range(3):
#     tim.right(120)
#     tim.forward(100)
#
# tim.pencolor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
#
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)
#
# tim.pencolor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
#
# for _ in range(5):
#     tim.right(72)
#     tim.forward(100)
#
# tim.pencolor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
#
# for _ in range(6):
#     tim.right(60)
#     tim.forward(100)
#
# tim.pencolor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
#
# for _ in range(7):
#     tim.right(51.43)
#     tim.forward(100)
#
# tim.pencolor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
#
# for _ in range(8):
#     tim.right(45)
#     tim.forward(100)
#
# tim.pencolor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
#
# for _ in range(9):
#     tim.right(40)
#     tim.forward(100)
#
# tim.pencolor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
#
# for _ in range(10):
#     tim.right(36)
#     tim.forward(100)


# Challenge 3 revised - Draw different shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     tim.pencolor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
#     for _ in range(num_sides):
#         tim.right(angle)
#         tim.forward(100)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

# Challenge 4 - Generate a random walk
def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    return (r, g, b)
#
# tim.pensize(10)
# tim.speed(8)
# directions = [0, 90, 180, 270]
#
# for _ in range(150):
#     tim.color(random_color())
#
#     tim.setheading(random.choice(directions))
#     tim.forward(50)


# Turtle Challenge 5 - Draw a Spirograph
angle = 0
tim.speed(0)
while angle != 360:
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(angle)
    angle += 5




























screen.exitonclick()
