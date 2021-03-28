#!/usr/bin/env python2
#url_list_tk.py
from Tkinter import *
import tkFileDialog as tkf
import webbrowser as webb

def create_listbox():
    file1 = tkf.askopenfilename(initialdir = "/sdb2", title = "Selectfile")
    print (file1)

    comment_list = []
    main_list = []
    pos = 0

    with open(file1) as reader:
        ls = reader.read().split("\n")
        for i in ls:
            if i.startswith("#"):
                comment_list.append(i)
            else:
                main_list.append(i)

    def CurSelect(mouse1Event):
        #create an object with the tk attribute 'widget', extracts data from memory
        mouse1Event_widget = mouse1Event.widget
        #create an object processed by tk method 'curselection()', show index key
        selection=mouse1Event_widget.curselection()

        #debug
        #print main_list[int(selection[0])]

        #open website
        webb.open(main_list[int(selection[0])])

        #create an object processed by py method 'get()', show value of a index key
        valueDisplay=mouse1Event_widget.get(selection)

        #print valueDisplay

    mylistbox=Listbox(width = 100,height=20,font=('times',14))
    mylistbox.bind('<<ListboxSelect>>',CurSelect)
    mylistbox.pack()

    for items in comment_list:
        mylistbox.insert(END,items)

    mylistbox.mainloop()

create_listbox()
