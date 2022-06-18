from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import tkinter.font as tkFont

class Function:

    def open_file(self):
        try:
            f = askopenfile(mode='r', defaultextension=".txt",
                            filetypes=[("All File", "*.*"), ("Text Documents", "*.txt")])
            if f.name != "":
                root.title(f"{f.name} -Learning Akshat Legend Text Editor")
                textarea.delete("1.0", "end")
                textarea.insert('1.0', f.read())
                self.title = f.name
                f.close()
            else:
                pass
        except Exception as e:
            print(e)

    def save_file_as(self, text):
        try:
            f = asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents")])
            if f.name != None:
                f.write(str(text))
                f.close()
                root.title(f"{f.name} -Learning Akshat Legend Text Editor")
                self.title = f.name

        except Exception as e:
            print(e)

    def save(self, text):
        if root.title().startswith("Welcome To Learning Akshat Legend Text Editor"):
            Function().save_file_as(text)
        else:
            with open(root.title().replace("-Welcome To Learning Akshat Legend Text Editor", ""), 'w') as f:
                f.write(text)
                f.close()


root = Tk()
function = Function()

root.title("Welcome To Learning Akshat Legend Text Editor")
root.geometry("550x470")

root.minsize(200, 100)
root.maxsize(900, 800)

vscroolbar = Scrollbar(root, orient="vertical")
textarea = Text(root, height=434, width=644, yscrollcommand=vscroolbar.set,undo=True)


menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(
    menu,
    tearoff=0

)

menu.add_cascade(
    label="File",
    menu=file_menu
)
def undo():
    try:
        textarea.edit_undo()
    except Exception as e:
        pass

def redo():
    try:
        textarea.edit_redo()
    except Exception as e:
        pass

def select(event):
    Font_tuple = (combobox_font.get(),int(combobox_size.get()) ,  combobox_style.get().lower())
    print(Font_tuple)

    textarea.tag_add("bt2", "sel.first", "sel.last")
    textarea.tag_config("bt2", font=Font_tuple)

    #textarea.configure(font=Font_tuple)

# def font_style(event):
#     return combobox_style.get()
#
#
# def font_size(event):
#     return combobox_size.get()
#
# def font_family(event):
#     return combobox_font.get()

root.wm_resizable(False,False)



panedwindow = PanedWindow()
panedwindow2 = PanedWindow()

undo = Button(panedwindow2,text="Undo",width=25,padx=50,command=undo)
redo = Button(panedwindow2,text="Redo",width=25,padx=50,command=redo)

panedwindow2.add(undo)
panedwindow2.add(redo)

combobox_size = ttk.Combobox(panedwindow,width = 5, textvariable = StringVar())
combobox_font = ttk.Combobox(panedwindow,width = 27, textvariable = StringVar())
combobox_style = ttk.Combobox(panedwindow,width = 17, textvariable = StringVar())


combobox_font['values'] = font.families()
combobox_size['values'] = (8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72)
combobox_style['values'] = ("Bold", "Italic", "Underline", "Normal")


panedwindow.add(combobox_style)
panedwindow.add(combobox_size)
panedwindow.add(combobox_font)

combobox_style.bind("<<ComboboxSelected>>",select)
combobox_size.bind("<<ComboboxSelected>>",select)
combobox_font.bind("<<ComboboxSelected>>",select)

combobox_style.current(0)
combobox_font.current(11)
combobox_size.current(0)


panedwindow.pack(side=TOP,fill=BOTH,expand=1)
panedwindow2.pack(side=BOTTOM,fill=BOTH,expand=1)




vscroolbar.pack(side=RIGHT, fill="y")
file_menu.add_command(label="New")
file_menu.add_command(label="Open", command=lambda: function.open_file())
file_menu.add_command(label="Save", command=lambda: function.save(textarea.get(1.0, END)))
file_menu.add_command(label="Save As", command=lambda: function.save_file_as(textarea.get(1.0, END)))
#file_menu.add_command(label="Format", command=lambda: font_box())
file_menu.add_command(label="Exit", command=root.destroy)

textarea.pack()

root.mainloop()

