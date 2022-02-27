import os
import re
from tkinter import *
from tkinter.constants import *
from tkinter import messagebox
from time import *
f = open('../../file0.txt','r')
clicks = int(f.readline())
coins = int(f.readline())
clicksPerClick = int(f.readline())
f.close
root = Tk()
root.geometry('1920x1080')
root.title('Clicker game v1.0 - Game')
def save():
    global clicks
    global coins
    global clicksPerClick
    f = open("../../file0.txt","a")
    f.truncate(0)
    f.write(str(clicks))
    f.write(str(coins))
    f.write(str(clicksPerClick))
    f.close()
def addclick():
    global clicks
    global clicksPerClicks
    clicks += clicksPerClick
    save()
def showclicks():
    global clicks
    print(' ')
    print('You have')
    print(clicks)
    print('clicks')
    messagebox.showinfo(title="Clicker game v1.0 - Info", message="Check the console")
def shop():
    global coins
    global clicks
    global awnser
    global clicksPerClick
    smallest_item_cost = cost_of_lvl_1
    awnser = messagebox.askquestion(title='Clicker game v1.0 - Info', message="Check the console")
    if awnser == 'yes':
        print('Here is what you can afford')
        print('You can afford:')
        if coins >= 10:
            print('•Upgrade(lvl 1)')
            lvl_1_bought = input('would you like to buy it?(Y/N): ')
            if lvl_1_bought.lower() == 'y':
                coins = coins - cost_of_lvl_1
                clicksPerClick += 1
                print('Ok, you have bought 1 lvl 1 upgrade, you now have')
                print(coins)
                print('coins and')
                print(clicksPerClick)
                print('clicks per click')
                save()
        else:
            print('at this moment you cannot afford anything')
            save()
def sell():
    global clicks
    global coins
    awnser = messagebox.askquestion(title='Clicker game v1.0 - Info', message="Are you sure?")
    if awnser == 'yes':
        messagebox.showinfo(title='Clicker game v1.0 - Info', message='Check the console')
        coins = coins + clicks
        clicks = 0
        print('You have sold your clicks for money, you now own no clicks and')
        print(coins)
        print('coins')
        save()
clickme = Button(root, text='Click me!', command=lambda : addclick())
clickme.place(x=960, y=540)
clickmee = Button(root, text='show clickss', command=lambda : showclicks())
clickmee.place(x=0, y=0)
clickmeee = Button(root, text='shop', command=lambda : shop())
clickmeee.place(x=76, y=0)
clickmeeee = Button(root, text='sell', command=lambda : sell())
clickmeeee.place(x=113, y=0)
root.mainloop()

