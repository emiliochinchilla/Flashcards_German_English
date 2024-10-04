from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- GET WORDS FROM DATA BASE ------------------------------- #
data = pandas.read_csv("data\german_words.csv") #create DataFrame
word_dict = data.to_dict(orient="records") #Create dictionary. records {column: value}
language = "German"
#
# random_index = random.choice(list(word_dict["German"]))
def next_card():
    random_word = random.choice(word_dict)[language]
    print(random_word)
    canvas.itemconfig(title, text=f"{language}")
    canvas.itemconfig(words, text=f"{random_word}")






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0) #size of the image 800x526
card_front_img = PhotoImage(file="images\card_front.png")
canvas.create_image(400, 263, image = card_front_img) #create and center img
title = canvas.create_text(400, 150, text="Title", font = ("Ariel", 40, "italic"))
words = canvas.create_text(400, 263, text="Word", font = ("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, stick="EW", columnspan = 2)

#Buttons
wrong_btn_img = PhotoImage(file="images\\wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_btn.grid(column=0, row=1)

right_btn_img = PhotoImage(file="images\\right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
right_btn.grid(column=1, row=1)

next_card()

mainloop()