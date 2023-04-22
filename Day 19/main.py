from turtle import Turtle, Screen
import random

# Create the screen and define its size
screen = Screen()
screen.setup(width=500, height=400)

# Obtain the colour chosen by the user and validate that it is one of the available colours.
available_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color ({', '.join(available_colors)}): ")
while user_bet and user_bet.lower() not in available_colors:
    user_bet = screen.textinput(title="Invalid color", prompt=f"{user_bet} is not a valid color. Enter a color ({', '.join(available_colors)}): ")

# Create the turtles and define their initial positions
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for index, color in enumerate(available_colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

# Start the race when the user has placed a bet
is_race_on = bool(user_bet)

while is_race_on:
    for turtle in all_turtles:
        # Make each turtle move a random distance.
        turtle.forward(random.randint(0, 10))

        # Check if any tortoise has reached the goal (230 is 250 - half the width of the tortoise).
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            # Show the result of the race
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

# Wait for user to close the window before exiting
screen.exitonclick()
