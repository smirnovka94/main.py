
from tkinter import *
from functions import *
from time import sleep

window = Tk()
window.title("Addings for Windows")
window.wm_attributes("-topmost", 1)
#window.geometry('300x250')
window.config(bg='#D9D8D7')
label = Label(window,
              text='',
              font=("Arial Narrow", 100),
              )
import psutil
battery1 = psutil.sensors_battery()
print(battery1[2])
while True:

    label.pack()
    label.grid(column=0, row=0)
    time_ = str(time_this_moment())
    battery_ = str(level_battery()) + '%'
    full_string = f'{time_} \n {battery_}'
    label.config(text=full_string)
    label.config(fg=critical_battery(10))
    window.update()
    sleep(60)


