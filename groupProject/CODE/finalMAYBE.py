import tkinter.font as tkfont
import tkinter as tk
import tkinter.filedialog as filedialog
import random
import os
import sys


def restart_program():
    """Restarts the current program, with file objects and descriptors
    cleanup performed by Python's garbage collector.
    """
    os.execv(sys.executable, ["python"] + sys.argv)


# window management
def show_frame(frame):
    frame.pack(fill=tk.BOTH, expand=1)


def hide_frame(frame):
    frame.pack_forget()


def switch_view1_2():
    hide_frame(frame1)
    show_frame(frame2)


def switch_view1_3():
    hide_frame(frame1)
    show_frame(frame3)


def switch_view1_4():
    hide_frame(frame1)
    show_frame(frame4)
    display_random_question()


def set_background(frame, image_path):
    # Load the image
    image = tk.PhotoImage(file=image_path)

    # Downscale the image to a fifth of its size
    image = image.subsample(4)

    # Create a label with the image
    background_label = tk.Label(frame, image=image)
    background_label.image = (
        image  # Keep a reference to the image to prevent garbage collection
    )

    # Place the label at the top left corner and make it cover the entire frame
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Data management
data_dict = {
    "difficulty": {
        "new": {},
        "hard": {},
        "mid": {},
        "ez": {},
    },
}

# Create a dictionary to update the data_dict
updated_data_dict = {
    "difficulty": {
        "new": {},
        "hard": {},
        "mid": {},
        "ez": {},
    },
}

# Create the main window
window = tk.Tk()
window.title("Flash Card App")
window.geometry("425x320")

# Menu
frame1 = tk.Frame(window)

# set_background(frame1, "CODE/Images/background.gif")

# Set the system font and configure the title label
system_font = tkfont.Font(family="System", size=40, weight="bold")
title_label = tk.Label(window, text="PY-Cards", font=system_font)

# Place the title label at the center of the window
title_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# ...


# Create the buttons
createButton = tk.Button(frame1, text="Create Cards", command=switch_view1_2)
cardpacksButton = tk.Button(frame1, text="Card Packs", command=switch_view1_3)
reviewButton = tk.Button(frame1, text="Review Cards", command=switch_view1_4)

# Place the buttons at the bottom next to each other
createButton.pack(side="left", anchor="sw")
cardpacksButton.pack(side="left", anchor="s")
reviewButton.pack(side="left", anchor="se")

# Resize the buttons
createButton.configure(width=12, height=1)
cardpacksButton.configure(width=12, height=1)
reviewButton.configure(width=12, height=1)

# Creation Frame
frame2 = tk.Frame(window)

# set_background(frame2, "CODE/Images/background.gif")

questionLabel = tk.Label(frame2, text="Question:")
answerLabel = tk.Label(frame2, text="Answer:")

questionInput = tk.Entry(frame2)
answerInput = tk.Entry(frame2)

questionLabel.pack()
questionInput.pack()
answerLabel.pack()
answerInput.pack()


def save_input_data():
    question = questionInput.get()
    answer = answerInput.get()
    data_dict["difficulty"]["new"][question] = answer
    questionInput.delete(0, tk.END)
    answerInput.delete(0, tk.END)


def save_dictionary():
    file_path = filedialog.asksaveasfilename(
        initialdir=os.path.join(os.path.dirname(__file__), "CardPacks"),
        title="Save Dictionary",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")),
    )
    if file_path:
        with open(file_path, "w") as f:
            for difficulty, questions in data_dict["difficulty"].items():
                for question, answer in questions.items():
                    f.write(f"{difficulty}:{question}:{answer}\n")
    restart_program()


saveButton = tk.Button(frame2, text="Save", command=save_dictionary)
saveButton.pack(anchor="s")


confirmButton = tk.Button(frame2, text="Confirm", command=save_input_data)
confirmButton.pack(anchor="s")

# Card Pack Frame

frame3 = tk.Frame(window)

# set_background(frame3, "CODE/Images/background.gif")


# Function to get the list of text files in the CardPacks directory
def get_cardpack_files():
    cardpack_dir = os.path.join(os.path.dirname(__file__), "CardPacks")
    cardpack_files = [
        f
        for f in os.listdir(cardpack_dir)
        if os.path.isfile(os.path.join(cardpack_dir, f))
    ]
    return cardpack_files


# Function to fill the dictionary with file contents
def fill_dictionary(file):
    file_path = os.path.join(os.path.dirname(__file__), "CardPacks", file)
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            difficulty, question, answer = line.strip().split(":")
            data_dict["difficulty"][difficulty][question] = answer
    show_frame(frame1)
    hide_frame(frame3)


# Get the list of card pack files
cardpack_files = get_cardpack_files()

# Create a label for each card pack file
selected_file = None  # Variable to store the selected filename


# Define the select_file function
def select_file(file):
    global selected_file
    selected_file = file
    fill_dictionary(file)


for file in cardpack_files:
    label = tk.Label(frame3, text=file)
    label.pack()

    # Button to select the file and store the filename
    select_button = tk.Button(
        frame3, text="Select", command=lambda file=file: select_file(file)
    )
    select_button.pack()

#! The code runs in an infinite loop we need to fix this...
#! The window is ugly and the answer button doesn't disapear when you click it and hides the question...
#! Background image doesn't work
# Review Frame
frame4 = tk.Frame(window)


