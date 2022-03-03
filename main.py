import turtle
import math

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def setupWindow(mywindow):
  mywindow.setworldcoordinates(-360, -1, 360, 1)

def setupAxis(turtle):
  turtle.penup()
  turtle.goto(0, -1)
  turtle.pendown()
  turtle.goto(0, 1)
  turtle.penup()
  turtle.goto(360, 0)
  turtle.pendown()
  turtle.goto(-360, 0)
  turtle.penup()

def drawSineCurve(turtle):
  turtle.pendown()
  for x in range(-360, 360):
    y = math.sin(math.radians(x))
    print(y)
    turtle.goto(x,y)
  turtle.goto(-360, 0)
  turtle.penup()
    
def drawCosineCurve(turtle):
  turtle.pendown()
  for x in range(-360, 360):
    y = math.cos(math.radians(x))
    print(y)
    turtle.goto(x,y)
  turtle.goto(-360, 0)
  turtle.penup()

def drawTangentCurve(turtle):
  turtle.pendown()
  for x in range(-360, 360):
    y = math.tan(math.radians(x))
    print(y)
    turtle.goto(x,y)
  turtle.goto(-360, 0)
  turtle.penup()

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
