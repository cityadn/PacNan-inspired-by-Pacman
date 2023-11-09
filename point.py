import turtle


def triangle():
    TRIANGLE_SIZE = 20
    BORDER_SIZE = 3
    STAMP_UNIT = 20

    turtle.shape("triangle")
    turtle.hideturtle()
    turtle.penup()
    turtle.right(30)  # realign triangle
    turtle.fillcolor("red")
    turtle.shapesize(TRIANGLE_SIZE / STAMP_UNIT, TRIANGLE_SIZE / STAMP_UNIT, BORDER_SIZE)
    turtle.stamp()

def squareshape():
    turtle.shape('square')
    turtle.fillcolor('gold')
    turtle.shapesize(1)
    turtle.stamp()



