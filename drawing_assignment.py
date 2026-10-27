from turtle import *

# Colourful Star Pattern
setup(800, 700)
bgcolor("black")
speed(0)
pensize(2)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink"]

length = 40

for i in range(40):
    pencolor(colors[i % len(colors)])

    # Draw one star
    for j in range(5):
        forward(length)
        right(144)

    # Turn before drawing the next star
    right(10)

    # Dynamically change the length
    length = length + 3

exitonclick()
