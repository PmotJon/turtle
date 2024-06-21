from turtle import *

# Graphical user interface star pattern
turtle = Turtle()
screen = Screen()

for c in ["red", "green", "blue", "yellow", "pink"]:
    turtle.color(c)
    turtle.width(5)
    turtle.width(5)
    turtle.forward(200)
    turtle.right(144)

screen.mainloop()
screen.exitonclick
