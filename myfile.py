from cProfile import label
from tkinter import *


window = Tk()
label1 = Label(window, text='Title')
label1.grid(row=0, column=0)

label2 = Label(window, text='Author')
label2.grid(row=0, column=2)

label3 = Label(window, text='Year')
label3.grid(row=1, column=0)

label4 = Label(window, text='Book number')
label4.grid(row=1, column=2)

title_text = StringVar()
input1 = Entry(window, textvariable=title_text)
input1.grid(row=0, column=1)

author_text = StringVar()
input2 = Entry(window, textvariable=author_text)
input2.grid(row=0, column=3)

year_num = IntVar()
input3 = Entry(window, textvariable=year_num)
input3.grid(row=1, column=1)

book_num = IntVar()
input4 = Entry(window, textvariable=book_num)
input4.grid(row=1, column=3)


listview1 = Listbox(window, height=6, width=35)
listview1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll_bar = Scrollbar(window)
scroll_bar.grid(row=2, column=2, rowspan=6)

listview1.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=listview1.yview)


window.mainloop()