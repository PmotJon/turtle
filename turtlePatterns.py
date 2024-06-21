import turtle


def pattern_desain():
    colors = ["red", "orange", "green", "purple", "blue"]
    pen = turtle.Turtle()
    pen.speed(20)
    turtle.bgcolor("black")

    for i in range(180):
        pen.color(colors[i % 6])
        pen.forward(200)
        pen.right(61)
        pen.forward(100)
        pen.right(120)
        pen.forward(100)
        pen.right(61)
        pen.forward(200)
        pen.right(181)

    pen.hideturtle()


pattern_desain()
turtle.done()
