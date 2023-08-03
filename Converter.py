'''from tkinter import *
win = Tk()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d" % (width, height))
win.title(" UnitConverter by AdamUltra")
win.mainloop()'''


def ask():
    UInp = str(input('Enter 1 to do Celsius to Fahrenheit\nEnter 2 to do Fahrenheit to Celsius'))
    if UInp == '1':
        UInp = int(input('enter number'))
        result = (UInp * 9 / 5) + 32
        print('The equivalent Fahrenheit degree is', result)
        ask()

    elif UInp == '2':
        UInp = int(input('enter number'))
        result = (UInp - 32) * 5/9
        print('The equivalent Celsius degree is', result)
        ask()


ask()
