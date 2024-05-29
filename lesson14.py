import turtle
import random


def draw_cube():
    for i in range(4):
        bob.right(90)
        bob.backward(100)
    bob.right(90)
    bob.backward(100)
    bob.right(45)
    bob.backward(50)
    bob.right(45)
    bob.backward(100)
    bob.right(90)
    bob.backward(100)
    bob.right(45)
    bob.backward(50)
    bob.right(135)
    bob.backward(100)
    bob.right(45)
    bob.backward(50)


def b():
    bob.left(30)
    bob.forward(70)
    bob.right(30)
    bob.forward(50)
    bob.right(90)
    bob.forward(20)
    bob.right(60)
    bob.forward(25)
    bob.left(120)
    bob.forward(25)
    bob.right(60)
    bob.forward(20)
    bob.right(90)
    bob.forward(50)
    bob.right(30)
    bob.forward(70)


def a():
    for i in range(50):
        bob.forward(200)
        bob.left(110)


def draw_polygon(n):
    corner = 180 - (180 * (n - 2) / n)
    for i in range(n):
        bob.forward(100)
        bob.left(corner)


def draw_snowflake():
    bob.color('cyan')
    bob. pensize(3)

    for i in range(7):
        bob.forward(100)
        bob.backward(50)
        bob.right(45)
        bob.forward(40)
        bob.backward(40)
        bob.left(90)
        bob.forward(40)
        bob.backward(40)
        bob.right(45)
        bob.home()
        bob.left(60 * i)

    bob.hideturtle()


def up():
    bob.setheading(90)
    bob.forward(50)


def down():
    bob.setheading(270)
    bob.forward(50)


def left():
    bob.setheading(180)
    bob.forward(50)


def right():
    bob.setheading(0)
    bob.forward(50)


def change_color():
    color = random.choice(colors)
    bob.color(color)


def clear_all():
    bob.penup()
    bob.clear()
    bob.home()
    bob.pendown()


def dragging(x, y):
    bob.ondrag(None)
    bob.speed(-2)
    bob.setheading(bob.towards(x, y))
    bob.goto(x, y)
    bob.ondrag(dragging)


bob = turtle.Turtle()
bob.shape('turtle')
# bob.speed(10)

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'gold', 'cyan']

# draw_cube()
# draw_polygon(3)
# bob.circle(50)
# draw_snowflaka()
# bob.clear()
# turtle.onkeypress()
# turtle.onkeyrelease()

turtle.listen()
turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
turtle.onkey(change_color, 'space')
turtle.onkey(clear_all, 'c')
bob.ondrag(dragging)

turtle.mainloop()
