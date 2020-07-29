from tkinter import *


root = Tk()
root.geometry('300x300')
root.title("Player360")
root.iconbitmap(r'../ico/360icon.ico')

text = Label(root,text="Music Player")
text.pack()

playimg = PhotoImage(file="../ico/play.png")
stopimg = PhotoImage(file="../ico/stop.png")
nextimg = PhotoImage(file="../ico/next.png")
previousimg = PhotoImage(file="../ico/previous.png")



def play_btn():
    print("play button")

def stop_btn():
    print("stop button")


def next_btn():
    print("next button")


def previous_btn():
    print("previous button")



playtBtn = Button(root,image=playimg,command=play_btn).pack()
stopBtn = Button(root,image=stopimg,command=stop_btn).pack()
nextBtn = Button(root,image=nextimg,command=next_btn).pack()
previousBtn = Button(root,image=previousimg,command=previous_btn).pack()

root.mainloop()