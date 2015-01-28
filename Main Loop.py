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
mainWindow.minsize(800, 600)
mainWindow.geometry('800x600-50+50')
mainWindow.mainloop()
# Widgets

# Draws the window on screen complete with widgets


#Get User passphrase
#Encrypt Message --> Pass details to Encryption.py
#Display Result --> Recieve and Display message



