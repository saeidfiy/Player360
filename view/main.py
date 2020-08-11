import os
import time
import threading
from tkinter import *
from pygame import mixer
import tkinter.messagebox
from mutagen.mp3 import MP3
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


root.geometry('300x200')
root.title("Player360")
root.iconbitmap(r'../ico/360icon.ico')

fileLable = Label(root,text="Music Player")
fileLable.pack()


fileLength = Label(root,text="Total Length : --:--")
fileLength.pack()

currentLengthLabel = Label(root,text="Current Length : --:--",relief = GROOVE)
currentLengthLabel.pack(pady=5)






playimg = PhotoImage(file="../ico/play.png")
stopimg = PhotoImage(file="../ico/stop.png")
nextimg = PhotoImage(file="../ico/next.png")
rewindimg = PhotoImage(file="../ico/rewind.png")
pauseimg = PhotoImage(file="../ico/pause.png")
mute = PhotoImage(file="../ico/mute.png")
unmute = PhotoImage(file="../ico/unmute.png")

def show_details():
    fileLable['text'] = "Playing " + os.path.basename(filename)

    file_type = os.path.splitext(filename)
    

    if file_type[1] == '.mp3':
        audio = MP3(filename)
        total_length = audio.info.length      
    else:
        a = mixer.Sound(filename)
        total_length = a.get_length()
        print(file_type[1])
    mins,secs = divmod(total_length,60)
    mins = round(mins)
    secs = round(secs)
    timeFormat = '{:02d}:{:02d}'.format(mins,secs)
    fileLength['text'] = "Total Length : " + timeFormat
    t1 = threading.Thread(target=start_count,args=(total_length,))
    t1.start()
    
def start_count(t):
    global paused
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:    
            mins,secs = divmod(current_time,60)
            mins = round(mins)
            secs = round(secs)
            timeFormat = '{:02d}:{:02d}'.format(mins,secs)
            currentLengthLabel['text'] = "Current Length : " + timeFormat
            time.sleep(1)
            current_time += 1

def play_btn():
    global paused
    if paused:
        statusbar['text'] = "Resumed Music" + " - " + os.path.basename(filename)
        mixer.music.unpause()
        paused=FALSE
    else:    
         try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Playin Music" + " - " + os.path.basename(filename)
            show_details()
            print("play button")
         except:
            tkinter.messagebox.showerror('File not found','Player 360 could not open music')
        
def stop_btn():
    mixer.music.stop()
    statusbar['text'] = "Stop Music"
    print("stop button")


def next_btn():
    print("next button")


def rewind_btn():
    play_btn()
    statusbar['text'] = "Rewind Music" + " - " + os.path.basename(filename)
    print("previous button")

paused = FALSE
def pause_btn():
    global paused
    paused = TRUE
    statusbar['text'] = "Paused Music" + " - " + os.path.basename(filename)
    mixer.music.pause()
    print("pause button")


isMute = FALSE    
def val_btn(val):
    volume = int(val) /100
    mixer.music.set_volume(volume)


def mute_btn():
    global isMute
    if isMute:
        muteBtn.configure(image=unmute)
        mixer.music.set_volume(0.7)
        scale.set(70)
        isMute = FALSE
    else:
        muteBtn.configure(image=mute)
        mixer.music.set_volume(0)
        scale.set(0)
        isMute = TRUE
    
    print("mute button")    


middleframe.pack()
playtBtn = Button(middleframe,image=playimg,command=play_btn).grid(row=0,column=1,padx=2)
stopBtn = Button(middleframe,image=stopimg,command=stop_btn).grid(row=0,column=2,padx=2)
pauseBtn = Button(middleframe,image=pauseimg,command=pause_btn).grid(row=0,column=3,padx=2)
nextBtn = Button(middleframe,image=nextimg,command=next_btn).grid(row=0,column=4,padx=2)
rewindBtn = Button(middleframe,image=rewindimg,command=rewind_btn).grid(row=0,column=0,padx=2)

bottomFrame = Frame(root)
bottomFrame.pack()

muteBtn = Button(bottomFrame,image=unmute,command=mute_btn)
muteBtn.grid(row=0,column=0,padx=2)

scale = Scale(bottomFrame,from_=0,to=100,orient=HORIZONTAL,command=val_btn)
scale.set(70)
scale.grid(row=0,column=1)

#Label(root,text="Welcome to Player360",relief=SUNKEN,anchor=W).pack(side=BOTTOM)

statusbar = Label(root,text="Welcome to Player360",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

def on_closing():
    stop_btn()
    root.destroy()

root.protocol("WM_DELETE_WINDOW",on_closing)

root.mainloop()