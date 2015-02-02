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


def showScrambleView():
    inputMessageLabel = Label(mainWindow, text="Enter the message to be scrambled")
    inputMessageLabel.pack()
    inputMessageEntry = Entry(mainWindow)
    inputMessageEntry.pack()
    showUnscrambleView.outputMessageLabel.pack_forget()
    showUnscrambleView.outputMessageEntry.pack_forget()

def showUnscrambleView():
    outputMessageLabel = Label(mainWindow, text="This is your scrambled message:")
    outputMessageLabel.pack()
    outputMessageText = Text(mainWindow)
    outputMessageText.insert(INSERT, "Test Text")
    outputMessageText.pack()
    showScrambleView.inputMessageLabel.pack_forget()
    showScrambleView.inputMessageEntry.pack_forget()

# Render GUI
mainWindow = Tk()

# Widgets

# Program Title
programTitle = StringVar()
programTitle.set("Simple Cipher Program")
titleWidget = Label(mainWindow, textvariable=programTitle)

# User Action Radio Button

radioController = IntVar()
scramblerRadio = Radiobutton(mainWindow, text='Scramble a message', variable=radioController, value=1,
                             command=showScrambleView)
unscrambleRadio = Radiobutton(mainWindow, text='Unscramble a message', variable=radioController, value=2,
                              command=showUnscrambleView)

# Draws the window on screen complete with widgets

mainWindow.minsize(800, 600)
mainWindow.geometry('800x600-50+50')

titleWidget.pack()
scramblerRadio.pack()
unscrambleRadio.pack()
mainWindow.mainloop()


#Encrypt Message --> Pass details to Encryption.py
#Display Result --> Recieve and Display message



