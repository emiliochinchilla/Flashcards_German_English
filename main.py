from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# ---------------------------- GET WORDS FROM DATA BASE ------------------------------- #
try:
    data = pandas.read_csv("data\words_to_learn.csv") #Try using existing save file
except FileNotFoundError:
    original_data = pandas.read_csv("data\german_words.csv")  # create DataFrame with all words if there is no existing saved file
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")  # Create dictionary. records {column: value}

#
# random_index = random.choice(list(word_dict["German"]))
def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title, text="German", fill="black")
    canvas.itemconfig(words, text=current_card["German"], fill="black")
    timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(words, text=current_card["English"], fill="white")

def is_known():
    global current_card
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data\words_to_learn.csv", index=False) # index=False is so pandas doesnt add the index each time a DF is converted to csv



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0) #size of the image 800x526
card_front_img = PhotoImage(file="images\card_front.png")
card_back_img = PhotoImage(file="images\card_back.png")
canvas_image = canvas.create_image(400, 263, image = card_front_img) #create and center img
title = canvas.create_text(400, 150, text="Title", font = ("Ariel", 40, "italic"))
words = canvas.create_text(400, 263, text="Word", font = ("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, stick="EW", columnspan = 2)

#Buttons
wrong_btn_img = PhotoImage(file="images\\wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_btn.grid(column=0, row=1)

right_btn_img = PhotoImage(file="images\\right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_btn.grid(column=1, row=1)

next_card()

mainloop()