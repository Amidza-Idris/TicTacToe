import sys
import time
from turtle import Screen, Turtle
import main
# Because for some reason im running into problems with calling back certain variables,
# so I import the file itself back to itself... yes.

screen = Screen()

victory = Turtle()
red = Turtle()
blue = Turtle()
end = Turtle()

buttonone = Turtle()
buttontwo = Turtle()
buttonthree = Turtle()
buttonfour = Turtle()
buttonfive = Turtle()
buttonsix = Turtle()
buttonseven = Turtle()
buttoneight = Turtle()
buttonnine = Turtle()


def end_button():
    end.speed(0)
    end.penup()
    end.shape("square")
    end.shapesize(6, 4)
    end.fillcolor("red")

    end.right(90)
    end.forward(300)

    end.onclick(end_all)
    end.write("END", align="center", font=("Arial", 22, "bold"))


def blue_wins():
    blue.speed(0)
    blue.penup()
    blue.hideturtle()
    blue.shape("square")

    blue.forward(250)
    blue.left(90)
    blue.forward(250)


def red_wins():
    red.speed(0)
    red.penup()
    red.hideturtle()
    red.shape("square")

    red.forward(-250)
    red.left(90)
    red.forward(250)


def victory_function():
    victory.speed(0)
    victory.penup()
    victory.hideturtle()
    victory.shape("square")

    victory.left(90)
    victory.forward(150)


def button_one():
    buttonone.penup()
    buttonone.shape('square')
    buttonone.shapesize(4, 4)
    buttonone.fillcolor('gray')

    buttonone.forward(-100)
    buttonone.left(90)
    buttonone.forward(100)

    buttonone.onclick(click1)


def button_two():
    buttontwo.penup()
    buttontwo.shape('square')
    buttontwo.shapesize(4, 4)
    buttontwo.fillcolor('gray')

    buttontwo.left(90)
    buttontwo.forward(100)

    buttontwo.onclick(click2)


def button_three():
    buttonthree.penup()
    buttonthree.shape('square')
    buttonthree.shapesize(4, 4)
    buttonthree.fillcolor('gray')

    buttonthree.forward(100)
    buttonthree.left(90)
    buttonthree.forward(100)

    buttonthree.onclick(click3)


def button_four():
    buttonfour.penup()
    buttonfour.shape('square')
    buttonfour.shapesize(4, 4)
    buttonfour.fillcolor('gray')

    buttonfour.forward(-100)

    buttonfour.onclick(click4)


def button_five():
    buttonfive.penup()
    buttonfive.shape('square')
    buttonfive.shapesize(4, 4)
    buttonfive.fillcolor('gray')

    buttonfive.onclick(click5)


def button_six():
    buttonsix.penup()
    buttonsix.shape('square')
    buttonsix.shapesize(4, 4)
    buttonsix.fillcolor('gray')

    buttonsix.forward(100)

    buttonsix.onclick(click6)


def button_seven():
    buttonseven.penup()
    buttonseven.shape('square')
    buttonseven.shapesize(4, 4)
    buttonseven.fillcolor('gray')

    buttonseven.left(-90)
    buttonseven.forward(100)
    buttonseven.left(-90)
    buttonseven.forward(100)

    buttonseven.onclick(click7)


def button_eight():
    buttoneight.penup()
    buttoneight.shape('square')
    buttoneight.shapesize(4, 4)
    buttoneight.fillcolor('gray')

    buttoneight.left(-90)
    buttoneight.forward(100)

    buttoneight.onclick(click8)


def button_nine():
    buttonnine.penup()
    buttonnine.shape('square')
    buttonnine.shapesize(4, 4)
    buttonnine.fillcolor('gray')

    buttonnine.left(-90)
    buttonnine.forward(100)
    buttonnine.left(90)
    buttonnine.forward(100)

    buttonnine.onclick(click9)


def OFA():
    buttonone.speed(10)
    buttontwo.speed(10)
    buttonthree.speed(10)
    buttonfour.speed(10)
    buttonfive.speed(10)
    buttonsix.speed(10)
    buttonseven.speed(10)
    buttoneight.speed(10)
    buttonnine.speed(10)

    button_one()
    button_two()
    button_three()
    button_four()
    button_five()
    button_six()
    button_seven()
    button_eight()
    button_nine()
    victory_function()


