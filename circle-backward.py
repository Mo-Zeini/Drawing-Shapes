# This program draws a circle backwards using the turtle library

import math # Import the math library
import turtle # Import the turtle library
bob = turtle.Turtle() # Assign the returned instance of the class Turtle to the variable bob

# This function controls the drawing of the circle and defines the circumference of the circle and its length 
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length) # Move forward
        t.lt(step_angle) # Turn left with an angle

arc(bob, r=100, angle=360) # Call the arc function
