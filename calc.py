from tkinter import *
import keyboard

# GUI 
calc = Tk()
calc.geometry("312x283")
calc.resizable(0,0)
calc.title("Calculator")

# Functions

# Adds the number to the expression and display when a number button is pressed
def numbtn(num):
    global expression
    global disp_exp
    if (expression != "" and expression[-1] in ".+-" and num in "+-") or (expression != "" and expression[-1] == "." and num == "."):
        expression = expression
    else:
        expression = expression + str(num)
        disp_exp = disp_exp + str(num)
        display.set(disp_exp)

# Makes the display of division sign look better in GUI while maintaining its function
def divbtn():
    global expression
    global disp_exp
    if (expression == "") or (expression != "" and expression[-1] in ".+-*/"):
        expression = expression
    else:
        expression = expression + str("/")
        disp_exp = disp_exp + str("÷")
        display.set(disp_exp)

# Makes the display of multiplication sign look better in GUI while maintaining its function
def multiplybtn():
    global expression
    global disp_exp
    if (expression == "") or (expression != "" and expression[-1] in ".+-*/"):
        expression = expression
    else:
        expression = expression + str("*")
        disp_exp = disp_exp + str("×")
        display.set(disp_exp)

# Deletes the last character in the expression and GUI, backspace
def backspace():
    global expression
    global disp_exp
    expression = expression[:-1]
    disp_exp = disp_exp[:-1]
    display.set(disp_exp)

# Clears the stored expression, reset calculator
def clearbtn():
    global expression
    global disp_exp
    expression = ""
    disp_exp = ""
    display.set(disp_exp)

# Evaluates the entered expression and display result, then automatically clears the stored expression
def equalbtn():
    global expression
    global disp_exp
    result = str(eval(expression))
    result_modified = result.rstrip("0").rstrip(".") if "." in result else result
    display.set(result_modified)
    expression = result_modified
    disp_exp = result_modified

# Detects keyboard input
def key_input(event):
    key = event.name
    if key.isdigit() or key in ["+", "-", "*", "/", ".", "(", ")"]:
        numbtn(key) if key.isdigit() or key in "0123456789" else None
        numbtn("+") if key == "+" else None
        numbtn("-") if key == "-" else None
        multiplybtn() if key == "*" else None
        divbtn() if key == "/" else None
        numbtn(".") if key == "." else None
        numbtn("(") if key == "(" else None
        numbtn(")") if key == ")" else None
    elif key == "enter":
        equalbtn()
    elif key == "backspace":
        backspace()
    elif key == "esc":
        clearbtn()

# Enables keyboard input listener when window is active, disables previous listeners if any
def start_key_cap():
    keyboard.unhook_all()
    keyboard.on_press(key_input)

# Disables keyboard input listener when window is not active
def stop_key_cap():
    keyboard.unhook_all()

expression = "" # Default values of expression and display
disp_exp = ""

# Window focus events to start and stop keyboard capturing
calc.bind("<FocusIn>", lambda event: start_key_cap())
calc.bind("<FocusOut>", lambda event: stop_key_cap())

# GUI

display = StringVar()
inputframe = Frame(calc, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
inputframe.pack(side=TOP)

inputfield = Entry(inputframe, font=("ariel", 20, "bold"), textvariable=display, width=50, bg="#eee", bd=0, justify=RIGHT, state="readonly")
inputfield.grid(row=0, column=0)
inputfield.pack(ipady=10)

btnframe = Frame(calc, width=312, height=172.5, bg="grey")
btnframe.pack()

btnwidth = 5
btnheight = 1

clear = Button(btnframe, text="C", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#eee", cursor="hand2", command=lambda: clearbtn()).grid(row=0, column=0, padx=1, pady=1)
openbrac = Button(btnframe, text="(", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#eee", cursor="hand2", command=lambda: numbtn("(")).grid(row=0, column=1, padx=1, pady=1)
closebrac = Button(btnframe, text=")", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#eee", cursor="hand2", command=lambda: numbtn(")")).grid(row=0, column=2, padx=1, pady=1)
divide = Button(btnframe, text="÷", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#eee", cursor="hand2", command=lambda: divbtn()).grid(row=0, column=3, padx=1, pady=1)

seven = Button(btnframe, text="7", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#fff", cursor="hand2", command=lambda: numbtn(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btnframe, text="8", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#fff", cursor="hand2", command=lambda: numbtn(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btnframe, text="9", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#fff", cursor="hand2", command=lambda: numbtn(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btnframe, text="×", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#eee", cursor="hand2", command=lambda: multiplybtn()).grid(row=1, column=3, padx=1, pady=1)

four = Button(btnframe, text="4", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#fff", cursor="hand2", command=lambda: numbtn(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btnframe, text="5", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#fff", cursor="hand2", command=lambda: numbtn(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btnframe, text="6", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#fff", cursor="hand2", command=lambda: numbtn(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btnframe, text="-", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#eee", cursor="hand2", command=lambda: numbtn("-")).grid(row=2, column=3, padx=1, pady=1)

one = Button(btnframe, text="1", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#fff", cursor="hand2", command=lambda: numbtn(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btnframe, text="2", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#fff", cursor="hand2", command=lambda: numbtn(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btnframe, text="3", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#fff", cursor="hand2", command=lambda: numbtn(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btnframe, text="+", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#eee", cursor="hand2", command=lambda: numbtn("+")).grid(row=3, column=3, padx=1, pady=1)

back = Button(btnframe, text="⌫", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#eee", cursor="hand2", command=lambda: backspace()).grid(row=4, column=0, padx=1, pady=1)
zero = Button(btnframe, text="0", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#fff", cursor="hand2", command=lambda: numbtn(0)).grid(row=4, column=1, padx=1, pady=1)
point = Button(btnframe, text=".", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#eee", cursor="hand2", command=lambda: numbtn(".")).grid(row=4, column=2, padx=1, pady=1)
equal = Button(btnframe, text="=", font=("ariel 18"), fg="black", width=btnwidth, height=btnheight, bd=0, bg="#eee", cursor="hand2", command=lambda: equalbtn()).grid(row=4, column=3, padx=1, pady=1)


calc.mainloop()