from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create a screen object
screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)

screen.title("Pong Game")

# Turn off automatic updating of the screen
screen.tracer(0)

# Create two paddles and a ball object
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


scoreboard = Scoreboard()

# Enable key listening on the screen and bind the Up and Down arrow keys to the right paddle
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# Bind the W and S keys to the left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)

    # Update the screen to display any changes
    screen.update()
    
    ball.move()

    # Bounce the ball off the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Bounce the ball off the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Reset the ball and add a point for the left player if the ball goes past the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        time.sleep(2)
        scoreboard.l_point()

    # Reset the ball and add a point for the right player if the ball goes past the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        time.sleep(2)
        scoreboard.r_point()

# Exit the game when the user clicks on the screen
screen.exitonclick()
