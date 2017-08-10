
# The Archer Game PLay - This file contains the codes for all the functions to run the program.
# This file is called by the Archer Run App.

from Tkinter import *


def initialise(data):
    data.sL = 0
    data.sT = 250
    data.tL = 780
    data.tT = 250
    data.ax1 = data.sL + 10
    data.ay1 = data.sT + 40
    data.ax11 = data.sL + 10
    data.ay11 = data.sT + 40
    data.vx = 100
    data.vx1 = 100
    data.vy = 0
    data.vy1 = 0
    data.dt = 0.2
    data.ay = 9.8
    data.counter = 0
    data.state = 0
    data.score = 0
    data.gameOver = False
    data.state1 = 0
    data.state2 = 0

def moveTarget(data, dy):
    if (data.gameOver == False):

        data.tT += dy
        if (data.tT > 599):
            data.tT = -140

def drawArrow(canvas, data):
    if (data.gameOver == False):


        canvas.create_line(data.ax1, data.ay1,
                        data.ax1 + 60, data.ay1,
                       fill="blue", width=3)
        canvas.create_line(data.ax1 + 60, data.ay1,
                           data.ax1 + 60 - 10, data.ay1 - 10,
                           fill="blue", width=3)
        canvas.create_line(data.ax1 + 60, data.ay1,
                           data.ax1 + 60 - 10, data.ay1 + 10,
                           fill="blue", width=3)

def moveArrow(data):


    data.ax1 = data.ax1 + (data.vx * data.dt)
    data.ay1 = data.ay1 - (data.vy * data.dt)
    data.vy = data.vy - (data.ay * data.dt)


    if (data.ax1 + 60 > data.tL and data.ay1 >= data.tT and data.ay1 <= data.tT + 35):
        data.ax1 = data.ax11
        data.ay1 = data.ay11
        data.vx = data.vx1
        data.vy = data.vy1
        data.score += 10
        data.counter += 1
        data.state2 = 0

    if (data.ax1 + 60 > data.tL and data.ay1 > data.tT + 105 and data.ay1 <= data.tT + 140):
        data.ax1 = data.ax11
        data.ay1 = data.ay11
        data.vx = data.vx1
        data.vy = data.vy1
        data.score += 10
        data.counter += 1
        data.state2 = 0

    if (data.ax1 + 60 > data.tL and data.ay1 > data.tT + 35 and data.ay1 < data.tT + 60):
        data.ax1 = data.ax11
        data.ay1 = data.ay11
        data.vx = data.vx1
        data.vy = data.vy1
        data.score += 20
        data.counter += 1
        data.state2 = 0

    if (data.ax1 + 60 > data.tL and data.ay1 > data.tT + 80 and data.ay1 <= data.tT + 105):
        data.ax1 = data.ax11
        data.ay1 = data.ay11
        data.vx = data.vx1
        data.vy = data.vy1
        data.score += 20
        data.counter += 1
        data.state2 = 0

    if (data.ax1 + 60 > data.tL and data.ay1 >= data.tT + 60 and data.ay1 <= data.tT + 80):
        data.ax1 = data.ax11
        data.ay1 = data.ay11
        data.vx = data.vx1
        data.vy = data.vy1
        data.score += 30
        data.counter += 1
        data.state2 = 0

    if (data.ax1 + 60 > 810):
        data.ax1 = data.ax11
        data.ay1 = data.ay11
        data.vx = data.vx1
        data.vy = data.vy1
        data.counter += 1
        data.state2 = 0

    if (data.counter == 10):
        data.gameOver = True


def projectileVar(data, dvy):

    data.vy += dvy
    if (data.vy == 60):
        data.vy = 0

def timerFired(data):

    if (data.gameOver == False):
        moveTarget(data, 15)
        if data.state2 != 1:
            projectileVar(data,5)

def redrawAll(canvas, data):

    canvas.create_rectangle(data.sL, data.sT, data.sL + 20, data.sT + 80, fill="red")
    canvas.create_rectangle(data.tL, data.tT, data.tL + 25, data.tT + 140, fill="yellow")
    canvas.create_rectangle(data.tL, data.tT + 35, data.tL + 25, data.tT + 105, fill="orange")
    canvas.create_rectangle(data.tL, data.tT + 60, data.tL + 25, data.tT + 80, fill="red")
    drawArrow(canvas, data)

    if data.gameOver == True:
        canvas.create_rectangle(data.width // 4, data.height // 4, 3 * data.width // 4, 2 * data.height // 4, fill="black")
        canvas.create_text(data.width // 2, data.height // 3, text="""

    THE ARCHER

    Game Over

    Score = """ + str(data.score), fill="white")


def run(width, height):
    def redrawAllWrapper(canvas, data):

        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height, fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()


    def onClick (event):

            data.state2 = 1
            if (data.gameOver == False):
                while data.state2 == 1:
                    moveArrow(data)
                    redrawAllWrapper(canvas, data)



    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)


    class Struct(object): pass

    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 50

    initialise(data)

    root = Tk()
    root.title ("The Archer")

    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    canvas.bind("<Button>", onClick)

    timerFiredWrapper(canvas, data)

    root.mainloop()

run(800, 600)