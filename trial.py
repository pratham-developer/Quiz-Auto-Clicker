
import mouse
import time as tt
from tkinter import ttk
from ttkthemes import themed_tk as tk
import tkinter as bk
from tkinter import messagebox as mb
import pygame
import csv

root = tk.ThemedTk()
root.geometry("400x150")
root.resizable(width=False, height=False)
root.title("Quiz Auto-Clicker")
root.iconbitmap(r'assets\icon.ico')
pygame.mixer.init()
pygame.mixer.music.load("assets\Tech.ogg")



def readCsv(filename) -> dict:
    # Read the CSV and return a dict of coordinates.
    cor = {}
    with open(filename,'r') as f:
        csvReader = csv.reader(f, delimiter=',')
        check = True
        for item in csvReader:
            if check: itemOne,itemTwo = item[1],item[2];check=False; continue
            cor[item[0]]= {itemOne:item[1], itemTwo:item[2]}
    return cor

def writeCsv(filename, option, x, y):
    tempLL = []
    with open(filename, "r") as f:
        dt = csv.DictReader(f)
        for i in dt:
            tempLL.append(i)
    for i in tempLL:
        if i.get("option") == option:
            i["x"] = x
            i["y"] = y
    print(tempLL)
    with open('assets/location.csv', 'w', newline='') as f:
        fieldnames = ['option','x','y']
        kalam = csv.DictWriter(f, fieldnames=fieldnames)
        kalam.writeheader()
        for i in tempLL:
            kalam.writerow(i)

cord = readCsv("assets/location.csv")

#Run the clicker

def optionA():
    delay = var1.get()
    if delay == 1:
        num = int(230)
        time = float(0.075)

    elif delay == 2:
        num = int(120)
        time = float(0.15)

    elif delay == 3:
        num = int(65)
        time = float(0.3)

    else:
        mb.showerror(title="Quiz Auto-Clicker", message="Please choose the delay time.")
        return

    root.iconify()
    tt.sleep(0.05)
    i = 0
    while i < num:
        i = i + 1
        mouse.move(x=cord.get("A")["x"], y=cord.get("A")["y"], absolute=True)
        mouse.click('left')
        tt.sleep(time)
    if i==num:
        tt.sleep(0.05)
        root.update()
        root.deiconify()
        pygame.mixer.music.play()

def optionB():
    delay = var1.get()
    if delay == 1:
        num = int(230)
        time = float(0.075)

    elif delay == 2:
        num = int(120)
        time = float(0.15)

    elif delay == 3:
        num = int(65)
        time = float(0.3)

    else:
        mb.showerror(title="Quiz Auto-Clicker", message="Please choose the delay time.")
        return

    root.iconify()
    tt.sleep(0.05)
    i = 0
    while i < num:
        i = i + 1
        mouse.move(x=cord.get("B")["x"], y=cord.get("B")["y"], absolute=True)
        mouse.click('left')
        tt.sleep(time)
    if i==num:
        tt.sleep(0.05)
        root.update()
        root.deiconify()
        pygame.mixer.music.play()

def optionC():
    delay = var1.get()
    if delay == 1:
        num = int(230)
        time = float(0.075)

    elif delay == 2:
        num = int(120)
        time = float(0.15)

    elif delay == 3:
        num = int(65)
        time = float(0.3)

    else:
        mb.showerror(title="Quiz Auto-Clicker", message="Please choose the delay time.")
        return

    root.iconify()
    tt.sleep(0.05)
    i = 0
    while i < num:
        i = i + 1
        mouse.move(x=cord.get("C")["x"], y=cord.get("C")["y"], absolute=True)
        mouse.click('left')
        tt.sleep(time)
    if i==num:
        tt.sleep(0.05)
        root.update()
        root.deiconify()
        pygame.mixer.music.play()

def optionD():
    delay = var1.get()
    if delay == 1:
        num = int(230)
        time = float(0.75)

    elif delay == 2:
        num = int(120)
        time = float(0.15)

    elif delay == 3:
        num = int(65)
        time = float(0.3)

    else:
        mb.showerror(title="Quiz Auto-Clicker", message="Please choose the delay time.")
        return

    root.iconify()
    tt.sleep(0.05)
    i = 0
    while i < num:
        i = i + 1
        mouse.move(x=cord.get("D")["x"], y=cord.get("D")["y"], absolute=True)
        mouse.click('left')
        tt.sleep(time)
    if i==num:
        tt.sleep(0.05)
        root.update()
        root.deiconify()
        pygame.mixer.music.play()


