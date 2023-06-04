# This program draws a polygon with 7 legs using the turtle library

import turtle # Import the turtle library
bob = turtle.Turtle() # Assign the returned instance of the class Turtle to the variable bob

# This function controls the drawing of the polygon
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length) # Move forward
        t.lt(angle) # Turn left with an angle

polygon(bob, n=7, length=70)  # Call the polygon function
