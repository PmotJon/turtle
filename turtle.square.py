from turtle import *

# Graphical user interface star pattern
turtle = Turtle()
screen = Screen()

for c in ["red", "green", "blue", "yellow"]:
    turtle.color(c)
    turtle.width(3)
    turtle.forward(100)
    turtle.right(90)


screen.mainloop()
screen.exitonclick
