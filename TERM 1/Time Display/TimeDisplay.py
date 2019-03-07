from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import calendar
import time
import datetime
def time_input():
        ahour = 8
        aminute = 19
        asecond = 0
        return ahour, aminute, asecond
def gmtnow():
    seconds = calendar.timegm(time.gmtime())
    current_second = seconds % 60
    minutes = seconds // 60
    current_minute = minutes % 60
    hours = minutes //  60
    current_hour = hours % 24
    #set the time zone
    current_hour = current_hour - 6
    if current_hour >= 12:
        tag = " PM"
    else:
        tag = " AM"
    #format the output
    timex = str(current_hour) + ":" + str(current_minute) + ":" + str(current_second) + tag
    #alarm
    ahour, aminute, asecond = time_input()
    if ahour >= 12:
        atag = " PM"
    else:
        atag = " AM"
    alarm = str(ahour) + ":" + str(aminute) + ":" + str(asecond) + atag
    if alarm == timex:
        winsound.Beep(750,2000)
        winsound.Beep(1000,1000)
        winsound.Beep(750,2000)
    return timex

def quit(*args):
    root.destroy()

def show_time():
    time = gmtnow()
    #show the time
    txt.set(time)
    #trigger the tick after 1000ms
    root.after(1000, show_time)
#use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen", False)
root.configure(background = 'black')
root.bind("x", quit)
root.after(1000, show_time)
fnt = font.Font(family = 'Century Gothic', size = 60, weight = "normal")
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
