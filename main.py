import tkinter as tk
from tkinter import filedialog, messagebox

LIGHT_THEME = {
    "bg": "white",
    "fg": "black",
    "cursor": "black",
    "status_bg": "#EAEAEA",
    "status_fg": "black"
}

DARK_THEME = {
    "bg": "#1E1E1E",
    "fg": "white",
    "cursor": "white",
    "status_bg": "#2D2D2D",
    "status_fg": "white"
}

light = LIGHT_THEME
dark = DARK_THEME

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.root.config(bg=dark['bg'])
        self.filename = None

        # Creating Text widget
        self.text = tk.Text(self.root, width=80, height=25, wrap='word', bg=dark['bg'], fg=dark['fg'], insertbackground=dark['cursor'], font=('Arial', 12), undo=True)
        self.text.pack(fill='both', expand=True)

        # Creating Menu bar
        self.menubar = tk.Menu(self.root, bg=dark['bg'], fg=dark['fg'])
        
        # Creating File menu
        self.filemenu = tk.Menu(self.menubar, tearoff=0, )
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        
        # Adding Features inside File menu
        self.filemenu.add_command(label='New', command=self.new_file)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save', command=self.save_file)
        self.filemenu.add_command(label='Save As', command=self.save_as)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Quit', command=self.root.quit)
    
        # Creating View menu
        self.view_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="View", menu=self.view_menu)
        
        # Adding Features inside View menu
        self.word_wrap = tk.BooleanVar()
        self.word_wrap.set(True)
        self.view_menu.add_checkbutton(label='Word Wrap', variable=self.word_wrap, command=self.word_wrap_update, onvalue=1, offvalue=0)
        
        self.status_bar_toggle = tk.BooleanVar()
        self.status_bar_toggle.set(True)
        self.view_menu.add_checkbutton(label='Status Bar', variable=self.status_bar_toggle, command=self.status_bar_update, onvalue=1, offvalue=0)
        
        self.theme_toggle = tk.BooleanVar()
        self.theme_toggle.set(True)
        self.view_menu.add_checkbutton(label='Dark Mode', variable=self.theme_toggle, command=self.theme_update, onvalue=1, offvalue=0)
        
        # Creating Status bar
        self.status_bar = tk.Label(self.root, anchor=tk.SW, text="Ln: 1 " + "  --  " + " Col: 0", bd='5px', bg=dark['bg'], fg=dark['fg'])
        self.status_bar.pack(side='bottom', fill='x')
        
        self.text.bind('<KeyRelease>', self.update_status_bar)
        self.text.bind('<ButtonRelease-1>', self.update_status_bar)
        
        self.root.config(menu=self.menubar)
        
    # Word Wrap update
    def word_wrap_update(self):
        if self.word_wrap.get() :
            self.text.config(wrap='word')
        else:
            self.text.config(wrap='none')
    
    # Status Bar toggle
    def status_bar_update(self):
        if self.status_bar_toggle.get() :
            self.status_bar.pack(side='bottom', fill='x')
        else:
            self.status_bar.pack_forget()
            
    # Dark Theme implementation
    def theme_update(self):
        if self.theme_toggle.get():
            self.text.config(bg=dark['bg'], fg=dark['fg'], insertbackground=dark['cursor'])
            self.root.config(bg=dark['bg'])
            self.menubar.config(bg=dark['bg'], fg=dark['fg'])
            self.status_bar.config(bg=dark['bg'], fg=dark['fg'])
        else:
            self.text.config(bg=light['bg'], fg=light['fg'], insertbackground=light['cursor'])
            self.root.config(bg=light['bg'])
            self.menubar.config(bg=light['bg'], fg=light['fg'])
            self.status_bar.config(bg=light['bg'], fg=light['fg'])
    
    # Creating updating status bar
    def update_status_bar(self, event=None):
        line, column = self.text.index('insert').split('.')
        self.status_bar.config(text= f"Ln: {line}  --  Col:  {column}")
        
    # Command methods for menu options
    def new_file(self):
        self.filename = None
        self.text.delete("1.0", tk.END)

    def save_file(self):
        if not self.filename:
            self.save_as()
            return

        content = self.text.get("1.0", tk.END)
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write(content.rstrip('\n'))
            messagebox.showinfo("Success", "File saved successfully!")
        except OSError as exc:
            messagebox.showerror("Error", f"Unable to save file: {exc}")

    def save_as(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension='.txt',
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
        )
        if not file_path:
            return

        content = self.text.get("1.0", tk.END)
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content.rstrip('\n'))
            self.filename = file_path
            messagebox.showinfo("Success", "File saved successfully!")
        except OSError as exc:
            messagebox.showerror("Error", f"Unable to save file: {exc}")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
        )
        if not file_path:
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.text.delete("1.0", tk.END)
            self.text.insert("1.0", content)
            self.filename = file_path
            messagebox.showinfo("Success", "File opened successfully!")
        except OSError as exc:
            messagebox.showerror("Error", f"Unable to open file: {exc}")


if __name__ == '__main__':
    root = tk.Tk()
    TextEditor(root)
    root.mainloop()