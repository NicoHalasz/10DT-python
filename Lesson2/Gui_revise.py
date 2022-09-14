# Nico Halasz

# ***************************************************
# Python Calculator with GUI (Graphic User Interface)
# ***************************************************

from tkinter import * # import the tkinter library

def button_press(num):
    pass

def equals():
    pass

def clear():
    pass

window = Tk()
window.title("Python Calculator")
window.geometry("500x500")
window.configure(bg="grey")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("console", 20), bg="white", width=24, height=1)
label.pack()

frame = Frame(window)
frame.pack

button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)


window.mainloop()