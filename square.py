# This program draws a square using the turtle library

import turtle # Import the turtle library
bob = turtle.Turtle() # Assign the returned instance of the class Turtle to the variable bob

# This function controls the drawing of the square 
def square(t):
    for i in range(4):
        t.fd(100) # Move forward length of 100
        t.lt(90) # angle of 90 degrees

square(bob) # Call the square function
