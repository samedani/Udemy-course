import turtle as t
import random

t.colormode(255)  # Ensure we use RGB color mode
tim = t.Turtle()
lengths = [25, 30]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    tim.pencolor(r, g, b)  # Set the pen color to a random RGB value

# Set initial heading to a specific direction
tim.setheading(random.choice(directions))

for _ in range(1000):
    random_color()  # Apply a random color
    tim.forward(random.choice(lengths))  # Move forward by a random length

    # After moving forward, choose a random direction to turn
    tim.left(random.choice([90, 180, 270]))  # Turning instead of setting random heading

s = t.Screen()
s.exitonclick()