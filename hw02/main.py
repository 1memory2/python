import turtle 
def goto(x,y):
    turtle.up();
    turtle.goto(x,y);
    turtle.down; 
def drawxwjx(x):
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(x)
        turtle.right(144)
    turtle.end_fill() 
turtle.setup(580,400,0,0)
turtle.color("yellow")
turtle.bgcolor("red")
goto(-250,120)
turtle.begin_fill()
for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.end_fill()
for i in range(4):
    x = 1
    if i in [0,3]:
        x = 0
    goto(-110+x*45,180-i*45)
    turtle.left(15-i*15)
    drawxwjx(30) 
turtle.hideturtle() 
turtle.done()

