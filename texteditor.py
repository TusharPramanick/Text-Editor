from tkinter import *
from tkinter import filedialog, messagebox

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(1.0, END)

def saveFile():
    global filename
    if filename == "Untitled":
        messagebox.showerror("Error", "Please save file with a name first (use Save As)")
        return
    t = text.get(1.0, END)
    try:
        f = open(filename, 'w')
        f.write(t)
        f.close()
    except:
        messagebox.showerror("Error", "Unable to save file")
    
def saveAs():
    global filename
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if not f:
        return
    t = text.get(1.0, END)
    try:
        f.write(t.rstrip())
        f.close()
        filename = f.name
        messagebox.showinfo("Success", "File saved successfully!")
    except:
        messagebox.showerror(title="Error", message="Unable to save...")
        
def openFile():
    global filename
    f = filedialog.askopenfile('r')
    if not f:
        return
    try:
        t = f.read()
        f.close()
        text.delete(1.0,END)
        text.insert(1.0, t)
        filename = f.name
        messagebox.showinfo("Success", "File opened successfully!")
    except:
        messagebox.showerror("Error", "Unable to open file")

#setting up the window
root = Tk()
root.title("Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

#Creating Text-box widget
text = Text(root, width=400, height=400, wrap='word', font=('Arial', 12), undo=True)
text.pack()

#Creating meanu-bar widget
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label='New', command=newFile)
filemenu.add_command(label='Save', command=saveFile)
filemenu.add_command(label='Save As', command=saveAs)
filemenu.add_command(label='Open', command=openFile)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)

root.config(menu=menubar)
root.mainloop()