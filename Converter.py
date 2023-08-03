'''from tkinter import *
win = Tk()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d" % (width, height))
win.title(" UnitConverter by AdamUltra")
win.mainloop()'''


def ask():
    UInp = int(input('enter number'))
    result = (UInp * 9 / 5) + 32
    print('The equivalent fahrenheit degree is', result)
    ask()


ask()
