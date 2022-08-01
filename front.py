from tkinter import *
import database


def view_command():
    listview1.delete(0,END)
    for row in database.view():
        listview1.insert(END,row)

def search_command():
    listview1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_num.get(),book_num.get()):
        listview1.insert(END,row)

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

year_num = StringVar()
input3 = Entry(window, textvariable=year_num)
input3.grid(row=1, column=1)

book_num = StringVar()
input4 = Entry(window, textvariable=book_num)
input4.grid(row=1, column=3)


listview1 = Listbox(window, height=6, width=35)
listview1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll_bar = Scrollbar(window)
scroll_bar.grid(row=2, column=2, rowspan=6)

listview1.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=listview1.yview)



'''
buttons and configuration below
b1 - b6 where b means button ie variable name
'''
b1 = Button(window, text='view all', width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search entry', width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add entry', width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update', width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete', width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=12)
b6.grid(row=7, column=3)


window.mainloop()