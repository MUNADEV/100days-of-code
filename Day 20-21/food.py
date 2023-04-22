from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-180, 180)
        random_y = random.randint(-180, 180)
        self.goto(random_x, random_y)
