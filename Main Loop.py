__author__ = 'Alex Corkin'

from Tkinter import *
import webbrowser

personalWebsite = "http://4lex.nz"
linkedIn = "http://nz.linkedin.com/in/alexcorkin"


def OpenUrl(desiredUrl):
    webbrowser.open_new(desiredUrl)

def placeholderFunction():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


class GUI:
    def __init__(self):
        # Set Up User Menu
        menubar = Menu(root)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Clear Data", command=placeholderFunction)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        contactMenu = Menu(menubar, tearoff=0)
        contactMenu.add_command(label="4lex.nz Website", command=lambda aurl=personalWebsite: OpenUrl(aurl))
        contactMenu.add_command(label="LinkedIn", command=lambda aurl=linkedIn: OpenUrl(aurl))
        menubar.add_cascade(label="Contact", menu=contactMenu)

        root.config(menu=menubar)

        # Show title
        titleMessage = StringVar()
        titleMessage.set("Welcome to the Simple Cipher Program")

        label = Label(root, textvariable=titleMessage, relief=RAISED, height=3)

        label.pack()


        # Get User message

        L1 = Label(root, text="User Name")
        L1.pack(side=LEFT)
        E1 = Entry(root, bd=5)

        E1.pack(side=RIGHT)


if __name__ == '__main__':
    root = Tk()
    GUI(root)
    root.mainloop()

#Get User passphrase
#Encrypt Message --> Pass details to Encryption.py
#Display Result --> Recieve and Display message



