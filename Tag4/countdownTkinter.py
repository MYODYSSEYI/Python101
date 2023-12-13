from tkinter import *
import time 

root = Tk()

# Window Titel and Size
root.title("Countdown.exe")
root.geometry("700x500")

def countdownAnzeigen():
    eingabe = int(eingabefeld.get())
    while int(eingabe) >= 0:
        lblcountdown.config(text=eingabe)
        eingabe -= 1
        time.sleep(1)

eingabefeld = Entry(root)
eingabefeld.pack()

lblcountdown = Label(root, text="")
lblcountdown.pack()

button = Button(root, text="Start Countdown", command=countdownAnzeigen)
button.pack()

root.mainloop()
