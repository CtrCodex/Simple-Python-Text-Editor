from tkinter import *
from tkinter.ttk import *
import pyttsx3
import tkinter.messagebox as tmsg
import os
from PIL import Image, ImageTk

from tkinter.filedialog import askopenfilename, asksaveasfilename


class TextEditorApp:
    def __init__(self, master):
        self.master = master
        master.geometry('470x550')
        master.resizable(False, False)
        master.title('Untitled - Notepad')

        self.file = None
        
        # Textarea
        self.textarea = Text(master, font='lucida 13')
        self.textarea.pack(side="bottom", expand=True, fill=BOTH)

        # Scrollbar
        self.scrollbar = Scrollbar(self.textarea)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.textarea.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textarea.yview)



        
        #----------------TOOLBAR-------------
        toolbar = Frame(master)
        toolbar.pack(side="top", fill="x")
                
        
        # TOOLBAR BUTTONS
        width, height = 13, 13  # Adjust width and height as needed
        
        # New Button
        new_image = Image.open("icons/new.png")
        resized_image = new_image.resize((width, height), Image.LANCZOS)

        # Creating a photoimage object with the resized image
        self.photo_new = ImageTk.PhotoImage(resized_image)
        
        # Creating the button with the resized image
        new_button = Button(toolbar, image=self.photo_new, command=self.new)
        new_button.pack(side="left", padx=4, pady=4)


        # Save Button
        save_image = Image.open("icons/save.png")
        resized_image = save_image.resize((width, height), Image.LANCZOS)
        self.save_image = ImageTk.PhotoImage(resized_image)
        new_button = Button(toolbar, image=self.save_image, command=self.save)
        new_button.pack(side="left", padx=4, pady=4)


        # Open Button
        open_image = Image.open("icons/open.png")
        resized_image = open_image.resize((width, height), Image.LANCZOS)
        self.open_image = ImageTk.PhotoImage(resized_image)
        new_button = Button(toolbar, image=self.open_image, command=self.open_file)
        new_button.pack(side="left", padx=4, pady=4)


        # Redo Button
        redo_image = Image.open("icons/redo.png")
        resized_image = redo_image.resize((width, height), Image.LANCZOS)
        self.redo_image = ImageTk.PhotoImage(resized_image)
        new_button = Button(toolbar, image=self.redo_image, command=self.redo)
        new_button.pack(side="left", padx=4, pady=4)
        
        
        # Undo Button
        undo_image = Image.open("icons/undo.png")
        resized_image = undo_image.resize((width, height), Image.LANCZOS)
        self.undo_image = ImageTk.PhotoImage(resized_image)
        new_button = Button(toolbar, image=self.undo_image, command=self.undo)
        new_button.pack(side="left", padx=4, pady=4)


        # Find Button
        find_image = Image.open("icons/find.png")
        resized_image = find_image.resize((width, height), Image.LANCZOS)
        self.find_image = ImageTk.PhotoImage(resized_image)
        new_button = Button(toolbar, image=self.find_image, command=self.undo)
        new_button.pack(side="left", padx=4, pady=4)



        # Menubar
        menubar = Menu(master)
        master.config(menu=menubar)

        # File menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label='Speak', command=self.speak)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.app_quit)
        menubar.add_cascade(label='File', menu=file_menu)

        # Edit menu
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label='Cut', command=self.cut)
        edit_menu.add_command(label='Copy', command=self.copy)
        edit_menu.add_command(label='Paste', command=self.paste)
        menubar.add_cascade(label='Edit', menu=edit_menu)

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label='View Help', command=self.view_help)
        help_menu.add_command(label='About Notepad', command=self.about_notepad)
        menubar.add_cascade(label='Help', menu=help_menu)
        
        #Tool Menu
        tool_menu = Menu(menubar)
        menubar.add_cascade(label="Tools", menu=tool_menu, underline=0)

        tool_menu.add_command(label="Change Color", command=self.change_color)
        tool_menu.add_command(label="Search", command=self.find_text, compound='left')
        
        # STATUS BAR
        status = Label(master, text="", border=1, relief=SUNKEN, anchor=W).pack(side="bottom", fill="x")
        
        
        # Binding Right Click Menu to Right button (Mouse)
        self.master.bind_class("Text", "<Button-3><ButtonRelease-3>", self.show_right_click_menu)
    
    
    
    
    
    
    
    
    
    
    
    def redo(self):
        pass
    
    def undo(self):
        pass
    
    def change_color(self):
        pass
        
    def find_text(self, event=None):
        pass

    # remove search tags and destroys the search box
    def find_text_cancel_button(search_toplevel):
        pass
        
    def new(self):
        self.master.title('Untitled - Notepad')
        self.file = None
        self.textarea.delete(1.0, END)

    def save(self):
        if self.file is None:
            self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                            filetypes=[('All Files', '*.*'), ('Text documents', '*.txt')])

            if self.file == '':
                self.file = None
            else:
                # Save as a new file
                with open(self.file, 'w') as f:
                    f.write(self.textarea.get(1.0, END))

                self.master.title(os.path.basename(self.file) + " - Notepad ")

        else:
            # Save the new file
            with open(self.file, 'w') as f:
                f.write(self.textarea.get(1.0, END))

            self.master.title(os.path.basename(self.file) + " - Notepad ")

    def open_file(self):
        self.file = askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text documents', '*.txt')])
        if self.file == '':
            self.file = None
        else:
            self.master.title(os.path.basename(self.file) + " - Notepad")
            self.textarea.delete(1.0, END)
            with open(self.file, 'r') as f:
                self.textarea.insert(1.0, f.read())

    def speak(self):
        audio = self.textarea.get(1.0, END)
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()

    def cut(self):
        self.textarea.event_generate(('<<Cut>>'))

    def copy(self):
        self.textarea.event_generate(('<<Copy>>'))

    def paste(self):
        self.textarea.event_generate(('<<Paste>>'))

    def view_help(self):
        tmsg.showinfo('help', " We will contact you soon")

    def about_notepad(self):
        tmsg.showinfo('About Notepad', 'This Notepad is created by Mayank Chaudhary @chaudhary_19')

    def app_quit(self):
        self.master.destroy()

    def right_click_menu(self, event):
        self.menu = Menu(self.master, tearoff=0)
        self.menu.add_command(label="Cut", command=self.cut)
        self.menu.add_command(label="Copy", command=self.copy)
        self.menu.add_command(label="Paste", command=self.paste)

    def show_right_click_menu(self, event):
        event_widget = event.widget
        self.menu.entryconfigure(
            "Cut",
            command=lambda: event_widget.event_generate("<<Cut>>")
        )
        self.menu.entryconfigure(
            "Copy",
            command=lambda: event_widget.event_generate("<<Copy>>")
        )
        self.menu.entryconfigure(
            "Paste",
            command=lambda: event_widget.event_generate("<<Paste>>")
        )

        self.menu.tk.call("tk_popup", self.menu, event.x_root, event.y_root)









if __name__ == "__main__":
    root = Tk()
    app = TextEditorApp(root)
    root.mainloop()