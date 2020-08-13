import os
import time
import threading
from tkinter import *
from pygame import mixer
import tkinter.messagebox
from mutagen.mp3 import MP3
from tkinter import filedialog


root = Tk()


statusbar = Label(root,text="Welcome to Player360",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)


playList = []


#config tapbar
menuBar = Menu(root)
root.config(menu=menuBar)
#make topbar
def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    add_to_playList(filename)

def add_to_playList(f):
    index = 0
    playList.insert(index,f)
    f = os.path.basename(f)
    playListBox.insert(index,f)
    index += 1
   



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


root.geometry('425x225')
root.title("Player360")
root.iconbitmap(r'../ico/360icon.ico')

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)

rightFrame = Frame(root)
rightFrame.pack()

topFrame = Frame(rightFrame)
topFrame.pack()



fileLength = Label(topFrame,text="Total Length : --:--")
fileLength.pack()

currentLengthLabel = Label(topFrame,text="Current Length : --:--",relief = GROOVE)
currentLengthLabel.pack(pady=5)






playimg = PhotoImage(file="../ico/play.png")
stopimg = PhotoImage(file="../ico/stop.png")
nextimg = PhotoImage(file="../ico/next.png")
rewindimg = PhotoImage(file="../ico/rewind.png")
pauseimg = PhotoImage(file="../ico/pause.png")
mute = PhotoImage(file="../ico/mute.png")
unmute = PhotoImage(file="../ico/unmute.png")


playListBox = Listbox(leftFrame)
playListBox.pack(padx=20)

btn_add = Button(leftFrame,text="+ Add",command=browse_file)
btn_add.pack(side=LEFT,padx=20)

btn_del = Button(leftFrame,text="- Delete")
btn_del.pack(side=LEFT,padx=10)

def show_details():
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
            selected_song = playListBox.curselection()
            selected_song = int(selected_song[0])
            play_it = playList[selected_song]
            print(play_it)
            mixer.music.load(play_it)
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

middleframe = Frame(rightFrame)

middleframe.pack()
playtBtn = Button(middleframe,image=playimg,command=play_btn).grid(row=0,column=1,padx=2)
stopBtn = Button(middleframe,image=stopimg,command=stop_btn).grid(row=0,column=2,padx=2)
pauseBtn = Button(middleframe,image=pauseimg,command=pause_btn).grid(row=0,column=3,padx=2)
nextBtn = Button(middleframe,image=nextimg,command=next_btn).grid(row=0,column=4,padx=2)
rewindBtn = Button(middleframe,image=rewindimg,command=rewind_btn).grid(row=0,column=0,padx=2)

bottomFrame = Frame(rightFrame)
bottomFrame.pack()

muteBtn = Button(bottomFrame,image=unmute,command=mute_btn)
muteBtn.grid(row=0,column=0,padx=2)

scale = Scale(bottomFrame,from_=0,to=100,orient=HORIZONTAL,command=val_btn)
scale.set(70)
scale.grid(row=0,column=1)

#Label(root,text="Welcome to Player360",relief=SUNKEN,anchor=W).pack(side=BOTTOM)



def on_closing():
    stop_btn()
    root.destroy()

root.protocol("WM_DELETE_WINDOW",on_closing)

root.mainloop()