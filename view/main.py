from tkinter import *


root = Tk()
root.geometry('300x300')
root.title("Player360")
root.iconbitmap(r'../ico/360icon.ico')

text = Label(root,text="Music Player")
text.pack()

img = PhotoImage(file="../ico/play.png")

photo = Label(root,image=img).pack()

root.mainloop()