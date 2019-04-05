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
        self.mediumFont = tkinter.font.Font(family="PibotoLt", size=40)
        self.normalFont = tkinter.font.Font(family="PibotoLt", size=20)
        self.smallFont = tkinter.font.Font(family="PibotoLt", size=6)

    def setupGUI(self):
        self.grid(row=0, column=0)

        # Weather & news frame to contain weather/news info
        # For weather, column 0 = info, column 1 = icon
        weather_news_frame = Frame(self, width=400, height=500, bg='black')
        weather_news_frame.grid(row=0, column=0)

        GUI.weather_label1 = Label(weather_news_frame, text="Weather today", fg='white', bg='black',
                                   font=self.mediumFont)
        GUI.weather_label1.grid(row=0, column=0)

        icon = PhotoImage(file="weather_icons/clear.gif")
        icon = icon.subsample(8)
        icon_label = Label(weather_news_frame, borderwidth=0, image=icon)
        icon_label.photo = icon
        icon_label.grid(row=0, column=1)

        # Adjust this width for spacing
        frame_placeholder = Frame(self, width=300, height=10, bg='black')
        frame_placeholder.grid(row=0, column=1)

        # Time frame to hold time & date in grid
        time_frame = Frame(self, width=400, height=500, bg='black')
        time_frame.grid(row=0, column=2, sticky=E)
        GUI.time_label = Label(time_frame, text=strftime("%I:%M %p", time.localtime()), fg='white', bg='black',
                               font=self.largeFont)
        GUI.time_label.grid(row=0, column=0, sticky=E)

        GUI.date_label = Label(time_frame, text=strftime("%A, %B %d", time.localtime()), fg='white', bg='black',
                               font=self.normalFont)
        GUI.date_label.grid(row=1, column=0, sticky=E)

        self.configure(background='black')

    def updateGUI(self):
        # Constantly updates the time until the program is stopped
        GUI.time_label.configure(text=strftime("%I:%M %p", time.localtime()))
        GUI.date_label.configure(text=strftime("%A, %B %d", time.localtime()))

        window.after(1000, mirror.updateGUI)

    def updateWeather(self):
        GUI.weather_label1.configure(text=strftime("Updated weather %S", time.localtime()))
        window.after(50000, mirror.updateWeather)


window = Tk()
window.title("Test window")
window.geometry('800x600')
window.configure(background='black')

#This removes borders from GUI
#window.overrideredirect(1)

mirror = GUI(window)
mirror.setupGUI()
window.after(1000, mirror.updateGUI)
window.after(1000, mirror.updateWeather)
window.mainloop()
