print("day 0 homework ")
from turtle import *

#we want to print a house

#step 1: draw a square

width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()


#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
penup()
goto(60, 160)
pendown()

color("blue")
begin_fill()
left(30)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
end_fill()

#drawing a window 2

penup()
goto(170, 160)
pendown()

color("blue")
begin_fill()
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
end_fill()




exitonclick()
