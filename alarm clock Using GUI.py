from tkinter import *
import datetime as dt
import time
import winsound as ws

# defining the function for the alarm clock
def alarm(setAlarmTimer):
    while True:
        time.sleep(1)
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H : %M : %S")
        currentDate = actualTime.strftime("%d / %m / %Y")
        the_message = "Current Time: " + str(currentTime)
        print(the_message)
        if currentTime == setAlarmTimer:
            ws.PlaySound("sound.wav", ws.SND_ASYNC)
            break

def getAlarmTime():
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"
    alarm(alarmSetTime)

def resetTimer():
    hour.set('')
    minute.set('')
    second.set('')

# creating the GUI for the application
guiWindow = Tk()
guiWindow.title("The Alarm Clock")
guiWindow.geometry("475x225")
guiWindow.config(bg = "#87BDD8")
guiWindow.resizable(width = False, height = False)

# Header
heading = Label(
    guiWindow,
    text="Alarm Clock",
    font=("Arial", 25),
    fg="#36486B",
    bg="#87BDD8",
    width=20,
    pady=10
    ).grid(row=0, columnspan=4)

timeFormat = Label(
    guiWindow,
    text="Remember to set time in 24-hour format!",
    fg="white",
    bg="#36486B",
    font=("Arial", 12)
    ).grid(row=4, columnspan=4)

add_time = Label(
    guiWindow,
    text="Hour",
    font=60,
    fg="white",
    bg="#87BDD8"
    ).grid(row=2, column=1)

add_time = Label(
    guiWindow,
    text="Minutes",
    font=60,
    fg="white",
    bg="#87BDD8"
    ).grid(row=2, column=2)

add_time = Label(
    guiWindow,
    text="Second",
    font=60,
    fg="white",
    bg="#87BDD8"
    ).grid(row=2, column=3)

setAlarm = Label(
    guiWindow,
    text="Set Time for Alarm: ",
    fg="white",
    bg="#034F84",
    relief="solid",
    font=("Helevetica", 8, "bold")
    ).grid(row=3, column=0, padx=10, pady=10, ipadx=1, ipady=1)

hour = StringVar()
minute = StringVar()
second = StringVar()

hourTime = Entry(
    guiWindow,
    textvariable=hour,
    bg="#FEFBD8",
    width=4,
    font=(20)
    ).grid(row=3, column=1)

minuteTime = Entry(
    guiWindow,
    textvariable=minute,
    bg="#FEFBD8",
    width=4,
    font=(20)
    ).grid(row=3, column=2)

secondTime = Entry(
    guiWindow,
    textvariable=second,
    bg="#FEFBD8",
    width=4,
    font=(20)
    ).grid(row=3, column=3)

submit = Button(
    guiWindow,
    text="Set The Alarm",
    fg="white",
    bg="#82B74B",
    width=15,
    command=getAlarmTime,
    font=(20),
    
    ).grid(row=5, padx=5)

reset = Button(
    guiWindow,
    text="Reset Timer",
    fg="white",
    bg="#B74848",
    width=15,
    command=resetTimer,
    font=(20)
    ).grid(row=5, column=2, pady=5)

guiWindow.mainloop()