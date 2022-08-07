import tkinter as tk
import logic
import view

# input_line = None

def find_entry():
    value = input_line.get()
    output_line_1 = tk.Label(win, text = "Contact's information:", bg="Gray", justify=tk.RIGHT)
    output_text = logic.find_contact(value)
    output_line_2 = tk.Label(win, text=output_text, bg="Gray", justify=tk.LEFT, padx=2, pady=2)
    output_line_1.grid(row=1, column=0, stick="wesn")
    output_line_2.grid(row=2, column=0, rowspan=5, stick="wesn", padx=2, pady=2)

def add_entry():
    first_name = tk.Entry(win)
    first_name.insert(0, "Enter first name: ")
    first_name.grid(row=1, column=0, stick="wesn")

    last_name = tk.Entry(win).grid(row=2, column=0, stick="wesn")
    phone_num = tk.Entry(win).grid(row=3, column=0, stick="wesn")
    comment = tk.Entry(win).grid(row=4, column=0, stick="wesn")
    abonent = {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_num, 'comment' : comment}
    logic.add_contact(abonent)
    view.success_saved()
    return abonent



if __name__ == '__main__':
    win = tk.Tk()
    # photo = tk.PhotoImage(file = 'name')
    # win.iconphoto(False, photo)
    win.title("Calculator")
    win.geometry(f"500x300+600+100")
    win.resizable(False, True)
    print('Its open')

    input_line = tk.Entry(win)
    input_line.grid(row=0, column=0, stick="we")

    find = tk.Button(win, text="Find", command=find_entry).grid(row=0, column=1, stick="we")
    delete = tk.Button(win, text="Delete").grid(row=1, column=1, stick="we")
    add = tk.Button(win, text="Add", command=add_entry).grid(row=2, column=1, stick="we")
    change = tk.Button(win, text="Change").grid(row=3, column=1, stick="we")
    export = tk.Button(win, text="Export", command=logic.export_contacts_to_csv).grid(row=4, column=1, stick="we")
    # insert = tk.Button(win, text="Insert", command=insert_entry).grid(row=5, column=1, stick="we")

    win.grid_columnconfigure(0, minsize=360)
    win.grid_columnconfigure(1, minsize=120)
    # win.grid_rowconfigure(0, minsize=30)
    # win.grid_rowconfigure(1, minsize=30)




    win.mainloop()
