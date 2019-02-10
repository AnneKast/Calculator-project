from tkinter import *

calc = Tk()

formula =""

equation = StringVar()
equation.set("0")

calculation = Label(calc, textvariable = equation)
calculation.grid(row=0, columnspan=4)

def pressBut(num):
    global formula
    formula = formula + str(num)
    equation.set(formula)

def equalBut():
    global formula
    #evaluates the string to see if it can be turned into a calculation
    result = str(eval(formula))
    equation.set(result)
    formula = ""

def clearBut():
    global formula
    formula = ""
    equation.set(formula)

#unless we press, the function will not be executed (lambda function) "anon. func."
Button1 = Button(calc,text="1", padx=15, pady=15, command= lambda: pressBut(1))
Button1.grid(row=1, column=0)

Button2 = Button(calc,text="2", padx=15, pady=15, command= lambda: pressBut(2))
Button2.grid(row=1, column=1)

Button3 = Button(calc,text="3", padx=15, pady=15, command= lambda: pressBut(3))
Button3.grid(row=1, column=2)

Button4 = Button(calc,text="+", padx=15, pady=15, command= lambda: pressBut("+"))
Button4.grid(row=1, column=3)

Button5 = Button(calc,text="4", padx=15, pady=15, command= lambda: pressBut(4))
Button5.grid(row=2, column=0)

Button6 = Button(calc,text="5", padx=15, pady=15, command= lambda: pressBut(5))
Button6.grid(row=2, column=1)

Button7 = Button(calc,text="6", padx=15, pady=15, command= lambda: pressBut(6))
Button7.grid(row=2, column=2)

Button8 = Button(calc,text="-", padx=15, pady=15, command= lambda: pressBut("-"))
Button8.grid(row=2, column=3)

Button9 = Button(calc,text="7", padx=15, pady=15, command= lambda: pressBut(7))
Button9.grid(row=3, column=0)

Button10 = Button(calc,text="8", padx=15, pady=15, command= lambda: pressBut(8))
Button10.grid(row=3, column=1)

Button11 = Button(calc,text="9", padx=15, pady=15, command= lambda: pressBut(9))
Button11.grid(row=3, column=2)

Button12 = Button(calc,text="*", padx=15, pady=15, command= lambda: pressBut("*"))
Button12.grid(row=3, column=3)

Button13 = Button(calc,text="0", padx=15, pady=15, command= lambda: pressBut(0))
Button13.grid(row=4, column=0)

Button14 = Button(calc,text="C", padx=15, pady=15, command= clearBut)
Button14.grid(row=4, column=1)

Button15 = Button(calc,text="=", padx=15, pady=15, command= equalBut)
Button15.grid(row=4, column=2)

Button16 = Button(calc,text="/", padx=15, pady=15, command= lambda: pressBut("/"))
Button16.grid(row=4, column=3)

calc.mainloop()
