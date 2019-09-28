from tkinter import *

root = None
textBox = None

def buttonPushed():
    global textBox
    txt = textBox.get()
    print("The text is", txt)

def createTextBox(parent):
    global textBox
    textBox = Entry(parent)
    textBox.pack()

def main():
    global root
    root = Tk()
    w = Label(root, text="Hello")
    w.pack()
    butt = Button(root, text="Exit", command=buttonPushed)
    butt.pack()
    createTextBox(root)
    root.mainloop()

main()

