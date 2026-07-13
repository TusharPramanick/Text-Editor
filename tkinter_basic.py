from tkinter import *

root = Tk()
root.title("Exploring Tkinter")

def display():
    print("Exploring Python Libraries")
    
showButton = Button(root, text='click',  command=display)
showButton.pack()

root.mainloop()
