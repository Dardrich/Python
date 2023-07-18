import turtle

turtle.hideturtle()

turtle.penup()
turtle.goto(0, -60)  # Move to the initial smiley face
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(-40, -10)  # Move to the smile position
turtle.pendown()
turtle.setheading(-30)  # Set the initial angle for the smile

turtle.color("black")
turtle.width(6)
turtle.circle(80, 60)  # Draw an arc for the smile

turtle.penup()
turtle.goto(35, 60)  # Move to the first eye position
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-35, 60)  # Move to the second eye position
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.exitonclick()
turtle.mainloop()
