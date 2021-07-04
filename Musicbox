import pygame
from pygame import mixer
from tkinter import *
import tkinter.messagebox
import os
def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()
def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()
def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()
def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()
def handleProtocol():
    # open a dialog
    if tkinter.messagebox.askokcancel("Notice", "Are you sure to close the window"):
       # close the application
       songstatus.set("Stopped")
       mixer.music.stop()
       root.destroy()

if __name__ == '__main__':
    root=Tk()
    root.title('Aniketh Music player project')
    mixer.init()
    pygame.init()
    songstatus=StringVar()
    songstatus.set("choosing")
    #playlist---------------
    playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=40)
    playlist.grid(columnspan=5)
    os.chdir(r'C:\AniTemp\MyPlaylist')
    songs=os.listdir()
    for s in songs:
        playlist.insert(END,s)
    playbtn=Button(root,text="play",command=playsong)
    playbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
    playbtn.grid(row=1,column=0)
    pausebtn=Button(root,text="Pause",command=pausesong)
    pausebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
    pausebtn.grid(row=1,column=1)
    stopbtn=Button(root,text="Stop",command=stopsong)
    stopbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
    stopbtn.grid(row=1,column=2)
    Resumebtn=Button(root,text="Resume",command=resumesong)
    Resumebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
    Resumebtn.grid(row=1,column=3)
    root.protocol("WM_DELETE_WINDOW", handleProtocol)
    root.mainloop()

