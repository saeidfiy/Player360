from tkinter import *
from pygame import mixer
import tkinter.messagebox


root = Tk()


#config tapbar
menuBar = Menu(root)
root.config(menu=menuBar)
#make topbar
subMenu = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Open")
subMenu.add_command(label="Exit",command=root.destroy)

def about_us():
    tkinter.messagebox.showinfo("About Player 360","It is light and safe music player  https://github.com/sasa6277")

subMenu = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="About Us",command=about_us)



mixer.init() #initializeing the mixer


root.geometry('300x300')
root.title("Player360")
root.iconbitmap(r'../ico/360icon.ico')

text = Label(root,text="Music Player")
text.pack()







playimg = PhotoImage(file="../ico/play.png")
stopimg = PhotoImage(file="../ico/stop.png")
nextimg = PhotoImage(file="../ico/next.png")
previousimg = PhotoImage(file="../ico/previous.png")
pauseimg = PhotoImage(file="../ico/pause.png")



def play_btn():
    mixer.music.load("../test.mp3")
    mixer.music.play()
    print("play button")

def stop_btn():
    mixer.music.stop()
    print("stop button")


def next_btn():
    print("next button")


def previous_btn():
    print("previous button")

def pause_btn():
    print("pause button")
def val_btn(val):
    volume = int(val) /100
    mixer.music.set_volume(volume)



playtBtn = Button(root,image=playimg,command=play_btn).pack()
stopBtn = Button(root,image=stopimg,command=stop_btn).pack()
pauseBtn = Button(root,image=pauseimg,command=pause_btn).pack()
nextBtn = Button(root,image=nextimg,command=next_btn).pack()
previousBtn = Button(root,image=previousimg,command=previous_btn).pack()

scale = Scale(root,from_=0,to=100,orient=HORIZONTAL,command=val_btn)
scale.set(70)
scale.pack()

root.mainloop()