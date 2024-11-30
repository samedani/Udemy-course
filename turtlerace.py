from turtle import Turtle, Screen
import random

is_race_on = False
all_turtles = []
screen = Screen()
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 350:
            is_race_on = False
            winner_color = turtle.pencolor()
            turtle.goto(0, 200)
            if user_bet.lower() == winner_color.lower():
                turtle.write(f"Your turtle won! The {winner_color} turtle won!", align="center", font=("Arial", 16, "bold"))
                # print(f"Your turtle won! The {winner_color} turtle won!")
            else:
                turtle.write(f"Your turtle lost! The {winner_color} turtle won!",  align="center", font=("Arial", 16, "bold"))
                # print(f"Your turtle lost! The {winner_color} turtle won!")


screen.exitonclick()
