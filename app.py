import turtle

# win => window
win = turtle.Screen()
win.title("Python Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# First Paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0) 
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(strech_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Second Paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(strech_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_a.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_a_up, "Up")
win.onkeypress(paddle_a_down, "Down")

while True:
    win.update()