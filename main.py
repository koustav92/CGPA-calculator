import tkinter
from tkinter import *

root = Tk()
root.title("CGPA % Calculator")
root.geometry("600x600+100+200")
root.resizable()
root.configure(bg="#17161b")

equation=""

def show(value):
    global equation
    equation+=value
    result.config(text=equation)

def clear():
    global equation
    equation = ""
    result.config(text=equation)


def calculate():
    global equation
    try:
        num = float(equation)
        product = num * 9.5
    except ValueError:
        product = "error"
    except:
        product = "error"
    result.config(text=product)
    equation = ""


result = Label(root, width=25, height=2, font=("times new roman", 34), bg="#ADADAD", fg="#000000")
result.pack()

Button(root, text="7", width=5, height=1, font=("arial",30, "bold"), bd=1, bg="#000000", fg="#007FFF", command=lambda:show("7")).place(x=50, y=125)
Button(root, text="8", width=5, height=1, font=("arial",30, "bold"), bd=1, bg="#000000", fg="#007FFF", command=lambda:show("8")).place(x=185, y=125)
Button(root, text="9", width=5, height=1, font=("arial",30, "bold"), bd=1, bg="#000000", fg="#007FFF", command=lambda:show("9")).place(x=320, y=125)

Button(root, text="4", width=5, height=1, font=("arial",30, "bold"), bd=1, bg="#000000", fg="#007FFF", command=lambda:show("4")).place(x=50, y=225)
Button(root, text="5", width=5, height=1, font=("arial",30, "bold"), bd=1, bg="#000000", fg="#007FFF", command=lambda:show("5")).place(x=185, y=225)
Button(root, text="6", width=5, height=1, font=("arial",30, "bold"), bd=1,bg="#000000", fg="#007FFF", command=lambda:show("6")).place(x=320, y=225)

Button(root, text="1", width=5, height=1, font=("arial",30, "bold"), bd=1, bg="#000000", fg="#007FFF", command=lambda:show("1")).place(x=50, y=325)
Button(root, text="2", width=5, height=1, font=("arial",30, "bold"), bd=1, bg="#000000", fg="#007FFF", command=lambda:show("2")).place(x=185, y=325)
Button(root, text="3", width=5, height=1, font=("arial",30, "bold"), bd=1, bg="#000000", fg="#007FFF", command=lambda:show("3")).place(x=320, y=325)
Button(root, text="0", width=4, height=3, font=("arial",30, "bold"), bd=1, bg="#000000", fg="#007FFF", command=lambda:show("0")).place(x=455, y=225)

Button(root, text=".", width=4, height=1, font=("arial",30, "bold"), bd=1, bg="#000000",fg="#00FF00", command=lambda:show(".")).place(x=455, y=125)

Button(root, text="C", width=6, height=1, font=("arial",30, "bold"), bd=1, bg="#F08080", fg="#fff", command=lambda : clear()).place(x=330, y=425)

Button(root, text="Calculate", width=8, height=1, font=("arial",30, "bold"), bd=1, bg="#98F5FF",fg="#000000", command=lambda : calculate()).place(x=100, y=425)

root.mainloop()
