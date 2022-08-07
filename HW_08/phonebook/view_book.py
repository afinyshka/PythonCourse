import tkinter as tk
import logic
import view

def get_entry(entry_text):
    value = entry_text.get()
    return value

def find_entry():
    value = input_line.get()
    output_line_1 = tk.Label(win, text = "Contact's information:", bg="Gray", justify=tk.RIGHT)
    output_text = logic.find_contact(value)
    output_line_2 = tk.Label(win, text=output_text, bg="Gray", justify=tk.LEFT, padx=2, pady=2)
    output_line_1.grid(row=1, column=0, columnspan=2, stick="wesn")
    output_line_2.grid(row=2, column=0, columnspan=2, rowspan=5, stick="wesn", padx=2, pady=2)

def add_entry():
    tk.Label(win, text='Enter first name:', justify=tk.RIGHT).grid(row=1, column=0, stick="wesn",)
    tk.Label(win, text='Enter last name:').grid(row=2, column=0, stick="wesn")
    tk.Label(win, text='Enter phone number:').grid(row=3, column=0, stick="wesn")
    tk.Label(win, text='Enter comment:').grid(row=4, column=0, stick="wesn")
    inp_line_1 = tk.Entry(win)
    inp_line_1.grid(row=1, column=1, stick="wesn")
    inp_line_2 = tk.Entry(win)
    inp_line_2.grid(row=2, column=1, stick="wesn")
    inp_line_3 = tk.Entry(win)
    inp_line_3.grid(row=3, column=1, stick="wesn")
    inp_line_4 = tk.Entry(win)
    inp_line_4.grid(row=4, column=1, stick="wesn")
    save = tk.Button(win, text="Save", command=add_to_phonebook).grid(row=5, column=1, stick="we")
    return [inp_line_1, inp_line_2, inp_line_3, inp_line_4]
    

def add_to_phonebook():
    first_name = add_entry()[0].get()
    last_name = add_entry()[1].get()
    phone_num = add_entry()[2].get()
    comment = add_entry()[3].get()
    abonent = {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_num, 'comment' : comment}
    view.print_dict(abonent)
    logic.add_contact(abonent)




if __name__ == '__main__':
    win = tk.Tk()
    # photo = tk.PhotoImage(file = 'name')
    # win.iconphoto(False, photo)
    win.title("Phone book")
    win.geometry(f"500x300+600+100")
    win.resizable(False, True)
    print('Its open')

    input_line = tk.Entry(win)
    input_line.grid(row=0, column=0, columnspan=2, stick="we")

    find = tk.Button(win, text="Find", command=find_entry).grid(row=0, column=2, stick="we")
    add = tk.Button(win, text="Add", command=add_entry).grid(row=1, column=2, stick="we")
    delete = tk.Button(win, text="Delete").grid(row=2, column=2, stick="we")
    change = tk.Button(win, text="Change").grid(row=3, column=2, stick="we")
    export = tk.Button(win, text="Export", command=logic.export_contacts_to_csv).grid(row=4, column=2, stick="we")
    # insert = tk.Button(win, text="Insert", command=insert_entry).grid(row=5, column=2, stick="we")

    win.grid_columnconfigure(0, minsize=180)
    win.grid_columnconfigure(1, minsize=180)
    win.grid_columnconfigure(2, minsize=120)
    # win.grid_rowconfigure(0, minsize=30)
    # win.grid_rowconfigure(1, minsize=30)

    win.mainloop()
