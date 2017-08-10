
# The Archer Run App - This file runs the main application.


from Tkinter import *
import os

root = Tk()
root.title("The Archer")

def onClick (event):
    root.destroy()
    os.system('python Archer_GamePlay.py')


canvas = Canvas(root, width=400, height=300)
canvas.pack()

play = Button (root, text="Start Game", activebackground= "Blue", height= 8, width= 8, relief= SUNKEN)
play.bind("<Button>", onClick)
play.pack()


image = PhotoImage(
    file="./bg1.gif")
canvas.create_image(200, 150, image=image, anchor=CENTER)


root.mainloop()
