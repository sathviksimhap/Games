from turtle import Turtle, Screen
from pins import Pin

game_on = True
colors = ["brown", "magenta", "red", "black"]
players = []

no_players = int(input("Enter the number of players (1-4): "))

if 0 < no_players <= 4:
    if no_players > 0:
        print("For player 1: Press (A) when its your turn")
    if no_players > 1:
        print("For player 2: Press (S) when its your turn")
    if no_players > 2:
        print("For player 3: Press (D) when its your turn")
    if no_players > 3:
        print("For player 4: Press (F) when its your turn")

else:
    exit("Invalid number of players")

print("Loading...")

#BOARD
Board = Screen()
Board.setup(560, 560)
Board.bgpic("board.PNG")

for i in range(no_players):
    player = Pin(colors[i])
    players.append(player)

Board.listen()
Board.onkey(players[0].roll, "a")
Board.onkey(players[1].roll, "s")
Board.onkey(players[2].roll, "d")
Board.onkey(players[3].roll, "f")








Board.exitonclick()