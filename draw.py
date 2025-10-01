import turtle
import colorsys

turtle.tracer(20)
b = "black"
turtle.bgcolor(b)
h = 0

for i in range(600):
    h += 0.004
    turtle.color(colorsys.hsv_to_rgb(h,1,1),b)
    turtle.begin_fill()

    for j in  range(5):
        turtle.fd(100)
        turtle.rt(100)
        turtle.fd(100)
        turtle.lt(100)
        turtle.rt(360/5)
    
    turtle.end_fill()
    turtle.rt(2)
    turtle.hideturtle()
    
turtle.done()