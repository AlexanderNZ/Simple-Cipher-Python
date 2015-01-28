__author__ = 'Alex Corkin'

from Tkinter import *
import webbrowser

personalWebsite = "http://4lex.nz"
linkedIn = "http://nz.linkedin.com/in/alexcorkin"


def OpenUrl(desiredUrl):
    webbrowser.open_new(desiredUrl)

def placeholderFunction():
    filewin = Toplevel(mainWindow)
    button = Button(filewin, text="Do nothing button")
    button.pack()


# Render GUI
mainWindow = Tk()

# Widgets

# Program Title
programTitle = StringVar()
programTitle.set("Simple Cipher Program")
titleWidget = Label(mainWindow, textvariable=programTitle)

# User Action Radio Button

radioController = IntVar()
scramblerRadio = Radiobutton(mainWindow, text='Scramble a message', variable=radioController, value=1)
unscrambleRadio = Radiobutton(mainWindow, text='Unscramble a message', variable=radioController, value=2)

# Draws the window on screen complete with widgets

mainWindow.minsize(800, 600)
mainWindow.geometry('800x600-50+50')

titleWidget.pack()
scramblerRadio.pack()
unscrambleRadio.pack()
mainWindow.mainloop()

#Get User passphrase
#Encrypt Message --> Pass details to Encryption.py
#Display Result --> Recieve and Display message



