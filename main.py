"""
This is a calculator that performs simple mathematical inputs using the buttons and typing it in.
Created by: Hashir Sami
Date: Dec 25, 2021
"""

#dependicies
from tkinter import *
from tkinter_custom_button import TkinterCustomButton
import string,math

#initialize the calculator window
root = Tk()
root.title("Calculator")
root.resizable(False, False)
root.configure(bg="#535e64")

#input box
e = Entry(root, width=25,borderwidth=5, background="#a8ae8f", readonlybackground="#a8ae8f", font=("Times New Roman", 25))
e.grid(row=0, column=0, columnspan=4)

#functions for adding input via buttons
def button_click(number):
    e.insert(END, number)

def btn_clear(*event):
    e.configure(state="normal")
    e.delete(0, END)

def btn_add(*event):
    e.insert(END, "+")

def btn_minus(*event):
    e.insert(END, "-")    

def btn_multiply(*event):
    e.insert(END, "*")

def btn_divide(*event):
    e.insert(END, "/")

def btn_pi():
    e.insert(END, "\u03C0")

def btn_b1(*event):
    e.insert(END, "(")

def btn_b2(*event):
    e.insert(END, ")")

#calculate the input
def calculate(*event):

    #try-except in case there are errors in the user input
    try:

        #get input
        current = e.get()

        #list of not allowed characters
        notAllowed = list(string.ascii_letters + "!@#$%^&|\{\}\[\];:\'\",.?")

        #check if characters are in input
        if not(any(item in notAllowed for item in current)):

            current = list(current)

            #iterates through input to replace pi and brackets with acceptable calculation things
            for x in range(len(current)):
                if current[x] != current[0] and current[x-1].isdigit():
                    current[x] = current[x].replace("\u03C0", "*"+str(math.pi)) 
                    current[x] = current[x].replace("(", "*(") 

                elif current[x] != current[-1] and current[x+1].isdigit():
                    current[x] = current[x].replace("\u03C0", str(math.pi)+"*")
                    current[x] = current[x].replace(")", ")*") 
                else:
                    current[x] = current[x].replace("\u03C0", str(math.pi))

            # use python eval to perform calculations
            default = ""
            default = default.join(current)
            total = eval(default)

            # update to show, make readonly so user can't edit
            e.delete(0, END)
            e.insert(0, total)
            e.configure(state="readonly")

        # if there is no proper input, force an exception
        else:
            raise ValueError

    except:
        e.delete(0, END)
        e.insert(0, "Err")
        e.configure(state="readonly")

# initialize buttons 
button_1 = TkinterCustomButton(text="1",width=75, fg_color= "#868ba6", hover_color="#9FA4C4",corner_radius = 10, command=lambda: button_click(1))
button_2 = TkinterCustomButton(text="2", width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=lambda: button_click(2))
button_3 = TkinterCustomButton(text="3", width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=lambda: button_click(3))
button_4 = TkinterCustomButton(text="4", width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=lambda: button_click(4))
button_5 = TkinterCustomButton(text="5", width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=lambda: button_click(5))
button_6 = TkinterCustomButton(text="6", width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=lambda: button_click(6))
button_7 = TkinterCustomButton(text="7", width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=lambda: button_click(7))
button_8 = TkinterCustomButton(text="8", width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=lambda: button_click(8))
button_9 = TkinterCustomButton(text="9", width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=lambda: button_click(9))
button_0 = TkinterCustomButton(text="0", width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=lambda: button_click(0))
button_pi = TkinterCustomButton(text="\u03C0", height=50, width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=btn_pi)
button_b1 = TkinterCustomButton(text="(", height=50,width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=btn_b1)
button_b2 = TkinterCustomButton(text=")", height=50,width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=btn_b2)
button_add = TkinterCustomButton(text="+", width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=btn_add)
button_minus = TkinterCustomButton(text="-",width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=btn_minus)
button_multiply = TkinterCustomButton(text="*", width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=btn_multiply)
button_divide = TkinterCustomButton(text="/", width=75, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=btn_divide)
button_equal = TkinterCustomButton(text="=", width=160, fg_color= "#868ba6",hover_color="#9FA4C4",corner_radius = 10, command=calculate)
button_clear = TkinterCustomButton(text="Clear", height=50, width=75, fg_color= "#cd6181",hover_color="#f07194",corner_radius = 10, command=btn_clear)

# place buttons on grind
button_clear.grid(row=1, column=0)
button_pi.grid(row=1, column=1)
button_b1.grid(row=1, column=2)
button_b2.grid(row=1, column=3, pady=10)

button_7.grid(row=2, column=0, padx=10, pady=10)
button_8.grid(row=2, column=1, padx=10, pady=10)
button_9.grid(row=2, column=2, padx=10, pady=10)
button_add.grid(row=2, column=3, padx=10, pady=10)

button_4.grid(row=3, column=0, padx=10, pady=10)
button_5.grid(row=3, column=1, padx=10, pady=10)
button_6.grid(row=3, column=2, padx=10, pady=10)
button_minus.grid(row=3, column=3, padx=10, pady=10)

button_1.grid(row=4, column=0, padx=10, pady=10)
button_2.grid(row=4, column=1, padx=10, pady=10)
button_3.grid(row=4, column=2, padx=10, pady=10)
button_multiply.grid(row=4, column=3, padx=10, pady=10)

button_0.grid(row=5, column=0, padx=10, pady=10)
button_equal.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
button_divide.grid(row=5, column=3, padx=10, pady=10)

# bind specific keys to buttons
root.bind("<Return>", calculate)
root.bind("<c>", btn_clear)

root.mainloop()