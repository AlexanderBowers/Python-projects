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

while True:
    win.update()