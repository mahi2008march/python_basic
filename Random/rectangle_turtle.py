# Rectangle
# Fd 300 rt 90 fd 150 rt 90
#Fd 300 rt 90 fd 150 rt 90
import turtle
import time
s = turtle.Screen()
s.bgcolor("light blue")
t=turtle.Turtle()
t.pen(pencolor="red", fillcolor="purple", pensize=10, speed=2)
t.begin_fill()
t.fd(200)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(100)
t.end_fill()

time.sleep(5)

t.end_fill()
t.rt(90)


for i in range(2):
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    i+=1
time.sleep(2)

time.sleep(5)