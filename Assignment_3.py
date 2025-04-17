import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Heart Drawing")

# Create turtle
heart = turtle.Turtle()
heart.color("red")
heart.pensize(3)
heart.speed(1)

# Function to draw heart
def draw_heart():
    heart.begin_fill()
    heart.left(140)
    heart.forward(180)
    heart.circle(-90, 200)
    heart.left(120)
    heart.circle(-90, 200)
    heart.forward(180)
    heart.end_fill()

# Draw the heart
draw_heart()

# Move turtle to write message
heart.penup()
heart.goto(0, -20)
heart.color("white")
heart.write("Love You!", align="center", font=("Arial", 18, "bold"))

# Hide the turtle
heart.hideturtle()

# Keep window open
turtle.done()
