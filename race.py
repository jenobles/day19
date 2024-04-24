from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_list = []

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = 'Make your bet', prompt = 'Which turtle will win the race? Enter a color: ')

for i in colors:
    num = int(colors.index(i))
    turtle_list.append(Turtle(shape = 'turtle'))
    turtle_list[num].color(i)
    turtle_list[num].penup()
    turtle_list[num].goto(x = -230, y = 150 - num * 50)

if user_bet:
    is_race_on = True

while is_race_on:  
    for i in turtle_list:
        index = int(turtle_list.index(i))
        if turtle_list[index].xcor() > 230:
            is_race_on = False
            winning_color = turtle_list[index].pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        else:
            distance = random.randint(0, 10)
            turtle_list[index].forward(distance)

screen.exitonclick()