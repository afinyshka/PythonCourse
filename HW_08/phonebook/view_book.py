from email.mime import image
import tkinter as tk
from unicodedata import name
import logic

def get_entry():
    value = input_line.get()
    return value


win = tk.Tk()
# photo = tk.PhotoImage(file = 'name')
# win.iconphoto(False, photo)
win.title("Calculator")
win.geometry(f"500x200+600+100")
win.resizable(False, False)
print('Its open')

input_line = tk.Entry(win)
input_line.grid(row=0, column=0, stick="we")

find = tk.Button(win, text="Find", command=logic.find_contact).grid(row=0, column=1, stick="we")
print("find = ", find)
delete = tk.Button(win, text="Delete").grid(row=1, column=1, stick="we")
add = tk.Button(win, text="Add").grid(row=2, column=1, stick="we")
change = tk.Button(win, text="Change").grid(row=3, column=1, stick="we")
export = tk.Button(win, text="Export").grid(row=4, column=1, stick="we")

win.grid_columnconfigure(0, minsize=360)
win.grid_columnconfigure(1, minsize=120)
# win.grid_rowconfigure(0, minsize=30)
# win.grid_rowconfigure(1, minsize=30)




win.mainloop()
