num = 3.65
print("{:.10f}".format(num))
print(num)

import turtle
tom = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tom.color("blue")

tom.shape("turtle")

degrees_to_turn = 360 / 12
tom.penup()
for count in range (12):
    tom.forward(100)
    tom.pendown()
    tom.forward(15)
    tom.penup()
    tom.forward(20)
    tom.stamp()
    
    
    tom.penup
    
    tom.forward(-135)
    tom.left(degrees_to_turn)
    
wn.exitonclick()


