#  File: Turtle.py
#  Description: Program that uses the Python Turtle module to draw graphs
#  Student's Name: Philip Cameron Bishop
#  Student's UT EID: pcb465
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 9/11/2015
#  Date Last Modified: 9/18/2015


# Import the modules "turtle" (all of the turtle classes and methods) and
# "math"(useful math functions and constants such as sin, sqrt, pi, etc.)
import math, turtle

def main():
    
    # Create a window 900 by 900 pixels in size.
    turtle.setup(width=900, height=900, startx=0, starty=0)
    # Call this window "CS 313E Assignment 2"
    turtle.title("CS 313E Assignment 2")
    
    # Create a turtle object.
    ttl = turtle.Turtle()

    ttl.speed(0)
    
    # Draw x and y axes that extend from -400 to +400 in the window.
    ttl.penup()
    ttl.goto(-400, 0)
    ttl.pendown()
    ttl.goto(400,0)
    ttl.penup()
    ttl.goto(0, -400)
    ttl.pendown()
    ttl.goto(0, 400)
    ttl.penup()
    
    # Draw tick marks on each axis at each 100 pixels.
    # The tick marks must be of length 10 pixels, extending from 5 pixels on one side of the axis to 5 pixels on the other side. 
    def Line (Xstart, Xend, Ystart, Yend):
        ttl.penup()
        ttl.goto(Xstart, Ystart)
        ttl.pendown()
        ttl.goto(Xend, Yend)
        ttl.penup

    # Use a scale of 1:100, so that the point (2,3) will appear in the window at the location (200 pixels, 300 pixels) from the origin.
    # Label each tick mark 1, 2, 3, etc. on both axes.
    def Write (x, y, string):
        ttl.penup()
        ttl.goto(x, y)
        ttl.pendown()
        ttl.write(string)
        ttl.penup()    

    # For loop to make all the grid marks and label them
    for i in [-400, -300, -200, -100, 100, 200, 300, 400]:
        Line(i, i, 5, -5)
        Write(i - 5 , -20, int(i/100))
        Line(-5, 5, i, i)
        Write(10, i - 5, int(i/100))
    Write (-15, -20, "0")

    #Function to help me plot the functions
    def plotFunc(func, a):
        # Ready the pen
        ttl.penup()
        #Set the lower bound and with it the X and Y values
        x = -314
        y = func(x/100)
        # Get ready to write
        ttl.goto(x, y*100)
        ttl.pendown()
        #Keep chugging through function until we reach pi
        while x <= 314:
            x = x + a
            y = func(x/100)
            ttl.goto(x, y*100)
        ttl.penup()
        
    # Function that allows me to plot the X^2 - 4 function
    def squareFunc(x):
        return (x ** 2 - 4)

    # Graph the function x2 - 4 on the interval from x=-π to x=+π.
    ttl.pencolor("Orange")
    plotFunc(squareFunc,1)

    # Graph the function sin(x) on the interval from x=-π to x=+π
    ttl.pencolor("Green")
    plotFunc(math.sin, 1)

    # Graph the function cos(x) on the interval from x=-π to x=+π
    ttl.pencolor("Blue")
    plotFunc(math.cos, 1)

    # Graph a function of my own choosing! (tangent)
    ttl.pencolor("Purple")
    plotFunc(math.tan, 1)
        
    # End the program
    turtle.done()  



main()
