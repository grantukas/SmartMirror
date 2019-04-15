import http
from tkinter import *
import tkinter.font
import time
from time import strftime
from darksky import forecast
from datetime import date, timedelta


WIDTH = 800
HEIGHT = 600

key = '93a522f375502ea4e4a091c06d034ff1'
ORANGE = 33.779638, (-117.853700)


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

        GUI.weather_label1 = Label(weather_news_frame, text="Loading weather...", fg='white', bg='black',
                                   font=self.normalFont, justify=LEFT)
        GUI.weather_label1.grid(row=0, column=0, sticky=W)
        GUI.weather_label2 = Label(weather_news_frame, text="Loading weather...", fg='white', bg='black',
                                   font=self.normalFont, justify=LEFT)
        GUI.weather_label2.grid(row=1, column=0, sticky=W)
        GUI.weather_label3 = Label(weather_news_frame, text="Loading weather...", fg='white', bg='black',
                                   font=self.normalFont, justify=LEFT)
        GUI.weather_label3.grid(row=2, column=0, sticky=W)
        GUI.weather_label4 = Label(weather_news_frame, text="Loading weather...", fg='white', bg='black',
                                   font=self.normalFont, justify=LEFT)
        GUI.weather_label4.grid(row=3, column=0, sticky=W)
        GUI.weather_label5 = Label(weather_news_frame, text="Loading weather...", fg='white', bg='black',
                                   font=self.normalFont, justify=LEFT)
        GUI.weather_label5.grid(row=4, column=0, sticky=W)
        GUI.weather_label6 = Label(weather_news_frame, text="Loading weather...", fg='white', bg='black',
                                   font=self.normalFont, justify=LEFT)
        GUI.weather_label6.grid(row=5, column=0, sticky=W)
        GUI.weather_label7 = Label(weather_news_frame, text="Loading weather...", fg='white', bg='black',
                                   font=self.normalFont, justify=LEFT)
        GUI.weather_label7.grid(row=6, column=0, sticky=W)
        GUI.weather_label8 = Label(weather_news_frame, text="Loading weather...", fg='white', bg='black',
                                   font=self.normalFont, justify=LEFT)
        GUI.weather_label8.grid(row=7, column=0, sticky=W)

        icon = PhotoImage(file="weather_icons/partly-cloudy-day.gif")
        icon = icon.subsample(10)

        #Set up labels to hold weather icons
        GUI.icon_label = Label(weather_news_frame, borderwidth=0, image=icon)
        GUI.icon_label.photo = icon
        GUI.icon_label.grid(row=0, column=1, sticky=W)
        GUI.icon_label2 = Label(weather_news_frame, borderwidth=0, image=icon)
        GUI.icon_label2.grid(row=1, column=1, sticky=W)
        GUI.icon_label3 = Label(weather_news_frame, borderwidth=0, image=icon)
        GUI.icon_label3.grid(row=2, column=1, sticky=W)
        GUI.icon_label4 = Label(weather_news_frame, borderwidth=0, image=icon)
        GUI.icon_label4.grid(row=3, column=1, sticky=W)
        GUI.icon_label5 = Label(weather_news_frame, borderwidth=0, image=icon)
        GUI.icon_label5.grid(row=4, column=1, sticky=W)
        GUI.icon_label6 = Label(weather_news_frame, borderwidth=0, image=icon)
        GUI.icon_label6.grid(row=5, column=1, sticky=W)
        GUI.icon_label7 = Label(weather_news_frame, borderwidth=0, image=icon)
        GUI.icon_label7.grid(row=6, column=1, sticky=W)
        GUI.icon_label8 = Label(weather_news_frame, borderwidth=0, image=icon)
        GUI.icon_label8.grid(row=7, column=1, sticky=W)

        # Adjust this width for spacing
        frame_placeholder = Frame(self, width=300, height=10, bg='black')
        frame_placeholder.grid(row=0, column=1)

        # Time frame to hold time & date in grid
        time_frame = Frame(self, width=400, height=500, bg='black')
        time_frame.grid(row=0, column=2, sticky=NE)
        GUI.time_label = Label(time_frame, text=strftime("%I:%M %p", time.localtime()), fg='white', bg='black',
                               font=self.largeFont)
        GUI.time_label.grid(row=0, column=0, sticky=NE)

        GUI.date_label = Label(time_frame, text=strftime("%A, %B %d", time.localtime()), fg='white', bg='black',
                               font=self.normalFont)
        GUI.date_label.grid(row=1, column=0, sticky=NE)

        self.configure(background='black')

    def updateGUI(self):
        # Constantly updates the time until the program is stopped
        GUI.time_label.configure(text=strftime("%I:%M %p", time.localtime()))
        GUI.date_label.configure(text=strftime("%A, %B %d", time.localtime()))

        window.after(1000, mirror.updateGUI)

    def updateWeather(self):
        weekday = date.today()
        daily_summary = ''
        weather_today = ''
        weather_list = []
        today_icon = ''
        icons_list = []

        counter = 0
        with forecast(key, *ORANGE) as orange:
            daily_summary += orange.daily.summary
            for day in orange.daily:
                day = dict(day=date.strftime(weekday, '%a'),
                           sum=day.summary,
                           tempMin=day.temperatureMin,
                           tempMax=day.temperatureMax,
                           icon=day.icon
                           )
                # Save each of these in a list to display to GUI
                if counter == 0:
                    weather_today += ('Today: High {tempMax} | Low {tempMin}'.format(**day))
                    today_icon = ('{icon}'.format(**day))
                    weekday += timedelta(days=1)
                    counter += 1
                else:
                    weather_list.append('{day}: High {tempMax} | Low {tempMin}'.format(**day))
                    icons_list.append('{icon}'.format(**day))
                    weekday += timedelta(days=1)
                    counter += 1

        GUI.weather_label1.configure(text=weather_today)

        icon_path = 'weather_icons/'
        today_icon += '.gif'
        icon_path += today_icon
        icon = PhotoImage(file=icon_path)
        icon = icon.subsample(10)
        GUI.icon_label.configure(image=icon)
        GUI.icon_label.photo = icon

        for x in range(0, len(weather_list)):
            temp_icon_path = 'weather_icons/'
            temp_icon_name = icons_list[x]
            temp_icon_name += '.gif'
            temp_icon_path += temp_icon_name
            temp_icon = PhotoImage(file=temp_icon_path)
            temp_icon = temp_icon.subsample(10)

            print(temp_icon_path)
            if x == 0:
                GUI.weather_label2.configure(text=weather_list[x])
                GUI.icon_label2.configure(image=temp_icon)
                GUI.icon_label2.photo = temp_icon
            if x == 1:
                GUI.weather_label3.configure(text=weather_list[x])
                GUI.icon_label3.configure(image=temp_icon)
                GUI.icon_label3.photo = temp_icon
            if x == 2:
                GUI.weather_label4.configure(text=weather_list[x])
                GUI.icon_label4.configure(image=temp_icon)
                GUI.icon_label4.photo = temp_icon
            if x == 3:
                GUI.weather_label5.configure(text=weather_list[x])
                GUI.icon_label5.configure(image=temp_icon)
                GUI.icon_label5.photo = temp_icon
            if x == 4:
                GUI.weather_label6.configure(text=weather_list[x])
                GUI.icon_label6.configure(image=temp_icon)
                GUI.icon_label6.photo = temp_icon
            if x == 5:
                GUI.weather_label7.configure(text=weather_list[x])
                GUI.icon_label7.configure(image=temp_icon)
                GUI.icon_label7.photo = temp_icon
            if x == 6:
                GUI.weather_label8.configure(text=weather_list[x])
                GUI.icon_label8.configure(image=temp_icon)
                GUI.icon_label8.photo = temp_icon

        window.after(500000, mirror.updateWeather)


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
