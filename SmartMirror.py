import http
from tkinter import *
import tkinter.font
import time
from time import strftime

WIDTH = 800
HEIGHT = 600

class GUI(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.largeFont = tkinter.font.Font(family="PibotoLt", size=70)
        self.normalFont = tkinter.font.Font(family="PibotoLt", size=20)
        self.smallFont = tkinter.font.Font(family="PibotoLt", size=6)

    def setupGUI(self):
        self.pack(fill=BOTH, expand=1)

        time_frame = Frame(self, width=400, height=105)
        GUI.textTime = Text(time_frame, bg='black', fg='white', font=self.largeFont, bd=0, highlightbackground='black')
        GUI.textTime.pack()
        time_frame.pack(side=TOP, anchor=NE)
        time_frame.pack_propagate(False)

        #Date frame
        date_frame = Frame(self, width=400, height=50)
        GUI.textDate = Text(date_frame, bg='black', fg='white', font=self.normalFont, bd=0, highlightbackground='black')
        GUI.textDate.pack()
        date_frame.pack(side=TOP, anchor=NE)
        date_frame.pack_propagate(False)

        #self.configure(background='black')
        #Do stuff to setup gui here

    def updateGUI(self):
        # Constantly updates the time until the program is stopped
        GUI.textTime.config(state=NORMAL)
        GUI.textTime.delete("1.0", END)
        GUI.textTime.insert(END, strftime("%I:%M %p", time.localtime()))


        GUI.textDate.config(state=NORMAL)
        GUI.textDate.delete("1.0", END)
        GUI.textDate.insert(END, strftime("%A, %B %d", time.localtime()))
        
        window.after(1000, mirror.updateGUI)


window = Tk()
window.title("Test window")
window.geometry('800x600')
window.configure(background='black')

#This removes borders from GUI
#window.overrideredirect(1)

mirror = GUI(window)
mirror.setupGUI()
window.after(1000, mirror.updateGUI)
window.mainloop()
