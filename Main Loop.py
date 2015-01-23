__author__ = 'Alex Corkin'

from Tkinter import *


def placeholderFunction():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


root = Tk()

# Set Up User Menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Clear Data", command=placeholderFunction)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

contactMenu = Menu(menubar, tearoff=0)
contactMenu.add_command(label="4lex.nz Website", command=placeholderFunction)
contactMenu.add_command(label="LinkedIn", command=placeholderFunction)
menubar.add_cascade(label="Contact", menu=contactMenu)

root.config(menu=menubar)

# Show title
titleMessage = StringVar()
titleMessage.set("Welcome to the Simple Cipher Program")

label = Label(root, textvariable=titleMessage, relief=RAISED, height=3)

label.pack()
root.mainloop()

# Give user Options
# Get User message
#Get User passphrase
#Encrypt Message --> Pass details to Encryption.py
#Display Result --> Recieve and Display message



