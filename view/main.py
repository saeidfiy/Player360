from tkinter import *


root = Tk()
root.geometry('300x300')
root.title("Player360")
root.iconbitmap(r'../ico/360icon.ico')

text = Label(root,text="Music Player")
text.pack()

playimg = PhotoImage(file="../ico/play.png")



def play_btn():
    print("play button")


    
btn = Button(root,image=playimg,command=play_btn).pack()

root.mainloop()