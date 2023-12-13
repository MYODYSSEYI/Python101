# import turtle
#
# # Create a turtle named 't'
# t = turtle.Turtle()
# # Set the speed of the turtle
# t.speed(1)
#
# # Drawing a square
# for _ in range(4):
#     t.forward(100) # Move forward by 100 units
#     t.right(90)    # Turn right by 90 degrees
#
# # Complete the drawing
# turtle.done()
#

from tkinter import *

root = Tk(className = "breakdown.exe")
root.geometry("500x300")

lbl = Label(root, text = "hello")
lbl.pack()

root.mainloop()
