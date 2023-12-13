import tkinter as tk
from tkinter import messagebox

# count button presses 
timesPressed = 0
def on_button_click():
    global timesPressed
    timesPressed += 1
    print(f"Button clicked {timesPressed}!")

# Create the main window
root = tk.Tk()
root.title("Basic Tkinter App")

# Rezise window 
window_width = 300
window_height = 200
root.geometry(f'{window_width}x{window_height}')

# Create a Label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()  # Place the label on the window

# Create a Button widget
button = tk.Button(root, 
                   text="Click Me", 
                   command=on_button_click, 
                   fg="white", 
                   bg="black")
button.pack()  # Place the button on the window

# Start the Tkinter event loop
root.mainloop()

