import tkinter as tk
import logic
import view

def get_entry(val_1, val_2, val_3, val_4):
    first_name = val_1.get()
    last_name = val_2.get()
    phone_num = val_3.get()
    comment = val_4.get()
    abonent = {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_num, 'comment' : comment}
    logic.add_contact(abonent)
    return abonent

def get_entry_delete(del_1, del_2, val_1, val_2, val_3, val_4):
    logic.delete_contact(del_1, del_2)
    get_entry(val_1, val_2, val_3, val_4)

def find_entry(texter):
    value = input_line.get()
    output_line_1 = tk.Label(win, text = texter, bg="Gray", justify=tk.RIGHT)
    if len(value) > 0:
        output_text = logic.find_contact(value)
    output_line_2 = tk.Label(win, text=output_text, bg="Gray", justify=tk.LEFT, padx=2, pady=2)
    output_line_1.grid(row=1, column=0, columnspan=2, stick="wesn")
    output_line_2.grid(row=2, column=0, columnspan=2, rowspan=4, stick="wesn", padx=2, pady=2)
    return output_text

def find_entry_del_widget(texter):
    value = input_line.get()
    output_line_1 = tk.Label(win, text = texter, bg="Gray", justify=tk.RIGHT)
    if len(value) > 0:
        output_text = logic.find_contact(value)
    output_line_2 = tk.Label(win, text=output_text, bg="Gray", justify=tk.LEFT, padx=2, pady=2)
    output_line_1.grid(row=1, column=0, columnspan=2, stick="wesn")
    output_line_2.grid(row=2, column=0, columnspan=2, rowspan=4, stick="wesn", padx=2, pady=2)
    clear_1 = tk.Button(win, text = "Clear", command=lambda: widgets_remove(output_line_1, output_line_2, clear_1))
    clear_1.grid(row=6, column=1, stick="we")

def widgets_remove(output_line_1, output_line_2, clear_1):
    output_line_1.grid_remove()
    output_line_2.grid_remove()
    clear_1.grid_forget()

def add_entry():
    widgets_remove(output_line_1, output_line_2, clear_1)
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
    save = tk.Button(win, text="Save", command=lambda: get_entry(inp_line_1, inp_line_2, inp_line_3, inp_line_4)).grid(row=5, column=1, stick="we")

def delete_entry():
    output_text = find_entry("Are you sure you want to remove the contact?")
    check_text = output_text.split()
    print(check_text)
    if output_text != "":
        btn_yes = tk.Button(win, text = "Yes", command=lambda: logic.delete_contact(check_text[1], check_text[3]))
        btn_yes.grid(row=6, column=0, stick="we")
        btn_no = tk.Button(win, text = "No", command=clear_input_line)
        btn_no.grid(row=6, column=1, stick="we")
    
def clear_input_line():
    input_line.delete(0, tk.END)

def edit_entry():
    output_text = find_entry('Do you want to edit the contact?')
    print('ot = ',output_text)
    check_text = output_text.split()
    print(check_text)
    if output_text != "":
        tk.Button(win, text = "Confirm", command=lambda: create_edit_entry(check_text)).grid(row=6, column=0, stick="we")
        tk.Button(win, text = "Esc", command=clear_input_line).grid(row=6, column=1, stick="we")

def create_edit_entry(lst: list):
    tk.Label(win, text='Enter first name:', justify=tk.RIGHT).grid(row=1, column=0, stick="wesn",)
    tk.Label(win, text='Enter last name:').grid(row=2, column=0, stick="wesn")
    tk.Label(win, text='Enter phone number:').grid(row=3, column=0, stick="wesn")
    tk.Label(win, text='Enter comment:').grid(row=4, column=0, stick="wesn")
    inp_line_1 = tk.Entry(win)
    inp_line_1.grid(row=1, column=1, stick="wesn")
    inp_line_1.insert(0, lst[1])
    inp_line_2 = tk.Entry(win)
    inp_line_2.grid(row=2, column=1, stick="wesn")
    inp_line_2.insert(0, lst[3])
    inp_line_3 = tk.Entry(win)
    inp_line_3.grid(row=3, column=1, stick="wesn")
    inp_line_3.insert(0, lst[5])
    inp_line_4 = tk.Entry(win)
    inp_line_4.grid(row=4, column=1, stick="wesn")
    inp_line_4.insert(0, lst[7])
    confirm = tk.Button(win, text="Save changes", command=lambda: get_entry_delete(lst[1], lst[3], inp_line_1, inp_line_2, inp_line_3, inp_line_4)).grid(row=5, column=1, stick="we")



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

# SUNKEN, RAISED, GROOVE, RIDGE
    find = tk.Button(win, text="Find", relief=tk.RAISED, command=lambda: find_entry_del_widget("Contact's information:")).grid(row=0, column=2, stick="we")
    add = tk.Button(win, text="Create", command=add_entry).grid(row=1, column=2, stick="we")
    delete = tk.Button(win, text="Remove", command=delete_entry).grid(row=2, column=2, stick="we")
    edit = tk.Button(win, text="Edit", command=edit_entry).grid(row=3, column=2, stick="we")
    export = tk.Button(win, text="Export", command=logic.export_contacts_to_csv).grid(row=4, column=2, stick="we")
    # clear = tk.Button(win, text="Clear", command=insert_entry).grid(row=5, column=2, stick="we")

    win.grid_columnconfigure(0, minsize=180)
    win.grid_columnconfigure(1, minsize=180)
    win.grid_columnconfigure(2, minsize=120)
    win.grid_rowconfigure(0, minsize=30)
    win.grid_rowconfigure(1, minsize=30)
    win.grid_rowconfigure(2, minsize=30)
    win.grid_rowconfigure(3, minsize=30)
    win.grid_rowconfigure(4, minsize=30)
    win.grid_rowconfigure(5, minsize=30)
    win.grid_rowconfigure(6, minsize=30)
    win.grid_rowconfigure(7, minsize=30)

    win.mainloop()
