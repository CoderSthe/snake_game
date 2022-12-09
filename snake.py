import turtle

# create screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
# turtle.done()

# create border
border = turtle.Turtle()
border.color("white")
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(3)

for side in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()




# create the snake turtle object
snake = turtle.Turtle()
snake.shape("square")
snake.color("light green")
snake.penup()
snake.goto(0,0)


while True:
    snake.forward(1)
    snake.speed(1)
    if snake.onclick("up"):
        snake.left(90)

turtle.done()


