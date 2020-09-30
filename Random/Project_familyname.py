import turtle
import time
s=turtle.Screen()
t=turtle.Turtle()
#time.sleep(4)
import turtle
import time
s=turtle.Screen()
t=turtle.Turtle()
t.speed(3)
s.bgcolor("yellow")
colors = [ "Black", "pink", "turquoise", "blue","red", "yellow", "blue", "green", "orange" ]
family = []
name=turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
while name != "":

    family.append(name)
    name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
for x in range(50):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x % len(family)], font=("gigi", int((x + 4) / 4), "underline"))
    t.right(360 / len(family) + 2)

time.sleep(5)
#