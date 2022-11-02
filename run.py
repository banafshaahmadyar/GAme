from tkinter import *
import time

window = Tk()
window.title("Digital clock")
window.geometry('400x150')


def mytime():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    am_pm=time.strftime('%p')
    day=time.strftime('%A')
    zone=time.strftime('%Z')
    myText = hour + ":" + minute + ":" + second + ":" +am_pm
    myText2=day + ","+zone
    myLabel.config(text=myText)
    myLabel2.config(text=myText2)
    myLabel.after(1000, mytime)


myLabel = Label(window, text="", font=("DS-digital", 50,"bold"), background='black',foreground='cyan')

myLabel.pack()
myLabel2 = Label(window,text="",font=("arail",15))
myLabel2.pack()
mytime()

window.mainloop()
