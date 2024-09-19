BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
import csv
key = {}
to_learn = {}
learnt_words = {}
timer = None



try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def word_to_learn():
    global learnt_words


    try:


        to_learn.remove(key)
        data = pandas.DataFrame(to_learn)
        data.to_csv("words_to_learns.csv", index=False)
        print(to_learn)
        learnt_words[f"{key["French"]}"] = f"{key["English"]}"
        print(learnt_words)
        with open("learning_data.txt", "w") as f:
            for item in learnt_words:
                f.writelines(f"{learnt_words[item]} : f{item} \n")


        next_card()

    except:
        next_card()




def next_card():

    global key, flip_timer
    window.after_cancel(flip_timer)
    key = random.choice(to_learn)




#to fix bug multi-clicking the button
    canvas.itemconfig(the_word, text=f"{key["French"]}", fil="black")
    canvas.itemconfig(the_title, text="French", fil="black")
    canvas.itemconfig(card_bg, image=back_image)
    window.after(3000, func=flip_card)



def flip_card():
    global key
    canvas.itemconfig(card_bg,image=card_image)
    canvas.itemconfig(the_word, text=f"{key["English"]}", fil="white")
    canvas.itemconfig(the_title, text="English", fil="white")


#-------------------------------UI--------------------#

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness= 0)
back_image = PhotoImage(file="images/card_front.png")
card_image = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=back_image)
the_title= canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
the_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#button

true_image = PhotoImage(file="images/right.png")
true_button = Button(image=true_image, highlightthickness= 0, command=word_to_learn)
true_button.grid(row=1,column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button =Button(image=wrong_image, highlightthickness= 0, command=next_card)
wrong_button.grid(row=1,column=0)



window.mainloop()
