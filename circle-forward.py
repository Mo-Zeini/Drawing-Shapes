# This program draws a circle forward using the turtle library

import math # Import the math library
import turtle # Import the turtle library
bob = turtle.Turtle() # Assign the returned instance of the class Turtle to the variable bob

# This function controls the drawing of the circle
def polygon(t, n, length):
    angle = 360 / n # Defining the angle
    for i in range(n):
        t.fd(length) # Move forward
        t.lt(angle) # Turn left


# This function defines the circumference of the circle and its length 
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

circle(bob, r=100)  # Call the circle function
