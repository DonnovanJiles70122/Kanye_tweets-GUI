from tkinter import *
import kanye
import requests


def get_quote():
    canvas.itemconfig(quote_text, text=('"'+ kanye.quote() +'"'))




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="#A6D0DD")

canvas = Canvas(width=300, height=300, bg="#A6D0DD", highlightthickness=0)
background_img = PhotoImage(file="bubble.png")
canvas.create_image(150, 130, image=background_img)
quote_text = canvas.create_text(150, 130, text=('"'+ kanye.quote() +'"'), width=250, font=("Arial", 10, "bold"), fill="#FF6969")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye_head.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bg="#A6D0DD")
kanye_button.grid(row=1, column=0)


window.mainloop()