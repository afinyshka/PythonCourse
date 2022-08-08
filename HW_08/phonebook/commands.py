# def find_entry(texter):
#     value = input_line.get()
#     output_line_1 = tk.Label(win, text = texter, bg="Gray", justify=tk.RIGHT)
#     if len(value) > 0:
#         output_text = logic.find_contact(value)
#     output_line_2 = tk.Label(win, text=output_text, bg="Gray", justify=tk.LEFT, padx=2, pady=2)
#     output_line_1.grid(row=1, column=0, columnspan=2, stick="wesn")
#     output_line_2.grid(row=2, column=0, columnspan=2, rowspan=4, stick="wesn", padx=2, pady=2)
#     return output_text

# def find_entry_del_widget(texter):
#     value = input_line.get()
#     output_line_1 = tk.Label(win, text = texter, bg="Gray", justify=tk.RIGHT)
#     if len(value) > 0:
#         output_text = logic.find_contact(value)
#     output_line_2 = tk.Label(win, text=output_text, bg="Gray", justify=tk.LEFT, padx=2, pady=2)
#     output_line_1.grid(row=1, column=0, columnspan=2, stick="wesn")
#     output_line_2.grid(row=2, column=0, columnspan=2, rowspan=4, stick="wesn", padx=2, pady=2)
#     clear_1 = tk.Button(win, text = "Clear", command=lambda: widgets_remove(output_line_1, output_line_2, clear_1))
#     clear_1.grid(row=6, column=1, stick="we")


# def widgets_remove(widgwt_1, widgwt_2, widgwt_3, widgwt_4):
#     widgwt_1.grid_remove()
#     widgwt_2.grid_remove()
#     widgwt_3.grid_remove()
#     widgwt_4.grid_forget()

# def find_entry(texter):
#     value = input_line.get()
#     output_line_1 = tk.Label(win, relief=tk.SUNKEN, text = texter, bg="Gray", justify=tk.RIGHT)
#     if len(value) > 0:
#         output_text = logic.find_contact(value)
#     output_line_2 = tk.Text(win, font="Arial 13", height = 6, width = 45, bg= "Gray")
#     output_line_1.grid(row=1, column=0, columnspan=2, stick="wesn")
#     output_line_2.grid(row=2, column=0, columnspan=2, rowspan=4, stick="sn")
#     sc = tk.Scrollbar(win, orient=tk.VERTICAL)
#     sc.grid(row=2, column=1, rowspan=4, sticky=tk.NS+tk.E)
#     output_line_2.config(yscrollcommand=sc.set)
#     sc.config(command=output_line_2.yview)
#     output_line_2.insert(1.0, output_text)
#     return output_text
