import os
from tkinter import *
from pygame import mixer
import tkinter.messagebox
from tkinter import filedialog


root = Tk()


middleframe = Frame(root)



#config tapbar
menuBar = Menu(root)
root.config(menu=menuBar)
#make topbar
def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)
subMenu = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Open",command=browse_file)
subMenu.add_command(label="Exit",command=root.destroy)

def about_us():
    tkinter.messagebox.showinfo("About Player 360","It is light and safe music player  https://github.com/sasa6277")

subMenu = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="About Us",command=about_us)



mixer.init() #initializeing the mixer


root.geometry('300x150')
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
    try:
        paused
    except NameError:    
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Playin Music" + " - " + os.path.basename(filename)
            print("play button")
        except:
            tkinter.messagebox.showerror('File not found','Player 360 could not open music')
    else:
        statusbar['text'] = "Resumed Music" + " - " + os.path.basename(filename)
        mixer.music.unpause()
        
def stop_btn():
    mixer.music.stop()
    statusbar['text'] = "Stop Music"
    print("stop button")


def next_btn():
    print("next button")


def previous_btn():
    print("previous button")

def pause_btn():
    global paused
    paused = TRUE
    statusbar['text'] = "Paused Music" + " - " + os.path.basename(filename)
    mixer.music.pause()
    print("pause button")
def val_btn(val):
    volume = int(val) /100
    mixer.music.set_volume(volume)


middleframe.pack()
playtBtn = Button(middleframe,image=playimg,command=play_btn).grid(row=0,column=1,padx=2)
stopBtn = Button(middleframe,image=stopimg,command=stop_btn).grid(row=0,column=2,padx=2)
pauseBtn = Button(middleframe,image=pauseimg,command=pause_btn).grid(row=0,column=3,padx=2)
nextBtn = Button(middleframe,image=nextimg,command=next_btn).grid(row=0,column=4,padx=2)
previousBtn = Button(middleframe,image=previousimg,command=previous_btn).grid(row=0,column=0,padx=2)
scale = Scale(root,from_=0,to=100,orient=HORIZONTAL,command=val_btn)
scale.set(70)
scale.pack()

#Label(root,text="Welcome to Player360",relief=SUNKEN,anchor=W).pack(side=BOTTOM)

statusbar = Label(root,text="Welcome to Player360",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()