counter = 1
draw_count = 1


def click1(x, y):
    main.draw_count = main.draw_count + 1
    main.counter = main.counter + 1

    if buttonone.fillcolor() == "red" or buttonone.fillcolor() == "blue":
        main.counter = main.counter - 1
        return

    if counter % 2 == 0:
        buttonone.fillcolor("red")
    else:
        buttonone.fillcolor("blue")

    if main.counter >= 4:
        check_red()
        check_blue()


def click2(x, y):
    main.draw_count = main.draw_count + 1
    main.counter = main.counter + 1

    if buttontwo.fillcolor() == "red" or buttontwo.fillcolor() == "blue":
        main.counter = main.counter - 1
        return

    if counter % 2 == 0:
        buttontwo.fillcolor("red")
    else:
        buttontwo.fillcolor("blue")

    if main.counter >= 4:
        check_red()
        check_blue()


def click3(x, y):
    main.draw_count = main.draw_count + 1
    main.counter = main.counter + 1

    if buttonthree.fillcolor() == "red" or buttonthree.fillcolor() == "blue":
        main.counter = main.counter - 1
        return

    if counter % 2 == 0:
        buttonthree.fillcolor("red")
    else:
        buttonthree.fillcolor("blue")

    if main.counter >= 4:
        check_red()
        check_blue()


def click4(x, y):
    main.draw_count = main.draw_count + 1
    main.counter = main.counter + 1

    if buttonfour.fillcolor() == "red" or buttonfour.fillcolor() == "blue":
        main.counter = main.counter - 1
        return

    if counter % 2 == 0:
        buttonfour.fillcolor("red")
    else:
        buttonfour.fillcolor("blue")

    if main.counter >= 4:
        check_red()
        check_blue()


def click5(x, y):
    main.draw_count = main.draw_count + 1
    main.counter = main.counter + 1

    if buttonfive.fillcolor() == "red" or buttonfive.fillcolor() == "blue":
        main.counter = main.counter - 1
        return

    if counter % 2 == 0:
        buttonfive.fillcolor("red")
    else:
        buttonfive.fillcolor("blue")

    if main.counter >= 4:
        check_red()
        check_blue()


def click6(x, y):
    main.draw_count = main.draw_count + 1
    main.counter = main.counter + 1

    if buttonsix.fillcolor() == "red" or buttonsix.fillcolor() == "blue":
        main.counter = main.counter - 1
        return

    if counter % 2 == 0:
        buttonsix.fillcolor("red")
    else:
        buttonsix.fillcolor("blue")

    if main.counter >= 4:
        check_red()
        check_blue()


def click7(x, y):
    main.draw_count = main.draw_count + 1
    main.counter = main.counter + 1

    if buttonseven.fillcolor() == "red" or buttonseven.fillcolor() == "blue":
        main.counter = main.counter - 1
        return

    if counter % 2 == 0:
        buttonseven.fillcolor("red")
    else:
        buttonseven.fillcolor("blue")

    if main.counter >= 4:
        check_red()
        check_blue()


def click8(x, y):
    main.draw_count = main.draw_count + 1
    main.counter = main.counter + 1

    if buttoneight.fillcolor() == "red" or buttoneight.fillcolor() == "blue":
        main.counter = main.counter - 1
        return

    if counter % 2 == 0:
        buttoneight.fillcolor("red")
    else:
        buttoneight.fillcolor("blue")

    if main.counter >= 4:
        check_red()
        check_blue()


def click9(x, y):
    main.draw_count = main.draw_count + 1
    main.counter = main.counter + 1

    if buttonnine.fillcolor() == "red" or buttonnine.fillcolor() == "blue":
        main.counter = main.counter - 1
        return

    if counter % 2 == 0:
        buttonnine.fillcolor("red")
    else:
        buttonnine.fillcolor("blue")

    if main.counter >= 4:
        check_red()
        check_blue()


