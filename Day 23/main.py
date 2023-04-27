import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player, car manager, and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for key presses and assign the "Up" key to make the player go up
screen.listen()
screen.onkey(player.go_up, "w")

# Set the game state to "on"
game_is_on = True

# Start the game loop
while game_is_on:
    # Wait for a short time (0.1 seconds) to make the game run more smoothly
    time.sleep(0.1)

    # Update the screen to show any changes
    screen.update()

    # Create new cars and move existing ones
    car_manager.create_car()
    car_manager.move_cars()

    # Check for collisions between the player and the cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            # If there is a collision, end the game and show the "game over" message
            game_is_on = False
            scoreboard.game_over()

    # If the player reaches the finish line, reset the player and increase the level
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

# Exit the game when the user clicks the screen
screen.exitonclick()
