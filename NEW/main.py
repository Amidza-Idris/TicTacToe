import sys
import time
from turtle import Screen, Turtle
import Values

screen = Screen()

class Miscellaneous:
    def __init__(self):
        self.button = Turtle()
        self.button.penup()
        self.button.hideturtle()
        self.button.speed(0)
        self.button.shape("square")

    def three_moves(self, fwd1=0, left2=0, fwd2=0):
        self.button.forward(fwd1)
        self.button.left(left2)
        self.button.forward(fwd2)


class Button:
    def __init__(self):
        self.button = Turtle()
        self.button.penup()
        self.button.speed(10)
        self.button.shape("square")
        self.button.shapesize(4, 4)
        self.button.fillcolor("gray")

        self.color = "gray"     # storing information for comparison since python dumb

        self.button.onclick(self.click)
        # this is very dumb, if you
        # put () when using onclick to call a function, it will run on click
        # as if it was called instantly. In order to avoid that, we must pass
        # the function without (), for example... bla.bla.onclick(click).
        # this will listen for clicks, while this bla.bla.onclick(click())
        # will execute instantly.

    # regarding optimization, I could have made a function with 3 moves only, but that takes space.

    def four_moves(self, left1=0, fwd1=0, left2=0, fwd2=0):
        self.button.left(left1)
        self.button.forward(fwd1)
        self.button.left(left2)
        self.button.forward(fwd2)

    def click(self, x=4, y=4):
        Values.draw_count = Values.draw_count + 1
        Values.counter = Values.counter + 1

        if self.get_color() == "red" or self.get_color() == "blue":
            Values.counter = Values.counter - 1
            return

        if Values.counter % 2 == 0:
            self.set_color("red")
        else:
            self.set_color("blue")

        if Values.counter >= 4:
            print("checking")
            self.check_red()
            # check_blue()

    def set_color(self, color):
        self.color = color
        self.button.fillcolor(color)

    def get_color(self):
        return self.color

    def check_red(self):
        win_combinations = [
            [buttonone, buttontwo, buttonthree],
            [buttonfour, buttonfive, buttonsix],
            [buttonseven, buttoneight, buttonnine],
            [buttonone, buttonfour, buttonseven],
            [buttontwo, buttonfive, buttoneight],
            [buttonthree, buttonsix, buttonnine],
            [buttonone, buttonfive, buttonnine],
            [buttonseven, buttonfive, buttonthree],
        ]
        for combination in win_combinations:
            if all(button.get_color() == "red" for button in combination):
                self.cut_operation_red()
                return
        for combination in win_combinations:
            if all(button.get_color() == "blue" for button in combination):
                self.cut_operation_blue()
                return

    def cut_operation_red(self):
        print("RED WON!")
        sys.exit()

    def cut_operation_blue(self):
        print("BLUE WON!")
        sys.exit()
# CALLING CLASS, TESTING AND ETC-------------------------------------------

buttonone = Button()
buttonone.four_moves(0, -100, 90, 100)

buttontwo = Button()
buttontwo.four_moves(0, 0, 90, 100)

buttonthree = Button()
buttonthree.four_moves(0, 100, 90, 100)

buttonfour = Button()
buttonfour.four_moves(0, -100)

buttonfive = Button()
buttonfive.four_moves()

buttonsix = Button()
buttonsix.four_moves(0, 100)

buttonseven = Button()
buttonseven.four_moves(-90, 100, -90, 100)

buttoneight = Button()
buttoneight.four_moves(-90, 100)

buttonnine = Button()
buttonnine.four_moves(-90, 100, 90, 100)


screen.mainloop()
