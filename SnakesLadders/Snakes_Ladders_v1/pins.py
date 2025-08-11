from turtle import Turtle
import random
import time
from mydata import POSITIONS, SNAKES, LADDERS

class Pin(Turtle):
    def __init__(self, color):
        super().__init__()
        self.pos = 0
        self.shape("triangle")
        self.color(color)
        self.up()
        self.setheading(90)
        self.goto(-275, -240)
        self.shapesize(1, 1.5)


    def roll(self):
        goal = random.randint(1, 6)
        goal_pos = self.pos + goal
        self.move(goal_pos)

        if self.pos in SNAKES.keys():
            self.goto(POSITIONS[SNAKES[self.pos]])
            self.pos = SNAKES[self.pos]

        elif self.pos in LADDERS.keys():
            self.goto(POSITIONS[LADDERS[self.pos]])
            self.pos = LADDERS[self.pos]
            if self.pos == 100:
                self.winner()

    def move(self, goal):
        if goal <= 100:
            while self.pos != goal:
                self.pos += 1
                self.goto(POSITIONS[self.pos])
                time.sleep(0.2)
            if self.pos == 100:
                self.winner()

    def winner(self):
        print("I Win\nGame Over!")