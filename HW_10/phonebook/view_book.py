import tkinter as tk
import tkinter.messagebox as mb
import logic


def find_entry(texter):
    value = input_line.get()
    output_line_1 = tk.Label(win, relief=tk.SUNKEN,
                             text=texter, bg="Gray", justify=tk.RIGHT)
    output_text = logic.find_contact(value)
    output_line_2 = tk.Text(win, font="Arial 13",
                            height=6, width=44, padx= 10, bg="Gray")
    output_line_1.grid(row=1, column=0, columnspan=2, stick="wesn")
    output_line_2.grid(row=2, column=0, columnspan=2, rowspan=4, stick="sn")
    sc = tk.Scrollbar(win, orient=tk.VERTICAL)
    sc.grid(row=2, column=1, rowspan=4, sticky=tk.NS+tk.E)
    output_line_2.config(yscrollcommand=sc.set)
    sc.config(command=output_line_2.yview)
    output_line_2.insert(0.0, output_text)
    clear_1 = tk.Button(win, text="Clear", relief=tk.RAISED, command=lambda: del_widget_clear_inp_line(
        output_line_1, output_line_2, clear_1, sc))
    clear_1.grid(row=6, column=1, stick="we")

def add_entry():
    line_1 = tk.Label(win, text='Enter first name:', justify=tk.RIGHT)
    line_1.grid(row=1, column=0, stick="wesn",)
    line_2 = tk.Label(win, text='Enter last name:')
    line_2.grid(row=2, column=0, stick="wesn")
    line_3 = tk.Label(win, text='Enter phone number:')
    line_3.grid(row=3, column=0, stick="wesn")
    line_4 = tk.Label(win, text='Enter comment:')
    line_4.grid(row=4, column=0, stick="wesn")
    inp_line_1 = tk.Entry(win)
    inp_line_1.grid(row=1, column=1, stick="wesn")
    inp_line_2 = tk.Entry(win)
    inp_line_2.grid(row=2, column=1, stick="wesn")
    inp_line_3 = tk.Entry(win)
    inp_line_3.grid(row=3, column=1, stick="wesn")
    inp_line_4 = tk.Entry(win)
    inp_line_4.grid(row=4, column=1, stick="wesn")
    save = tk.Button(win, text="Save", relief=tk.RAISED, command=lambda: del_widgets_get_entry(inp_line_1, inp_line_2, inp_line_3,
                     inp_line_4, line_1, line_2, line_3, line_4, inp_line_1, inp_line_2, inp_line_3, inp_line_4, save, back))
    save.grid(row=5, column=1, stick="we")
    back = tk.Button(win, text="Back", relief=tk.RAISED, command=lambda: widgets_remove(
        line_1, line_2, line_3, line_4, inp_line_1, inp_line_2, inp_line_3, inp_line_4, save, back))
    back.grid(row=5, column=0, stick="we")

def delete_entry():
    value = input_line.get()
    if len(value) > 0:
        output_text = logic.find_contact(value)
        if output_text == 'There\'s no contact with this name. Try again':
            output_line_1 = tk.Label(
                win, relief=tk.SUNKEN, text='There\'s no contact with this name. Try again', bg="Gray", justify=tk.RIGHT)
            output_line_1.grid(row=1, column=0, columnspan=2, stick="wesn")
            btn_back = tk.Button(win, text="Back", relief=tk.RAISED, command=lambda: del_widget_clear_inp_line(
                btn_back, output_line_1))
            btn_back.grid(row=6, column=1, stick="we")
        else:
            output_line_1 = tk.Label(
                win, relief=tk.SUNKEN, text="Are you sure you want to remove the contact?", bg="Gray", justify=tk.RIGHT)
            output_line_1.grid(row=1, column=0, columnspan=2, stick="wesn")
            output_line_2 = tk.Text(win, font="Arial 13",
                                height=6, width=44, padx= 10, bg="Gray")
            output_line_2.grid(row=2, column=0, columnspan=2,
                            rowspan=4, stick="sn")
            sc = tk.Scrollbar(win, orient=tk.VERTICAL)
            sc.grid(row=2, column=1, rowspan=4, sticky=tk.NS+tk.E)
            output_line_2.config(yscrollcommand=sc.set)
            sc.config(command=output_line_2.yview)
            output_line_2.insert(1.0, output_text)
            check_text = output_text.split()
            print(check_text)
            btn_yes = tk.Button(win, text="Yes", relief=tk.RAISED, command=lambda: del_widgets_delete_entry(
                check_text[1], check_text[3], btn_yes, btn_no, output_line_1, output_line_2, sc))
            btn_yes.grid(row=6, column=0, stick="we")
            btn_no = tk.Button(win, text="No", relief=tk.RAISED, command=lambda: del_widget_clear_inp_line(
                btn_yes, btn_no, output_line_1, output_line_2, sc))
            btn_no.grid(row=6, column=1, stick="we")