def check_red():
    if buttonone.fillcolor() == "red" and buttontwo.fillcolor() == "red" and buttonthree.fillcolor() == "red":
        cut_operation_red()
    elif buttonfour.fillcolor() == "red" and buttonfive.fillcolor() == "red" and buttonsix.fillcolor() == "red":
        cut_operation_red()
    elif buttonseven.fillcolor() == "red" and buttoneight.fillcolor() == "red" and buttonnine.fillcolor() == "red":
        cut_operation_red()
    elif buttonone.fillcolor() == "red" and buttonfour.fillcolor() == "red" and buttonseven.fillcolor() == "red":
        cut_operation_red()
    elif buttontwo.fillcolor() == "red" and buttonfive.fillcolor() == "red" and buttoneight.fillcolor() == "red":
        cut_operation_red()
    elif buttonthree.fillcolor() == "red" and buttonsix.fillcolor() == "red" and buttonnine.fillcolor() == "red":
        cut_operation_red()

    elif buttonone.fillcolor() == "red" and buttonfive.fillcolor() == "red" and buttonnine.fillcolor() == "red":
        cut_operation_red()
    elif buttonseven.fillcolor() == "red" and buttonfive.fillcolor() == "red" and buttonthree.fillcolor() == "red":
        cut_operation_red()


def check_blue():
    if buttonone.fillcolor() == "blue" and buttontwo.fillcolor() == "blue" and buttonthree.fillcolor() == "blue":
        cut_operation_blue()
    elif buttonfour.fillcolor() == "blue" and buttonfive.fillcolor() == "blue" and buttonsix.fillcolor() == "blue":
        cut_operation_blue()
    elif buttonseven.fillcolor() == "blue" and buttoneight.fillcolor() == "blue" and buttonnine.fillcolor() == "blue":
        cut_operation_blue()
    elif buttonone.fillcolor() == "blue" and buttonfour.fillcolor() == "blue" and buttonseven.fillcolor() == "blue":
        cut_operation_blue()
    elif buttontwo.fillcolor() == "blue" and buttonfive.fillcolor() == "blue" and buttoneight.fillcolor() == "blue":
        cut_operation_blue()
    elif buttonthree.fillcolor() == "blue" and buttonsix.fillcolor() == "blue" and buttonnine.fillcolor() == "blue":
        cut_operation_blue()

    elif buttonone.fillcolor() == "blue" and buttonfive.fillcolor() == "blue" and buttonnine.fillcolor() == "blue":
        cut_operation_blue()
    elif buttonseven.fillcolor() == "blue" and buttonfive.fillcolor() == "blue" and buttonthree.fillcolor() == "blue":
        cut_operation_blue()

    elif main.draw_count == 10:
        victory.write("DRAW!", align='center', font=('Arial', 20, 'bold'))
        main.draw_count = 1
        time.sleep(0.75)
        buttonone.reset()
        buttontwo.reset()
        buttonthree.reset()
        buttonfour.reset()
        buttonfive.reset()
        buttonsix.reset()
        buttonseven.reset()
        buttoneight.reset()
        buttonnine.reset()

        victory.reset()

        OFA()


redW = 0
def cut_operation_red():
    main.draw_count = 1
    red.reset()
    red_wins()
    main.redW = main.redW + 1
    victory.write("Red wins!", align='center', font=('Arial', 20, 'bold'))
    red.write("Red wins: " + str(redW), align='center', font=('Arial', 20, 'bold'))

    time.sleep(0.75)
    buttonone.reset()
    buttontwo.reset()
    buttonthree.reset()
    buttonfour.reset()
    buttonfive.reset()
    buttonsix.reset()
    buttonseven.reset()
    buttoneight.reset()
    buttonnine.reset()

    victory.reset()

    OFA()

blueW = 0
def cut_operation_blue():
    main.draw_count = 1
    blue.reset()
    blue_wins()
    main.blueW = main.blueW + 1
    victory.write("Blue wins!", align='center', font=('Arial', 20, 'bold'))
    blue.write("Blue wins: " + str(blueW), align='center', font=('Arial', 20, 'bold'))

    time.sleep(1)
    buttonone.reset()
    buttontwo.reset()
    buttonthree.reset()
    buttonfour.reset()
    buttonfive.reset()
    buttonsix.reset()
    buttonseven.reset()
    buttoneight.reset()
    buttonnine.reset()

    victory.reset()

    OFA()


def end_all(x, y):
    sys.exit()


OFA()
end_button()

screen.mainloop()