# Write the data_dict to the file
def write_data_dict_to_file(selected_file):
    file_path = os.path.join(os.path.dirname(__file__), "CardPacks", selected_file)
    with open(file_path, "w") as f:
        for difficulty, questions in data_dict["difficulty"].items():
            for question, answer in questions.items():
                f.write(f"{difficulty}:{question}:{answer}\n")


def display_random_question():
    # set_background(frame4, "CODE/Images/background.gif")
    if data_dict["difficulty"]["new"] != {}:
        # Get a random question from the dictionary
        question = random.choice(list(data_dict["difficulty"]["new"].keys()))
        answer = data_dict["difficulty"]["new"][question]

        for widget in frame4.winfo_children():
            widget.destroy()

        # Display the question
        question_label = tk.Label(frame4, text=question)
        question_label.pack()

        # Button to show the answer
        answer_button = tk.Button(
            frame4, text="Show Answer", command=lambda: show_answer(answer)
        )
        answer_button.pack()

        # Function to hide the answer button
        def hide_answer_button():
            answer_button.pack_forget()

        # Modify the command of the answer button to hide it when clicked
        answer_button.configure(
            command=lambda: [show_answer(answer), hide_answer_button()]
        )

    elif data_dict["difficulty"]["hard"] != {}:
        question = random.choice(list(data_dict["difficulty"]["hard"].keys()))
        answer = data_dict["difficulty"]["hard"][question]

        for widget in frame4.winfo_children():
            widget.destroy()

        question_label = tk.Label(frame4, text=question)
        question_label.pack()

        answer_button = tk.Button(
            frame4, text="Show Answer", command=lambda: show_answer(answer)
        )
        answer_button.pack()

        # Function to hide the answer button
        def hide_answer_button():
            answer_button.pack_forget()

        # Modify the command of the answer button to hide it when clicked
        answer_button.configure(
            command=lambda: [show_answer(answer), hide_answer_button()]
        )
    elif data_dict["difficulty"]["mid"] != {}:
        question = random.choice(list(data_dict["difficulty"]["mid"].keys()))
        answer = data_dict["difficulty"]["mid"][question]

        for widget in frame4.winfo_children():
            widget.destroy()

        question_label = tk.Label(frame4, text=question)
        question_label.pack()

        answer_button = tk.Button(
            frame4, text="Show Answer", command=lambda: show_answer(answer)
        )
        answer_button.pack()

        # Function to hide the answer button
        def hide_answer_button():
            answer_button.pack_forget()

        # Modify the command of the answer button to hide it when clicked
        answer_button.configure(
            command=lambda: [show_answer(answer), hide_answer_button()]
        )

    else:
        # write_data_dict_to_file(selected_file)
        # Hide frame4 and show frame1
        frame4.pack_forget()
        frame1.pack()


# * =======================================< SHOW THE ASWER AND CHOOSE DIFFICULTY>==================================================
def show_answer(answer):
    # Display the answer
    answer_label = tk.Label(frame4, text=answer)
    answer_label.pack()

    # Buttons to rank the difficulty
    easy_button = tk.Button(frame4, text="Easy", command=lambda: rank_difficulty("ez"))
    mid_button = tk.Button(frame4, text="Mid", command=lambda: rank_difficulty("mid"))
    hard_button = tk.Button(
        frame4, text="Hard", command=lambda: rank_difficulty("hard")
    )
    easy_button.pack(side="left")
    mid_button.pack(side="left")
    hard_button.pack(side="left")


# * =======================================< delete old entry and replace it with new >=============================================
def rank_difficulty(difficulty):
    # Get the selected question and answer
    question = frame4.winfo_children()[0].cget("text")
    answer = frame4.winfo_children()[2].cget("text")

    print("\n", "Original\n", data_dict)

    if question in data_dict["difficulty"]["ez"] and difficulty != "ez":
        del updated_data_dict["difficulty"]["ez"][question]
    elif question in data_dict["difficulty"]["mid"] and difficulty != "mid":
        del updated_data_dict["difficulty"]["mid"][question]
    elif question in data_dict["difficulty"]["hard"] and difficulty != "hard":
        del updated_data_dict["difficulty"]["hard"][question]

    # Move the question and answer to the selected difficulty key
    updated_data_dict["difficulty"][difficulty][question] = answer
    print("\n", "Updated\n", updated_data_dict)

    # Remove the question and answer from the dictionary
    if (
        question in data_dict["difficulty"]["new"]
        and question not in updated_data_dict["difficulty"]["new"]
    ):
        del data_dict["difficulty"]["new"][question]
        if data_dict["difficulty"]["new"] == {}:
            data_dict.update(updated_data_dict)
            write_data_dict_to_file(selected_file)
    elif (
        question in data_dict["difficulty"]["hard"]
        and question not in updated_data_dict["difficulty"]["hard"]
    ):
        del data_dict["difficulty"]["hard"][question]
        if data_dict["difficulty"]["hard"] == {}:
            data_dict.update(updated_data_dict)
            write_data_dict_to_file(selected_file)
    elif (
        question in data_dict["difficulty"]["mid"]
        and question not in updated_data_dict["difficulty"]["mid"]
    ):
        del data_dict["difficulty"]["mid"][question]
        if data_dict["difficulty"]["mid"] == {}:
            data_dict.update(updated_data_dict)
            write_data_dict_to_file(selected_file)
    else:
        data_dict.update(updated_data_dict)
        write_data_dict_to_file(selected_file)

    print("\n", "Updated\n", updated_data_dict)
    print("\n", "Originial\n", data_dict)

    display_random_question()


# Show the first frame
show_frame(frame1)
# Start the main loop
window.mainloop()