import tkinter as tk
import logic
import view

# self.entry = Entry(self.win)

input_line = None

def get_entry():
    # value = 'ak'
    value = input_line.get()
    return value

def insert_entry():
    output_line.delete(0,tk.END)
    output_line.insert(0, logic.find_contact())


if __name__ == '__main__':
    win = tk.Tk()
    # photo = tk.PhotoImage(file = 'name')
    # win.iconphoto(False, photo)
    win.title("Calculator")
    win.geometry(f"500x200+600+100")
    win.resizable(False, False)
    print('Its open')

    input_line = tk.Entry(win)
    input_line.grid(row=0, column=0, stick="we")
    # val_input_line = input_line.get()

    output_line = tk.Entry(win)
    output_line.grid(row=1, column=0, stick="we")

    # find = tk.Button(win, text="Find").grid(row=0, column=1, stick="we")
    find = tk.Button(win, text="Find", command=logic.find_contact).grid(row=0, column=1, stick="we")
    # find = tk.Button(win, text="Find", command=logic.find_contact).grid(row=0, column=1, stick="we")
    delete = tk.Button(win, text="Delete").grid(row=1, column=1, stick="we")
    add = tk.Button(win, text="Add").grid(row=2, column=1, stick="we")
    change = tk.Button(win, text="Change").grid(row=3, column=1, stick="we")
    export = tk.Button(win, text="Export").grid(row=4, column=1, stick="we")
    insert = tk.Button(win, text="Insert", command=insert_entry).grid(row=4, column=1, stick="we")

    win.grid_columnconfigure(0, minsize=360)
    win.grid_columnconfigure(1, minsize=120)
    # win.grid_rowconfigure(0, minsize=30)
    # win.grid_rowconfigure(1, minsize=30)




    win.mainloop()