def e():
    mb.showinfo(title="Quiz Auto Clicker", message="This is an auto-clicker specially designed for quizes going on EdTech platforms. It runs for around 10 seconds after clicking. For any help reach out on any Telegram ID - @PrathamDev or @navsrijan ")


#Change the co-ordinates

def callA(event):

    (x, y) = mouse.get_position()
    ques = mb.askquestion(title="Quiz Auto Clicker", message="Are you sure you want to locate the option A to a new position?")
    if ques=="yes":
        writeCsv("assets/location.csv", "A", x, y)

        tt.sleep(0.2)
        mb.showinfo(title="Quiz Auto Clicker",
                           message="The location has been succesfully changed. Please restart the application for the change to take effect.")

    else:
        pass

def callB(event):

    (x, y) = mouse.get_position()
    ques = mb.askquestion(title="Quiz Auto Clicker", message="Are you sure you want to locate the option B to a new position?")
    if ques=="yes":
        writeCsv("assets/location.csv", "B", x, y)
        tt.sleep(0.2)
        mb.showinfo(title="Quiz Auto Clicker",
                           message="The location has been succesfully changed. Please restart the application for the change to take effect.")

    else:
        pass



def callC(event):

    (x, y) = mouse.get_position()
    ques = mb.askquestion(title="Quiz Auto Clicker", message="Are you sure you want to locate the option C to a new position?")
    if ques=="yes":
        writeCsv("assets/location.csv", "C", x, y)
        tt.sleep(0.2)
        mb.showinfo(title="Quiz Auto Clicker",
                           message="The location has been succesfully changed. Please restart the application for the change to take effect.")

    else:
        pass


def callD(event):

    (x, y) = mouse.get_position()
    ques = mb.askquestion(title="Quiz Auto Clicker", message="Are you sure you want to locate the option D to a new position?")
    if ques=="yes":
        writeCsv("assets/location.csv", "D", x, y)
        tt.sleep(0.2)
        mb.showinfo(title="Quiz Auto Clicker",
                                   message="The location has been succesfully changed. Please restart the application for the change to take effect.")

    else:
        pass




def reset(event):

    (x, y) = mouse.get_position()
    ques = mb.askquestion(title="Quiz Auto Clicker", message="Are you sure you want to reset all the options to their default locations?")
    if ques=="yes":

     writeCsv("assets/location.csv", "A", 1298, 534)
     writeCsv("assets/location.csv", "B", 1392, 542)
     writeCsv("assets/location.csv", "C", 1294, 632)
     writeCsv("assets/location.csv", "D", 1385, 635)
     tt.sleep(0.2)
     mb.showinfo(title="Quiz Auto Clicker",
                           message="The locations have been succesfully changed. Please restart the application for the change to take effect.")

    else:
        pass

def calli():
   mb.showinfo(title="Quiz Auto-Clicker", message="Please locate the cursor and press the option name key (A,B,C,D) to calibrate its new location. Just press (R) to reset all the locations.")

textin =  bk.StringVar()
var1 = bk.IntVar()
textin.set("Please choose a suitable option")

lbl = ttk.Label(root, text="Delay Time", font=("Arial Black", 8),justify='center',)
lbl.place(x=300, y=10)

A = ttk.Button(root, text="A", command = optionA)
A.place(x= 50, y=20)

B = ttk.Button(root, text="B", command = optionB)
B.place(x=170, y=20)


C = ttk.Button(root, text="C", command = optionC)
C.place(x= 50, y=60)

D = ttk.Button(root, text="D", command = optionD)
D.place(x=170, y=60)

info  = ttk.Entry(root, state= 'disabled', width = 30, font=("Arial Black", 10),justify='center', textvar = textin)
info.place(x=10, y=100)

radio_low= ttk.Radiobutton(root, text="Low", variable=var1, value=1)
radio_low.place(x=300, y=30)

radio_medium= ttk.Radiobutton(root, text="Medium", variable=var1, value=2)
radio_medium.place(x=300, y=52)

radio_high= ttk.Radiobutton(root, text="High", variable=var1, value=3)
radio_high.place(x=300, y=74)


men = bk.Menu(root)
root.config(menu=men)
sec = bk.Menu(men)

men.add_cascade(menu=sec, label="Help")

sec.add_command(label="Calibrate", command=calli)
sec.add_command(label="About", command=e)

root.bind("<a>", callA)
root.bind("<b>", callB)
root.bind("<c>", callC)
root.bind("<d>", callD)
root.bind("<r>", reset)



root.mainloop()