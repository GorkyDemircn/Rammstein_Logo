import turtle as tur

def adjustment():
    scr = tur.Screen()
    scr.bgcolor("black")
    tur.pensize(2)
    tur.penup()
    tur.pencolor("white")
    tur.shape("turtle")
    tur.goto(-200, 350)
    tur.pendown()    

def top_left_corner_shape():
    tur.color("white")
    tur.begin_fill()
    tur.forward(140)
    tur.right(90)
    tur.forward(40)
    tur.right(90)
    tur.forward(100)
    tur.left(90)
    tur.forward(95)
    tur.right(90)
    tur.forward(40)
    tur.right(90)
    tur.forward(135)
    tur.end_fill()
    
def right_long_shape():
    tur.color("black")
    tur.pencolor("white")
    
    tur.right(90)
    tur.penup()
    tur.goto(-20, 350)
    tur.pendown()    
    tur.begin_fill()
    tur.forward(180)
    tur.right(90)
    tur.forward(200)
    tur.left(90)
    tur.forward(150)
    tur.right(90)
    tur.forward(150)
    tur.right(90)
    tur.forward(40)
    tur.right(90)
    tur.forward(110)
    tur.left(90)
    tur.forward(150)
    tur.right(90)
    tur.forward(200)
    tur.left(90)
    tur.forward(140)
    tur.right(90)
    tur.forward(40)
    tur.color("white")
    tur.end_fill()
    
def right_bottom_long_shape():
    tur.color("black")
    tur.pencolor("white")
    
    tur.penup()
    tur.goto(310, -30)
    tur.right(180)
    tur.pendown()
    tur.begin_fill()
    tur.forward(140)
    tur.right(90)
    tur.forward(150)
    tur.left(90)
    tur.forward(150)
    tur.right(90)
    tur.forward(180)
    tur.right(90)
    tur.forward(35)
    tur.right(90)
    tur.forward(145)
    tur.left(90)
    tur.forward(150)
    tur.right(90)
    tur.forward(145)
    tur.left(90)
    tur.forward(105)
    tur.right(90)
    tur.forward(40)
    tur.color("white")
    tur.end_fill()

def bottom_right_corner_shape():
    tur.penup()
    tur.goto(-200, -320)
    tur.pendown()
    tur.begin_fill()
    tur.forward(140)
    tur.left(90)
    tur.forward(35)
    tur.left(90)
    tur.forward(105)
    tur.right(90)
    tur.forward(95)
    tur.left(90)
    tur.forward(40)
    tur.left(90)
    tur.forward(120)
    tur.color("white")
    tur.end_fill()
    
def invoke_all_function():
    adjustment()
    top_left_corner_shape()
    right_long_shape()
    right_bottom_long_shape()
    bottom_right_corner_shape()

invoke_all_function()
tur.exitonclick()
