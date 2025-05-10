import turtle

drawing_pen = turtle.Turtle()

def draw_curve():
    # Draw a curve (part of the heart shape)
    for _ in range(200):  # Using '_' for a loop variable that's not used
        drawing_pen.right(1)
        drawing_pen.forward(1)

def draw_heart():
    # Function to draw a heart shape
    heart_color = 'firebrick'  # Changed color name
    drawing_pen.fillcolor(heart_color)
    drawing_pen.begin_fill()
    drawing_pen.left(140)
    drawing_pen.forward(113)
    draw_curve()
    drawing_pen.left(120)
    draw_curve()
    drawing_pen.forward(112)
    drawing_pen.end_fill()

def write_text():
    # Function to write the text on the heart
    text_color = 'lime'  # Changed color name
    drawing_pen.penup()
    drawing_pen.setpos(-68, 95)
    drawing_pen.pendown()
    drawing_pen.color(text_color)
    drawing_pen.write("SWEETHEART", font=("Arial", 14, "bold")) # Changed text and font

# Main drawing sequence
draw_heart()
write_text()

# Hide the turtle icon
drawing_pen.hideturtle()

turtle.done() # Keep the window open until it's manually closed