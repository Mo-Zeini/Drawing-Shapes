# This programe draws a triangle using the turtle library

import turtle # Import the turtle library

bob = turtle.Turtle() # Assign the returned instance of the class Turtle to the variable bob

# # This function controls the drawing of the tiangle and draws it
def triangle(t, n, length):
    for i in range(n):
        angle = 360 / n # Define the angle
        t.fd(length) # Move forward
        t.lt(angle) # Turn left with an angle

triangle(bob, n=3  , length=100) # Call the triangle function




