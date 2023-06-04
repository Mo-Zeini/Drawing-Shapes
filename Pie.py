# This program draws a pie as a polygon with 6 legs and 3 intersections

import turtle # Import the turtle library
bob = turtle.Turtle() # Assign the returned instance of the class Turtle to the variable bob

# This function controls the drawing of the pie
def shape(t, n, length):
    angle = 360 / n # Define the angle
    for i in range(n):
        t.fd(length) # Move forward
        t.lt(angle) # Turn left with an angle


    t.lt(60) # Turn left with an angle of 60 degrees
    t.fd(140) # Move forward with a length of 140

    t.lt(120) # Turn left with an angle of 120 degrees
    t.fd(70) # Move forward with a length of 70

    t.lt(120) # Turn left with an angle of 120 degrees
    t.fd(140) # Move forward with a length of 140

    t.lt(120) # Turn left with an angle of 120 degree
    t.fd(70) # Move forward with a length of 70

    t.lt(120) # Turn left with an angle of 120 degrees
    t.fd(140) # Move forward with a length of 140

    t.lt(120) # Turn left with an angle of 120 degree
    t.fd(70) # Move forward with a length of 70

shape(bob, 6, 70)  # Call the shape function
