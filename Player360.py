import os
import time
import threading
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from pygame import mixer
import tkinter.messagebox
from mutagen.mp3 import MP3
from tkinter import filedialog


root = ThemedTk(theme="yaru")


statusbar = ttk.Label(root,text="Welcome to Player360",relief=SUNKEN,anchor=W,font="Times 10 bold")
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


root.geometry('610x233')
root.resizable(0, 0)
root.title("Player360")
root.iconbitmap(r'./ico/360icon.ico')

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)

rightFrame = Frame(root)
rightFrame.pack()

topFrame = Frame(rightFrame)
topFrame.pack()



fileLength = ttk.Label(topFrame,text="Total Length : --:--",font="Arial 10 bold")
fileLength.pack()

currentLengthLabel = ttk.Label(topFrame,text="Current Length : --:--",relief = GROOVE,font="Arial 8 bold")
currentLengthLabel.pack(pady=5)






playimg = PhotoImage(file="./ico/play.png")
stopimg = PhotoImage(file="./ico/stop.png")
nextimg = PhotoImage(file="./ico/next.png")
rewindimg = PhotoImage(file="./ico/rewind.png")
pauseimg = PhotoImage(file="./ico/pause.png")
mute = PhotoImage(file="./ico/mute.png")
unmute = PhotoImage(file="./ico/unmute.png")


playListBox = Listbox(leftFrame)
playListBox.pack(padx=20)

btn_add = ttk.Button(leftFrame,text="+ Add",command=browse_file)
btn_add.pack(side=LEFT)

def del_song():
    selected_song = playListBox.curselection()
    selected_song = int(selected_song[0])
    playListBox.delete(selected_song)
    playList.pop(selected_song)

btn_del = ttk.Button(leftFrame,text="- Delete",command=del_song)
btn_del.pack(side=LEFT)

def show_details(play_it):
    file_type = os.path.splitext(play_it)
    

    if file_type[1] == '.mp3':
        audio = MP3(play_it)
        total_length = audio.info.length      
    else:
        a = mixer.Sound(play_it)
        total_length = a.get_length()
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
            stop_btn()
            time.sleep(1) 
            selected_song = playListBox.curselection()
            selected_song = int(selected_song[0])
            play_it = playList[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text'] = "Playin Music" + " - " + os.path.basename(play_it)
            show_details(play_it)
         except:
            tkinter.messagebox.showerror('File not found','Player 360 could not open music')
        
def stop_btn():
    mixer.music.stop()
    statusbar['text'] = "Stop Music"


def next_btn():
    stop_btn()


def rewind_btn():
    play_btn()
    statusbar['text'] = "Rewind Music" + " - " + os.path.basename(filename)

paused = FALSE
def pause_btn():
    global paused
    paused = TRUE
    statusbar['text'] = "Paused Music" + " - " + os.path.basename(filename)
    mixer.music.pause()



isMute = FALSE    
def val_btn(val):
    volume = float(val) /100
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
      

middleframe = Frame(rightFrame)

middleframe.pack()
playtBtn = ttk.Button(middleframe,image=playimg,command=play_btn).grid(row=0,column=1,padx=2)
stopBtn = ttk.Button(middleframe,image=stopimg,command=stop_btn).grid(row=0,column=2,padx=2)
pauseBtn = ttk.Button(middleframe,image=pauseimg,command=pause_btn).grid(row=0,column=3,padx=2)
nextBtn = ttk.Button(middleframe,image=nextimg,command=next_btn).grid(row=0,column=4,padx=2)
rewindBtn = ttk.Button(middleframe,image=rewindimg,command=rewind_btn).grid(row=0,column=0,padx=2)

bottomFrame = Frame(rightFrame)
bottomFrame.pack()

muteBtn = ttk.Button(bottomFrame,image=unmute,command=mute_btn)
muteBtn.grid(row=0,column=0,padx=2)

scale = ttk.Scale(bottomFrame,from_=0,to=100,orient=HORIZONTAL,command=val_btn)
scale.set(70)
scale.grid(row=0,column=1)

#Label(root,text="Welcome to Player360",relief=SUNKEN,anchor=W).pack(side=BOTTOM)



def on_closing():
    stop_btn()
    root.destroy()

root.protocol("WM_DELETE_WINDOW",on_closing)

root.mainloop()