from turtle import Screen, Turtle
from random import randint, choice
import turtle
import time
s=Screen()
s.bgcolor("pink")
track = Turtle(visible=False)

# # track = turtle.Turtle()
track.speed('fastest')
track.penup()
track.goto(-100, 200)
for step in range(15):
    track.write(step, align='center')
    track.right(90)
    track.forward(10)
    track.pendown()
    track.forward(160)
    track.penup()
    track.backward(170)
    track.left(90)
    track.forward(20)


track.goto(200, 250)
track.write("Finish Line", align='center')
track.pendown()
track.right(90)
track.forward(300)


player1=turtle.textinput("Player 1","Enter Your Name: ")
# #
player_1 = turtle.Turtle('turtle')
player_1.speed('fastest')
player_1.color('Purple')
player_1.penup()
player_1.goto(-130, 165)
player_1.write(player1)
player_1.pendown()
player_1.penup()
player_1.goto(-120, 160)
player_1.pendown()

for turn in range(30):
    player_1.left(12)


player2=turtle.textinput("Player 2","Enter Your Name: ")

player_2 = turtle.Turtle('turtle')
player_2.speed('fastest')
player_2.color('blue')
player_2.penup()
player_2.goto(-130, 135)
player_2.write(player2)
player_2.pendown()
player_2.penup()
player_2.goto(-120, 130)
player_2.pendown()

for turn in range(30):
    player_2.left(12)

# #
player3=turtle.textinput("Player 3","Enter Your Name: ")
# #
player_3 = turtle.Turtle('turtle')
player_3.speed('fastest')
player_3.color('green')
player_3.penup()
player_3.goto(-130, 105)
player_3.write(player3)
player_3.pendown()
player_3.penup()
player_3.goto(-120, 100)
player_3.pendown()
for turn in range(30):
    player_3.left(12)

# #
while True:
    my_turtle = choice([player_1, player_2, player_3])
    my_turtle.forward(randint(1, 5))
    if my_turtle.xcor() > 200:
       break


my_turtle.color('gold')
x1=my_turtle.xcor()
y1=my_turtle.ycor()
track.penup()
track.goto(x1+30,y1)
track.color("black")
track.pendown()
track.write("I won!!",font = ("Agency FB", 30, "underline"))
time.sleep(10)
s.exitonclick()