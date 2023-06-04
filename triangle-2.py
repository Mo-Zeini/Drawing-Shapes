# or we can use the second method to draw a triangle as follows

import turtle # Import the turtle library
bob = turtle.Turtle() # Assign the returned instance of the class Turtle to the variable bob

# # This function controls the drawing of the tiangle and draws it
def triangle2(t):
    for i in range(3):
        t.fd(100) # Move forward with a length of 100
        t.lt(120) # Turn left with an angle of 120

triangle2(bob) # Call the triangle2 function
