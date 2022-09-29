# Nico Halasz
# 15/09/2022

# ***************************************************
# Python Calculator with GUI (Graphic User Interface)
# ***************************************************

from tkinter import * 
from turtle import color # import the tkinter library

def button_press(num):   # defining each button press
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():   # this block checks for the button_press(equals)
    
    global equation_text

    try:  # try is used in try...expect blocks. It defines a block of ode test if it contains any errors.
          # You can define different blocks for different errpr types, and blocks to execute if nothing went wrong.
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError: # Check for syntax error

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:   # Check for division by zero

        equation_label.set("arithmetic error")

        equation_text = ""


def clear(): # Clears the equation_label for the next calculation
    global equation_label
    global equation_text

    equation_label.set("")

    equation_text = " "

window = Tk()
window.title("Python Calculator") # Set the name of the window
window.geometry("400x500") # Set the size of the window
window.configure(bg="royalblue4") # Set the background colour of the window

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('console', 20), bg="springgreen3", width=23, height=2)
label.pack()

frame = Frame(window)
frame.pack()

# create the buttons (0 - 9)

button1 = Button(frame, text=1, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, bg="cyan", activebackground="cadetblue1", command=lambda: button_press(0))
button0.grid(row=3, column=0)

# create the operation buttons

plus = Button(frame, text='+', height=4, width=9, font=35, bg="yellow2", activebackground="#E3CF57", command=lambda: button_press('+'))
plus.grid(row=1, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, bg="yellow2", activebackground="#E3CF57", command=lambda: button_press('-'))
minus.grid(row=2, column=3)

multiply = Button(frame, text='×', height=4, width=9, font=35, bg="yellow2", activebackground="#E3CF57", command=lambda: button_press('*'))
multiply.grid(row=3, column=2)

divide = Button(frame, text='÷', height=4, width=9, font=35, bg="yellow2", activebackground="#E3CF57", command=lambda: button_press('/'))
divide.grid(row=3, column=1)

# create equals

equal = Button(window, text='=', height=4, width=40, font=35, bg="brown1", activebackground="coral2", command=equals)
equal.pack()

# create decimal

decimal = Button(frame, text='.',  height=4, width=9, font=35, bg="yellow2", activebackground="#E3CF57", command=lambda: button_press('.'))
decimal.grid(row=3, column=3)

# create clear button

clear = Button(frame, text='Reset', height=4, width=9, font=35, bg="greenyellow", activebackground="olivedrab1", command=clear)
clear.grid(row=0, column=3)

window.mainloop()