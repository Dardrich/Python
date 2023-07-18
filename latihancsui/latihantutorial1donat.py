import turtle

data = input("Masukkan rasa donat: ").lower()

turtle.hideturtle()  # Hide the turtle cursor

if data == "cokelat":
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.circle(150)  # Outer circle
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, 50)  # Move to the center of the donut
    turtle.pendown()

    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(100)  # Inner circle
    turtle.end_fill()

    turtle.exitonclick()
elif data == "stroberi":
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(150)  # Outer circle
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, 50)  # Move to the center of the donut
    turtle.pendown()

    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(100)  # Inner circle
    turtle.end_fill()

    turtle.exitonclick()
else:
    print("Maaf, rasa tersebut tidak tersedia")
