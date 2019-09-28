from tkinter import *

root = None
myText = None
count = 0

def buttonPushed():
    global count
    global myText

    count += 1
    myText.set("Clicked %d" %(count))

def addTextLabel(root):
    global myText
    myText = StringVar()
    myText.set("")
    myLable = Label(root, textvariable=myText)
    myLable.pack()

def main():
    global root
    root = Tk()
    w = Label(root, text="Hello")
    w.pack()
    butt = Button(root, text="Exit", command=buttonPushed)
    butt.pack()
    addTextLabel(root)
    root.mainloop()

main()

