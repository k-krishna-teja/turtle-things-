import turtle

# Initialize the turtle
t = turtle.Turtle()
s = turtle.Screen()

# Set the background color of the screen
s.bgcolor('#262626')

# Define the colors to be used
col = ['#ED7864', '#E5744F', '#592F2F', '#6E382E']

# Set the speed of the turtle
t.speed(0)  # Fastest speed

# Draw the pattern
for n in range(36):  # Increase the range for more layers
    for x in range(8):  # Number of petals in each layer
        t.pencolor(col[n % 4])
        t.pensize(2)
        t.circle(80 + n * 20, 90)
        t.left(50)
        t.left(45)

# Exit on click
s.exitonclick()