def edit_entry():
    value = input_line.get()
    if len(value) > 0:
        output_text = logic.find_contact(value)
        if output_text == 'There\'s no contact with this name. Try again':
            output_line_1 = tk.Label(
                win, relief=tk.SUNKEN, text='There\'s no contact with this name. Try again', bg="Gray", justify=tk.RIGHT)
            output_line_1.grid(row=1, column=0, columnspan=2, stick="wesn")
            btn_back = tk.Button(win, text="Back", relief=tk.RAISED, command=lambda: del_widget_clear_inp_line(
                btn_back, output_line_1))
            btn_back.grid(row=6, column=1, stick="we")
        else:
            output_line_1 = tk.Label(
                win, relief=tk.SUNKEN, text="Do you want to edit the contact?", bg="Gray", justify=tk.RIGHT)
            if len(value) > 0:
                output_text = logic.find_contact(value)
            output_line_2 = tk.Text(win, font="Arial 13",
                                    height=6, width=44, padx= 10, bg="Gray")
            output_line_1.grid(row=1, column=0, columnspan=2, stick="wesn")
            output_line_2.grid(row=2, column=0, columnspan=2, rowspan=4, stick="sn")
            sc = tk.Scrollbar(win, orient=tk.VERTICAL)
            sc.grid(row=2, column=1, rowspan=4, sticky=tk.NS+tk.E)
            output_line_2.config(yscrollcommand=sc.set)
            sc.config(command=output_line_2.yview)
            output_line_2.insert(1.0, output_text)
            print('ot = ', output_text)
            check_text = output_text.split()
            print(check_text)
            confirm = tk.Button(win, text="Confirm", relief=tk.RAISED, command=lambda: del_widgets_create_edit_entry(
                check_text, confirm, esc, output_line_1, output_line_2, sc))
            confirm.grid(row=6, column=0, stick="we")
            esc = tk.Button(win, text="Esc", relief=tk.RAISED, command=lambda: del_widget_clear_inp_line(
                confirm, esc, output_line_1, output_line_2, sc))
            esc.grid(row=6, column=1, stick="we")

def get_entry_add(val_1, val_2, val_3, val_4):
    first_name = val_1.get()
    last_name = val_2.get()
    phone_num = val_3.get()
    comment = val_4.get()
    abonent = {'first_name': first_name, 'last_name': last_name,
               'phone_number': phone_num, 'comment': comment}
    logic.add_contact(abonent)
    return abonent

def get_entry_edit(del_1, del_2, val_1, val_2, val_3, val_4, *widget):
    first_name = val_1.get()
    last_name = val_2.get()
    phone_num = val_3.get()
    comment = val_4.get()
    new_abonent = {'first_name': first_name, 'last_name': last_name,
               'phone_number': phone_num, 'comment': comment}
    logic.change_contact(del_1, del_2, new_abonent)
    widgets_remove(*widget)
    clear_input_line()
    showinfo_create("The data has been successfully updated!")

def clear_input_line():
    input_line.delete(0, tk.END)

def widgets_remove(*widget):
    for i in widget:
        i.grid_remove()

def del_widget_clear_inp_line(*widget):
    clear_input_line()
    widgets_remove(*widget)

def showinfo_create(textik):
    mb.showinfo("Info", textik)

def del_widgets_create_edit_entry(lst, *widget):
    create_edit_entry(lst)
    widgets_remove(*widget)

def del_widgets_delete_entry(txt_1, txt_2, *widget):
    logic.delete_contact(txt_1, txt_2)
    widgets_remove(*widget)
    clear_input_line()
    showinfo_create("The data has been successfully deleted!")

def del_widgets_get_entry(txt_1, txt_2, txt_3, txt_4, *widget):
    get_entry_add(txt_1, txt_2, txt_3, txt_4)
    widgets_remove(*widget)
    clear_input_line()
    showinfo_create("The data has been successfully saved!")

def export_to_csv():
    logic.export_contacts_to_csv()
    showinfo_create("The data has been successfully exported to contacts_book.csv")

def create_edit_entry(lst: list):
    save_changes = tk.Button(win, text="Save changes", relief=tk.RAISED, command=lambda: get_entry_edit(
        lst[1], lst[3], inp_line_1, inp_line_2, inp_line_3, inp_line_4, line_1, line_2, line_3, line_4, inp_line_1, inp_line_2, inp_line_3, inp_line_4, save_changes, cancel))
    save_changes.grid(row=5, column=1, stick="we")
    cancel = tk.Button(win, text="Back", relief=tk.RAISED, command=lambda: del_widget_clear_inp_line(
        line_1, line_2, line_3, line_4, inp_line_1, inp_line_2, inp_line_3, inp_line_4, save_changes, cancel))
    cancel.grid(row=5, column=0, stick="we")
    line_1 = tk.Label(win, text='Enter first name:', justify=tk.RIGHT)
    line_1.grid(row=1, column=0, stick="wesn",)
    line_2 = tk.Label(win, text='Enter last name:')
    line_2.grid(row=2, column=0, stick="wesn")
    line_3 = tk.Label(win, text='Enter phone number:')
    line_3.grid(row=3, column=0, stick="wesn")
    line_4 = tk.Label(win, text='Enter comment:')
    line_4.grid(row=4, column=0, stick="wesn")
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
    find = tk.Button(win, text="Find", relief=tk.RAISED, command=lambda: find_entry("Contact's information:")).grid(row=0, column=2, stick="we")
    add = tk.Button(win, text="Create", relief=tk.RAISED, command=add_entry).grid(row=1, column=2, stick="we")
    delete = tk.Button(win, text="Remove", relief=tk.RAISED, command=delete_entry).grid(row=2, column=2, stick="we")
    edit = tk.Button(win, text="Edit", relief=tk.RAISED, command=edit_entry).grid(row=3, column=2, stick="we")
    export = tk.Button(win, text="Export", relief=tk.RAISED, command=export_to_csv).grid(row=4, column=2, stick="we")

    win.grid_columnconfigure(0, minsize=190)
    win.grid_columnconfigure(1, minsize=190)
    win.grid_columnconfigure(2, minsize=110)
    win.grid_rowconfigure(0, minsize=30)
    win.grid_rowconfigure(1, minsize=30)
    win.grid_rowconfigure(2, minsize=30)
    win.grid_rowconfigure(3, minsize=30)
    win.grid_rowconfigure(4, minsize=30)
    win.grid_rowconfigure(5, minsize=30)
    win.grid_rowconfigure(6, minsize=30)
    win.grid_rowconfigure(7, minsize=30)

    win.mainloop()
