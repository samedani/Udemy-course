import turtle
import turtle as t
import random

t.colormode(255)  # Ensure we use RGB color mode
tim = t.Turtle()
lengths = [25, 30]
directions = [0, 90, 180, 270]
tim.speed('fastest')
tim.pensize(2)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    tim.pencolor(r, g, b)  # Set the pen color to a random RGB value

# Set initial heading to a specific direction
tim.setheading(random.choice(directions))

def draw_spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        random_color()  # Apply a random color
        tim.circle(150)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

s = t.Screen()
s.exitonclick()