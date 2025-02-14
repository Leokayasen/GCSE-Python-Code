import turtle

def drawCircle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.penup()
    turtle.circle(size)
    turtle.pendown()
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(900)

drawCircle(tommy, "red", 20, 20, 20)
drawCircle(tommy, "green", 20, 30, 20)
drawCircle(tommy, "blue", 20, 40, 20)

tommy.goto(30,40)
tommy.write("RGB Drawn!")





















