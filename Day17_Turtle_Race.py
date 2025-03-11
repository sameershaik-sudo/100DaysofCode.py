import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

def create_turtle(name, i, x):
    name = Turtle()
    name.shape("turtle")
    name.color(colors[i])
    name.penup()
    name.goto(x=-230, y=-100+x)
    all_turtles.append(name)

for i in range(6):
    create_turtle(colors[i], i, i*30)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230: # turtle size is 40x40 , so reduce 20 from finish line
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won the bet! The {winner} turtle is the winner!")
            else:
                print(f"You lost! The winner is the {winner} turtle!")

screen.exitonclick()
